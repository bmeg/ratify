#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import logging
import os

from contextlib import contextmanager
from os import listdir
from os.path import isfile, join

logger = logging.getLogger(__package__)


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
        msg = json.dumps({'path': path, 'error': e.message})
        # print '>>>\n{}\n<<<'.format(msg)
        logger.error(msg)
        # logger.exception(e)
    else:
        raise e


def _get_paths(project, prefix='biostream/protograph'):
    """ return any files in the path that contain name """
    p = '{}/{}/{}'.format(os.getenv('DATA_DIR'), prefix, project)
    logger.debug('loading paths from {}'.format(p))
    return [join(p, f) for f in listdir(p) if isfile(join(p, f))]


def _get_file_parts(path):
    """ return tuple of file parts. e.g.
        ccle.Biosample.Vertex.json ~ (project, label, node_type, extention)
        where node_type = Vertex | Edge; extention = json
    """
    basename = os.path.basename(path)
    return basename.split('.')


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
