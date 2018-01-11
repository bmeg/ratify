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

# our generated code
import tests.generated.ga4gh
import tests.generated.bmeg
sys.modules['ga4gh'] = sys.modules['tests.generated.ga4gh']  # noqa
sys.modules['bmeg'] = sys.modules['tests.generated.bmeg']  # noqa

from tests.generated.bmeg.clinical_pb2 import *
from tests.generated.bmeg.cna_pb2 import *
from tests.generated.bmeg.genome_pb2 import *
from tests.generated.bmeg.nlp_pb2 import *
from tests.generated.bmeg.pfam_pb2 import *
from tests.generated.bmeg.phenotype_pb2 import *
from tests.generated.bmeg.rna_pb2 import *


from tests.generated.ga4gh.allele_annotations_pb2 import *
from tests.generated.ga4gh.bio_metadata_pb2 import *
from tests.generated.ga4gh.common_pb2 import *
from tests.generated.ga4gh.genotype_phenotype_pb2 import *
from tests.generated.ga4gh.metadata_pb2 import *
from tests.generated.ga4gh.reads_pb2 import *
from tests.generated.ga4gh.references_pb2 import *
from tests.generated.ga4gh.rna_quantification_pb2 import *
from tests.generated.ga4gh.sequence_annotations_pb2 import *
from tests.generated.ga4gh.variants_pb2 import *

# our common code
from . import _get_paths, _get_file_parts, _logging, _load_lines, ErrorCount

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
        assert len(paths) > 0
        for path in paths:
            # get class name from file
            cls = _get_file_parts(path)[-2]
            error_count = ErrorCount()
            for line in _load_lines(path):
                with _logging(path, log_errors, error_count):
                    # use eval to create object
                    try:
                        pb_obj = eval('{}()'.format(cls))
                        o = json_format.Parse(line, pb_obj,
                                              ignore_unknown_fields=False)
                    except Exception as e:
                        raise ValueError(
                            "pb parse e:{} cls:{} {}".format(e.message,
                                                             cls, line)
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
    """ assert go data is ok """
    project_error_count = _validate_project('mc3')
    assert project_error_count == 0


def test_tcga():
    """ assert go data is ok """
    project_error_count = _validate_project('tcga')
    assert project_error_count == 0
