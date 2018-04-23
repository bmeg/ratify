#!/usr/bin/python
# -*- encoding: utf-8 -*-

import json
import logging
import inspect
import os
import os.path
import pkgutil
import pytest
import re
import requests
import sys
import yaml

from attrdict import AttrDict
from contextlib import contextmanager
from os import listdir
from os.path import isfile, join
from google.protobuf import json_format

# biostream-schema
from bmeg.clinical_pb2 import *
from bmeg.cna_pb2 import *
from bmeg.genome_pb2 import *
# from bmeg.nlp_pb2 import *
# from bmeg.pfam_pb2 import *
from bmeg.phenotype_pb2 import *
from bmeg.rna_pb2 import *
from bmeg.variants_pb2 import *

# our common code
from . import _get_paths, _get_file_parts, _logging, _load_lines, ErrorCount, \
    _get_dirs, _load_records

logger = logging.getLogger(__name__)


# *******
# utilities
# *******
def _validate_project(project):
    project_error_count = ErrorCount()
    log_errors = True
    path = 'biostream/biostream/{}'.format(project)
    with _logging(path, log_errors, project_error_count):
        paths = _get_paths(project, prefix='biostream/biostream')
        assert len(paths) > 0, 'expected paths for {}'.format(project)
        for path in paths:
            # get class name from file
            print path
            print _get_file_parts(path)
            cls = _get_file_parts(path)[-3]
            error_count = ErrorCount()
            with _logging(path, log_errors, error_count):
                for line in _load_lines(path):
                    # use eval to create object
                    try:
                        pb_obj = eval('{}()'.format(cls))
                        o = json_format.Parse(line, pb_obj,
                                              ignore_unknown_fields=False)
                    except Exception as e:
                        raise ValueError(
                            "pb parse e:{} cls:{} path:{} line:{}".format(
                                e.message, cls, path, line)
                        )
            project_error_count.increment(error_count.val())
    return project_error_count.val()


# *******
# tests
# *******
def test_ccle():
    """ assert ccle data is ok """
    project_error_count = _validate_project('ccle')
    assert project_error_count == 0


def test_ctdd():
    """ assert ctdd data is ok """
    project_error_count = _validate_project('ctdd')
    assert project_error_count == 0


def test_ensembl():
    """ assert ensembl data is ok """
    project_error_count = _validate_project('ensembl')
    assert project_error_count == 0


def test_go():
    """ assert go data is ok """
    project_error_count = _validate_project('go')
    assert project_error_count == 0


def test_mc3():
    """ assert mc3 data is ok """
    project_error_count = _validate_project('mc3')
    assert project_error_count == 0


def test_tcga():
    """ assert tcga data is ok """
    for dir_name in _get_dirs('tcga'):
        project_error_count = _validate_project('tcga/{}'.format(dir_name))
        assert project_error_count == 0


def test_g2p():
    """ assert g2p data is ok """
    project_error_count = _validate_project('g2p')
    assert project_error_count == 0


def test_g2p_variants():
    """ assert g2p variants is ok """
    paths = _get_paths('g2p', prefix='biostream/biostream')
    features_path = None
    for p in paths:
        if p.endswith('Variant.json'):
            features_path = p
    ref_alt_count = 0
    for f in _load_records(features_path):
        if 'referenceBases' in f or 'alternateBases' in f:
            ref_alt_count += 1
    assert ref_alt_count > 0, 'expected some features w/ ref or alt'
