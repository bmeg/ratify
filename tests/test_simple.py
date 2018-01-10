import json
import logging
import os
import os.path
import pytest
import re
import requests
import yaml

from os import listdir
from os.path import isfile, join
from attrdict import AttrDict


logger = logging.getLogger(__name__)


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
    """ get the protograph properties for the path, ignore 0 length files,
        indexed by label """
    (project, label, node_type_ignore, extention) = _get_file_parts(path)
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


def _load_records(path):
    """ load records from file, break if SAMPLE_SIZE set """
    sample_size = int(os.getenv('SAMPLE_SIZE', '-1'))
    with open(path, 'r') as ins:
        c = 0
        for line in ins:
            c += 1
            if c > sample_size and sample_size > -1:
                break
            yield AttrDict(json.loads(line))


def _exists(val):
    """ empty test """
    if isinstance(val, basestring) and not val.strip():
        return False
    if isinstance(val, (float, int, long)):
        return True  # 0.0 numbers ok
    if not val:
        return False
    return True


def _log_exception(path, log_errors, e):
    """ common logging """
    if log_errors:
        msg = json.dumps({'path': path, 'error': e.message})
        print '>>>\n{}\n<<<'.format(msg)
        logger.error(msg)
        # logger.exception(e)
    else:
        raise e


def _validate_edge_file(protograph, path, log_errors=True):
    """ validate edges, return error_count """
    edge_configs = _get_properties(protograph, path, 'edges')
    expected = set(['to', 'fromLabel', 'from',
                    'gid', 'toLabel', 'label'])
    error_count = 0
    for edge in _load_records(path):
        # check it has all the expected keys
        assert expected.issubset(set(edge.keys())), 'incomplete {}'.format(path)  # noqa
        # check all keys have data
        for k in expected:
            try:
                assert _exists(edge[k]), "missing '{}' in {} {}".format(k, path, edge)  # noqa
            except Exception as e:
                error_count += 1
                _log_exception(path, log_errors, e)
        # check the edge has a configuration
        try:
            assert edge.label == edge_configs[edge.label].label, "missing config for {}".format(edge.label)  # noqa
        except Exception as e:
            error_count += 1
            _log_exception(path, log_errors, e)
        edge_config = edge_configs[edge.label]
        # check that if data configured, the object exists
        if 'data' in edge_config:
            try:
                assert edge.data, 'edge should have .data {}'.format(edge)
            except Exception as e:
                error_count += 1
                _log_exception(path, log_errors, e)
            for k in edge_config.data.keys():
                try:
                    # filter out type field
                    key_fields = k.split('.')
                    k = key_fields[0]
                    _type = 'str'
                    k.split('.')[0]
                    assert _exists(edge.data[k]), "missing '{}' in {} {}".format(k, path, str(edge.data))  # noqa
                except Exception as e:
                    print e
                    error_count += 1
                    _log_exception(path, log_errors, e)
    return error_count


def _validate_vertex_file(protograph, path, log_errors=True):
    """ validate vertexes, return error_count """
    # graph config
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
                _log_exception(path, log_errors, e)
    return error_count


def _validate_project(protograph, project, path_match=r'.*'):
    """ assert project data is ok """
    project_error_count = 0
    try:
        paths = _get_paths(project)
        assert paths
        path_match = re.compile(path_match)
        for p in paths:
            if not path_match.match(p):
                continue
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
                msg = json.dumps({'project': project, 'label': label,
                                  'node_type': node_type, 'error': e.message})
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


def test_ccle_VariantAnnotation_Edge(protograph):
    """ assert ccle data is ok """
    project_error_count = _validate_project(protograph, 'ccle', path_match=r'.*VariantAnnotation.Edge.json')  # noqa
    assert project_error_count == 0


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
