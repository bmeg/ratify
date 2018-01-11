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

# our common code
from . import _get_paths, _get_file_parts, _logging, _load_lines, ErrorCount, \
              _load_records

logger = logging.getLogger(__name__)


# *******
# utilities
# *******
def _records(project, path_match=r'.*', log_errors=True):
    """ get records """
    paths = _get_paths(project)
    assert paths
    path_match = re.compile(path_match)
    for path in paths:
        if not path_match.match(path):
            continue
        for record in _load_records(path):
            yield record


# *******
# tests
# *******
def test_ccle_Biosample_Edge():
    """ assert ccle data is ok """
    project_error_count = ErrorCount()
    for variant in _records('ccle', path_match=r'.*Variant.Vertex.json'):  # noqa
        print variant # variant.gid, variant.data.id
    assert project_error_count == 0
