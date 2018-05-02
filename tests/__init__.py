#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import logging
import os
import re

from contextlib import contextmanager
from os import listdir
from os.path import isfile, join, isdir
from attrdict import AttrDict

logger = logging.getLogger(__package__)

assert os.getenv('DATA_DIR'), \
    'Please set DATA_DIR env var (points to "biostream")'


class ErrorCount(dict):
    """ simple stateful counter"""
    def __init__(self):
        self['count'] = 0

    def increment(self, val=1):
        self['count'] += val

    def val(self):
        return self['count']


@contextmanager
def _logging(path, log_errors, error_count):
    """ run code, log exception, return incremented error_count """
    try:
        yield
    except Exception as e:
        error_count.increment()
        _log_exception(path, log_errors, e)


def _log_exception(path, log_errors, e):
    """ common logging """
    if log_errors:
        msg = json.dumps({'path': path, 'error_type': e.__class__.__name__,
                         'error': e.message})
        # print '>>>\n{}\n<<<'.format(msg)
        logger.error(msg)
        logger.exception(e)
    else:
        raise e


def _get_paths(project, prefix='biostream/protograph'):
    """ return any files in the path that contain name """
    p = '{}/{}/{}'.format(os.getenv('DATA_DIR'), prefix, project)
    logger.debug('loading paths from {}'.format(p))
    return [join(p, f) for f in listdir(p) if isfile(join(p, f))]


def _get_dirs(project, prefix='biostream/protograph'):
    """ return any dirs in the path (simple dir name)"""
    p = '{}/{}/{}'.format(os.getenv('DATA_DIR'), prefix, project)
    logger.debug('loading paths from {}'.format(p))
    return [f for f in listdir(p) if isdir(join(p, f))]


def _get_file_parts(path):
    """ return tuple of file parts. e.g.
        ccle.Biosample.Vertex.json ~ (project, label, extention)
        Works from R->L so left keys are concatenated for project:
        "tcga.TCGA-BRCA.DrugTherapyjson" ~ project = "tcga.TCGA-BRCA"
        Note: we no longer support node_type
        e.g. Vertex|Edge "tcga.TCGA-BRCA.DrugTherapy.Vertex.json"
    """
    basename = os.path.basename(path)
    file_parts = basename.split('.')
    extention = file_parts[-1]
    project = None
    if len(file_parts) == 3:
        project = '.'.join(file_parts[:len(file_parts)-2])
        label = file_parts[-2]
    else:
        project = '.'.join(file_parts[:len(file_parts)-3])
        label = file_parts[-2]
        if label in ['Vertex', 'Edge']:
            label = file_parts[-3]
    return [project, label, extention]


def _load_lines(path):
    """ load plain text records from file, break if SAMPLE_SIZE set """
    sample_size = int(os.getenv('SAMPLE_SIZE', '-1'))
    with open(path, 'r') as ins:
        c = 0
        for line in ins:
            c += 1
            if c > sample_size and sample_size > -1:
                break
            yield line


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


def _records(project, path_match=r'.*', log_errors=True):
    """ get records from all files that match path """
    paths = _get_paths(project)
    assert paths
    path_match = re.compile(path_match)
    for path in paths:
        if not path_match.match(path):
            continue
        for record in _load_records(path):
            yield record
