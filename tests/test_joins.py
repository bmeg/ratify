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
              _load_records, _records

logger = logging.getLogger(__name__)


# *******
# tests
# *******
def test_ensembl_Transcript_Vertex():
    """ assert ensembl data is ok """
    project_error_count = ErrorCount()
    with _logging('ensembl_Transcript_Vertex',
                  log_errors=True, error_count=project_error_count):
        # load genes and ensure no dups
        genes = []
        for gene in _records('ensembl', path_match=r'.*Gene.Vertex.json'):
            assert gene.gid not in genes
            genes.append(gene.gid)

        # load transcripts and ensure no dups
        transcripts = []
        path_match = r'.*Transcript.Vertex.json'
        for transcript in _records('ensembl', path_match=path_match):
            assert transcript.gid not in transcripts
            transcripts.append(transcript.gid)

        # load transcripts edge and ensure connection to gene and transcript
        for edge in _records('ensembl', path_match=r'.*Transcript.Edge.json'):
            # assert 'from' points to existing transcript
            msg = "transcript edge from not 'Transcript'"
            assert edge.fromLabel == 'Transcript', msg
            msg = 'transcript edge from not in vertext {}'.format(edge['from'])
            assert edge['from'] in transcripts, msg
            # assert 'to' points to existing gene
            assert edge.toLabel == 'Gene', "transcript edge to not 'Gene'"
            msg = 'transcript toGene not in gene {}'.format(edge.to)
            assert edge.to in genes, msg

    assert project_error_count.val() == 0
