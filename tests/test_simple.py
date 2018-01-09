import json
import os
import os.path
import pytest
import requests
import yaml

from os import listdir
from os.path import isfile, join
import logging

logger = logging.getLogger(__name__)


class AttributeDict(dict):
    """ enable dot notation for dicts """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__


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

    protograph_object = AttributeDict({})
    for i in protograph_list:
        p = AttributeDict(i)
        protograph_object[p.label] = p
    return protograph_object


def _get_paths(project):
    """ return any files in the path that contain name """
    p = '{}/{}'.format(os.getenv('DATA_DIR', 'biostream/protograph'), project)
    logger.debug('loading paths from {}'.format(p))
    return [join(p, f) for f in listdir(p) if isfile(join(p, f))]


def _get_file_parts(path):
    """ return tuple of file parts. e.g.
        ccle.Biosample.Vertex.json ~ (project, label, node_type, extention)
        where node_type = Vertex | Edge; extention = json
    """
    basename = os.path.basename(path)
    return basename.split('.')


def _get_properties(protograph, path, node_type):
    """ get the protograph properties for the path, ignore 0 length files """
    (project, label, node_type2, extention) = _get_file_parts(path)
    logger.debug(path)
    assert protograph[label], '{} not found in protograph'.format(path)
    properties = protograph[label]
    properties = protograph[label]
    statinfo = os.stat(path)
    if statinfo.st_size:
        assert node_type in properties, '{} not found in protograpth {}'.format(node_type, path)  # noqa
        return properties[node_type]
    else:
        return {}


def _load_records(path):
    """ load records from file, break if SAMPLE_SIZE set """
    sample_size = int(os.getenv('SAMPLE_SIZE', '-1'))
    with open(path, 'r') as ins:
        c = 0
        for line in ins:
            c += 1
            if c > sample_size and sample_size > -1:
                break
            yield AttributeDict(json.loads(line))


def _exists(val):
    """ empty test """
    if not val:
        return False
    if isinstance(val, basestring) and not val.strip():
        return False
    return True


def _validate_edge_file(protograph, path, log_errors=True):
    """ validate edges, return error_count """
    edges = _get_properties(protograph, path, 'edges')
    expected = ['to', 'fromLabel', 'from', 'data', 'gid', 'toLabel', 'label']
    error_count = 0
    for edge in _load_records(path):
        assert edge.keys() == expected, 'incomplete {}'.format(path)
        for k in expected:
            try:
                assert _exists(edge[k]), "missing '{}' in {} {}".format(k, path, edge)  # noqa
            except Exception as e:
                error_count += 1
                if log_errors:
                    msg = json.dumps({'path': path, 'error': e.message})
                    print '>>>\n{}\n<<<'.format(msg)
                    logger.error(msg)
                else:
                    raise e
    return error_count


def _validate_vertex_file(protograph, path, log_errors=True):
    """ validate vertexes, return error_count """
    vertexes = _get_properties(protograph, path, 'vertexes')
    expected = ['gid', 'data', 'label']
    error_count = 0
    for vertex in _load_records(path):
        # ensure expected properties
        assert vertex.keys() == expected, 'incomplete {}'.format(path)
        for k in expected:
            try:
                assert _exists(vertex[k]), "missing '{}' in {} {}".format(k, path, vertex)  # noqa
            except Exception as e:
                error_count += 1
                if log_errors:
                    msg = json.dumps({'path': path, 'error': e.message})
                    print '>>>\n{}\n<<<'.format(msg)
                    logger.error(msg)
                else:
                    raise e
    return error_count


def _validate_project(protograph, project):
    """ assert project data is ok """
    project_error_count = 0
    try:
        paths = _get_paths(project)
        assert paths
        for p in paths:
            project, label, node_type, extention = _get_file_parts(p)
            try:
                error_count = 0
                if node_type == 'Edge':
                    error_count = _validate_edge_file(protograph, p)
                if node_type == 'Vertex':
                    error_count = _validate_vertex_file(protograph, p)
                msg = json.dumps({'error_count': error_count, 'path': p})
                print '>>>\n{}\n<<<'.format(msg)
                logger.info(msg)
                project_error_count += error_count
            except Exception as e:
                msg = json.dumps({'project': project, 'label': label, 'node_type': node_type, 'error': e.message})  # noqa
                print '>>>\n{}\n<<<'.format(msg)
                logger.error(msg)
    except Exception as e:
        msg = json.dumps({'project': project, 'error': e.message})
        print '>>>\n{}\n<<<'.format(msg)
        logger.error(msg)
        project_error_count += 1

    msg = json.dumps({'project_error_count': project_error_count,
                      'project': project})
    print '>>>\n{}\n<<<'.format(msg)
    logger.info(msg)
    return project_error_count


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


def test_ctdd(protograph):
    """ assert ctdd data is ok """
    project_error_count = _validate_project(protograph, 'ctdd')
    assert project_error_count == 0
