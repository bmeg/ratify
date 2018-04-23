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


def test_g2p_keys():
    """ assert g2p data keys are ok """
    genes = []
    features = []
    associations = []
    environments = []
    phenotypes = []
    paths = _get_paths('g2p', prefix='biostream/biostream')
    genes_path = None
    features_path = None
    associations_path = None
    environments_path = None
    phenotypes_path = None
    for p in paths:
        if p.endswith('Gene.json'):
            genes_path = p
        if p.endswith('Variant.json'):
            features_path = p
        if p.endswith('G2PAssociation.json'):
            associations_path = p
        if p.endswith('Compound.json'):
            environments_path = p
        if p.endswith('Phenotype.json'):
            phenotypes_path = p
    sys.stderr.write('\n*** checking g2p json files, this may take awhile.\n')
    for gene in _load_records(genes_path):
        assert gene.id not in genes
        genes.append(gene.id)
    # print 'no gene dups'
    for feature in _load_records(features_path):
        assert feature.id not in features
        features.append(feature.id)
    # print 'no feature dups'
    for environment in _load_records(environments_path):
        assert environment.id not in environments
        environments.append(environment.id)
    # print 'no environments dups'
    for phenotype in _load_records(phenotypes_path):
        assert phenotype.id not in phenotypes
        phenotypes.append(phenotype.id)
    # print 'no phenotypes dups'

    for association in _load_records(associations_path):
        assert association.id not in association
        associations.append(association.id)
        if 'features' in association:
            for feature_id in association.features:
                assert feature_id in features
        if 'genes' in association:
            for gene_id in association.genes:
                assert gene_id in genes
        if 'environments' in association:
            for environment_id in association.environments:
                assert environment_id in environments
        if 'phenotypes' in association:
            for phenotype_id in association.phenotypes:
                assert phenotype_id in phenotypes

    print 'association:no dups genes/features/environments/phenotypes found.'
