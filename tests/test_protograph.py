#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import logging
import os
import os.path
import pytest
import re
import requests
import yaml

from attrdict import AttrDict
from contextlib import contextmanager
from os import listdir
from os.path import isfile, join
# our common code
from . import _get_paths, _get_file_parts, _logging, _load_lines, ErrorCount, \
              _load_records, _get_dirs


logger = logging.getLogger(__name__)


# *******
# setup
# *******
@pytest.fixture
def protograph():
    """ ensure we have protograph definitions, lable used as key """
    fname = 'tests/bmeg.protograph.yaml'
    url = 'https://raw.githubusercontent.com/biostream' \
          '/bmeg-etl/master/bmeg.protograph.yaml'

    if not os.path.isfile(fname):
        response = requests.get(url)
        f = open(fname, 'w')
        f.write(response.content)
        f.close()

    with open(fname, 'r') as stream:
        protograph_list = yaml.load(stream)

    protograph_object = AttrDict({})
    for i in protograph_list:
        p = AttrDict(i)
        protograph_object[p.label] = p
    return protograph_object


# *******
# utilities
# *******
def _get_properties(protograph, path, node_type):
    """ get the protograph properties for the path, ignore 0 length files,
        indexed by label """
    (project, label, extention) = _get_file_parts(path)
    logger.debug(path)
    assert protograph[label], '{} not found in protograph'.format(path)
    properties = protograph[label]
    properties = protograph[label]
    # only check if file actually has a length > 0
    statinfo = os.stat(path)
    if statinfo.st_size:
        assert node_type in properties, '{} not found in protograph {}'.format(node_type, path)  # noqa
        labled = AttrDict({})
        for n in properties[node_type]:
            labled[n['label']] = AttrDict(n)
        return labled
    else:
        return {}


def _exists(val):
    """ empty test """
    if isinstance(val, basestring) and not val.strip():
        return False
    if isinstance(val, (float, int, long)):
        return True  # 0.0 numbers ok
    if not val:
        return False
    return True


def _validate_edge_file(protograph, path, log_errors=True):
    """ validate edges, return error_count """
    edge_configs = _get_properties(protograph, path, 'edges')
    expected = set(['to', 'fromLabel', 'from',
                    'gid', 'toLabel', 'label'])
    error_count = ErrorCount()
    for edge in _load_records(path):
        # check it has all the expected keys
        assert expected.issubset(set(edge.keys())), 'incomplete: {} does not contain keys {}'.format(path, expected)  # noqa
        # check all keys have data
        for k in expected:
            with _logging(path, log_errors, error_count):
                assert _exists(edge[k]), "missing '{}' in {} {}".format(k, path, edge)  # noqa
        # check the edge has a configuration
        with _logging(path, log_errors, error_count):
            assert edge.label == edge_configs[edge.label].label, "missing config for {}".format(edge.label)  # noqa
        edge_config = edge_configs[edge.label]
        # check that if data configured, the object exists
        if 'data' in edge_config:
            with _logging(path, log_errors, error_count):
                assert edge.data, 'edge should have .data {}'.format(edge)
            for k in edge_config.data.keys():
                with _logging(path, log_errors, error_count):
                    # filter out type field
                    key_fields = k.split('.')
                    k = key_fields[0]
                    _type = 'str'
                    k.split('.')[0]
                    assert _exists(edge.data[k]), "missing '{}' in {} {}".format(k, path, str(edge.data))  # noqa
    return error_count.val()


def _validate_vertex_file(protograph, path, log_errors=True):
    """ validate vertexes, return error_count """
    # graph config
    vertexes = _get_properties(protograph, path, 'vertexes')
    expected = ['gid', 'data', 'label']
    error_count = ErrorCount()
    for vertex in _load_records(path):
        # ensure expected properties
        assert vertex.keys() == expected, 'incomplete: {} does not contain keys {}'.format(path, expected)
        for k in expected:
            with _logging(path, log_errors, error_count):
                assert _exists(vertex[k]), "missing '{}' in {} {}".format(k, path, vertex)  # noqa
        # check lable ok
        with _logging(path, log_errors, error_count):
            assert vertex.label in vertexes.keys(), "vertex.label '{}' does not match yaml vertexes {}".format(vertex.label, vertexes.keys())  # noqa
        # check gid ok
        with _logging(path, log_errors, error_count):
            for gid_part in vertex.gid.split(':'):
                assert _exists(gid_part), "gid contains blanks '{}' in {}".format(vertex.gid, path)  # noqa

    return error_count.val()


def _validate_project(protograph, project, path_match=r'.*', log_errors=True):
    """ assert project data is ok """
    project_error_count = ErrorCount()
    with _logging(project, log_errors, project_error_count):
        paths = _get_paths(project)
        assert paths, 'expected paths for project {}'.format(project)
        path_match = re.compile(path_match)
        for p in paths:
            if not path_match.match(p):
                continue
            project, label, extention = _get_file_parts(p)
            with _logging(p, log_errors, project_error_count):
                error_count = 0
                node_type = 'Vertex'
                if 'Edge' in p:
                    node_type = 'Edge'
                if node_type == 'Edge':
                    error_count = _validate_edge_file(protograph, p)
                if node_type == 'Vertex':
                    error_count = _validate_vertex_file(protograph, p)
                project_error_count.increment(error_count)
    msg = json.dumps({'project_error_count': project_error_count.val(),
                      'project': project})
    logger.info(msg)
    return project_error_count.val()


# *****************
# tests
# *****************

def test_setup(protograph):
    """ assert we have protograph definitions """
    # print protograph.keys()
    # >>> ['Cohort', 'Evidence', 'ResponseCurve', 'GeneDatabase', 'Compound',
    # 'Variant', 'CNASegment', 'GeneExpression', 'Project', 'GeneFamily',
    # 'Individual', 'Exon', 'Biosample', 'CNACallSet', 'CallSet', 'Pubmed',
    # 'Gene', 'Transcript', 'GeneSynonym', 'VariantAnnotation']
    assert protograph


def test_ccle(protograph):
    """ assert ccle data is ok """
    project_error_count = _validate_project(protograph, 'ccle')
    assert project_error_count == 0


# test specific file
def test_ccle_VariantAnnotation_Edge(protograph):
    """ assert ccle data is ok """
    project_error_count = _validate_project(protograph, 'ccle', path_match=r'.*VariantAnnotation.Edge.json')  # noqa
    assert project_error_count == 0


# test specific file
def test_ccle_GeneExpression_Edge(protograph):
    """ assert ccle data is ok """
    project_error_count = _validate_project(protograph, 'ccle', path_match=r'.*GeneExpression.Edge.json')  # noqa
    assert project_error_count == 0


def test_ctdd(protograph):
    """ assert ctdd data is ok """
    project_error_count = _validate_project(protograph, 'ctdd')
    assert project_error_count == 0


def test_ensembl(protograph):
    """ assert ensembl data is ok """
    project_error_count = _validate_project(protograph, 'ensembl')
    assert project_error_count == 0


def test_go(protograph):
    """ assert go data is ok """
    project_error_count = _validate_project(protograph, 'go')
    assert project_error_count == 0


def test_mc3(protograph):
    """ assert test_mc3 data is ok """
    project_error_count = _validate_project(protograph, 'mc3')
    assert project_error_count == 0


def test_tcga(protograph):
    """ assert tcga data is ok """
    for dir_name in _get_dirs('tcga'):
        project_error_count = _validate_project(protograph,
                                                'tcga/{}'.format(dir_name))
        assert project_error_count == 0
