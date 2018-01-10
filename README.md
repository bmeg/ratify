# ratify, bmeg-validator

A simple test of bmeg etl output


## setup

Get the data

The environmental variable DATA_DIR needs to point to
https://exastack-00.ohsu.edu/dashboard/project/containers/container/biostream/

How you get access is up to you.  You can download the data, or mount it.

For example to map it via [The Swift Virtual File System](https://github.com/ovh/svfs)

```
# after sourcing the openstack rc file.

$ sudo ~/Downloads/svfs-darwin-amd64 mount --device CCCDEV --mountpoint $(echo ~/CCC2)  --os-auth-url $OS_AUTH_URL --os-password $OS_PASSWORD --os-username $OS_USERNAME --os-tenant-name $OS_TENANT_NAME  --default-uid $(id -u)

```

## run the tests

```
export DATA_DIR=<download/mapped dir>
export SAMPLE_SIZE=<number of records to test>
# note: DATA_DIR defaults to 'biostream/protograph'
# note: SAMPLE_SIZE default to -1 (test all records)
py.test
```

## other

The tests rely on the [yaml definitions of the graph](https://raw.githubusercontent.com/biostream/bmeg-etl/master/bmeg.protograph.yaml).

The test will download the yaml file to tests/ on first execution.


## example output

Each test will write a json formatted message to the standard python log output

```
$ DATA_DIR=~/CCC2/biostream/protograph SAMPLE_SIZE=10 pytest  -s
============================= test session starts ==============================
platform darwin -- Python 2.7.13, pytest-3.0.6, py-1.4.34, pluggy-0.4.0
rootdir: /Users/walsbr/ratify, inifile:
plugins: flask-0.8.1, catchlog-1.2.2
collected 9 items

tests/test_protograph.py .F.FFFFFF

=================================== FAILURES ===================================
__________________________________ test_ccle ___________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_ccle(protograph):
        """ assert ccle data is ok """
        project_error_count = _validate_project(protograph, 'ccle')
>       assert project_error_count == 0
E       assert 29 == 0

tests/test_protograph.py:228: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/ccle
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'biosample::', u'data': {}, u'gid': u'(biosample::)--sampleOf->()', u'toLabel': u'Individual', u'label': u'sampleOf'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'biosample::', u'data': {}, u'gid': u'(biosample::)--sampleOf->()', u'toLabel': u'Individual', u'label': u'sampleOf'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'biosample::', u'data': {}, u'gid': u'(biosample::)--sampleOf->()', u'toLabel': u'Individual', u'label': u'sampleOf'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'biosample::', u'data': {}, u'gid': u'(biosample::)--sampleOf->()', u'toLabel': u'Individual', u'label': u'sampleOf'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'biosample::', u'data': {}, u'gid': u'(biosample::)--sampleOf->()', u'toLabel': u'Individual', u'label': u'sampleOf'})\nassert False\n +  where False = _exists('')"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Biosample.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.ResponseCurve.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.Variant.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.Variant.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.VariantAnnotation.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.VariantAnnotation.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.VariantAnnotation.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.ResponseCurve.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.ResponseCurve.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.Variant.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'', u'fromLabel': u'GeneExpression', u'from': u'geneExpression::GeneExpression', u'data': {}, u'gid': u'(geneExpression::GeneExpression)--expressionFor->()', u'toLabel': u'Biosample', u'label': u'expressionFor'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000252876.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000252876.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000252876.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000252876.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000267617.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000267617.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000267617.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000267617.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000215811.3', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000215811.3', u'level': 0.106453105807304}, u'gid': u'()--expressionLevel->(gene:ENSG00000215811.3)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000215811.3', u'level': 0.106453105807304})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000238020.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000238020.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000238020.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000238020.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000231620.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000231620.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000231620.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000231620.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000075624.9', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000075624.9', u'level': 864.669738769531}, u'gid': u'()--expressionLevel->(gene:ENSG00000075624.9)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000075624.9', u'level': 864.669738769531})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000248514.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000248514.1', u'level': 1.15239310264587}, u'gid': u'()--expressionLevel->(gene:ENSG00000248514.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000248514.1', u'level': 1.15239310264587})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000117676.9', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000117676.9', u'level': 13.0834789276123}, u'gid': u'()--expressionLevel->(gene:ENSG00000117676.9)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000117676.9', u'level': 13.0834789276123})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000265778.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000265778.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000265778.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000265778.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py         207 INFO     {"project": "ccle", "project_error_count": 29}
________________________ test_ccle_GeneExpression_Edge _________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_ccle_GeneExpression_Edge(protograph):
        """ assert ccle data is ok """
        project_error_count = _validate_project(protograph, 'ccle', path_match=r'.*GeneExpression.Edge.json')  # noqa
>       assert project_error_count == 0
E       assert 19 == 0

tests/test_protograph.py:242: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/ccle
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'', u'fromLabel': u'GeneExpression', u'from': u'geneExpression::GeneExpression', u'data': {}, u'gid': u'(geneExpression::GeneExpression)--expressionFor->()', u'toLabel': u'Biosample', u'label': u'expressionFor'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000252876.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000252876.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000252876.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000252876.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000267617.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000267617.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000267617.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000267617.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000215811.3', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000215811.3', u'level': 0.106453105807304}, u'gid': u'()--expressionLevel->(gene:ENSG00000215811.3)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000215811.3', u'level': 0.106453105807304})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000238020.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000238020.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000238020.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000238020.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000231620.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000231620.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000231620.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000231620.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000075624.9', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000075624.9', u'level': 864.669738769531}, u'gid': u'()--expressionLevel->(gene:ENSG00000075624.9)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000075624.9', u'level': 864.669738769531})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000248514.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000248514.1', u'level': 1.15239310264587}, u'gid': u'()--expressionLevel->(gene:ENSG00000248514.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000248514.1', u'level': 1.15239310264587})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000117676.9', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000117676.9', u'level': 13.0834789276123}, u'gid': u'()--expressionLevel->(gene:ENSG00000117676.9)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000117676.9', u'level': 13.0834789276123})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'from' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'to': u'gene:ENSG00000265778.1', u'fromLabel': u'Biosample', u'from': u'', u'data': {u'sample': u'', u'gene': u'ENSG00000265778.1', u'level': 0.0}, u'gid': u'()--expressionLevel->(gene:ENSG00000265778.1)', u'toLabel': u'Gene', u'label': u'expressionLevel'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json", "error": "missing 'sample' in /SWIFT/biostream/protograph/ccle/ccle.GeneExpression.Edge.json AttrDict({u'sample': u'', u'gene': u'ENSG00000265778.1', u'level': 0.0})\nassert False\n +  where False = _exists('')"}
test_protograph.py         207 INFO     {"project": "ccle", "project_error_count": 19}
__________________________________ test_ctdd ___________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_ctdd(protograph):
        """ assert ctdd data is ok """
        project_error_count = _validate_project(protograph, 'ctdd')
>       assert project_error_count == 0
E       assert 11 == 0

tests/test_protograph.py:248: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/ctdd
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 0.6666666666666666, u'compound': u'pubchem:24771867'}, {u'ratio': 0.3333333333333333, u'compound': u'pubchem:24978538'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.2736}, {u'type': u'AUC', u'unit': u'uM', u'value': 7.9258}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/alisertib:navitoclax (2:1 mol/mol)', u'values': [{u'response': 0.2007, u'dose': 0.0015}, {u'response': -0.07458, u'dose': 0.003}, {u'response': -0.5947, u'dose': 0.0061}, {u'response': -0.01165, u'dose': 0.012}, {u'response': 0.03235, u'dose': 0.024}, {u'response': -0.08011, u'dose': 0.049}, {u'response': -0.6276, u'dose': 0.09699999999999999}, {u'response': -0.922, u'dose': 0.19}, {u'response': -1.266, u'dose': 0.39}, {u'response': -1.501, u'dose': 0.78}, {u'response': -1.454, u'dose': 1.6}, {u'response': -3.056, u'dose': 3.1}, {u'response': -3.397, u'dose': 6.2}, {u'response': -3.49, u'dose': 12.0}, {u'response': -3.62, u'dose': 25.0}, {u'response': -4.0280000000000005, u'dose': 50.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 0.5, u'compound': u'pubchem:24978538'}, {u'ratio': 0.5, u'compound': u'pubchem:216239'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 1.3319999999999999}, {u'type': u'AUC', u'unit': u'uM', u'value': 10.021}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/navitoclax:sorafenib (1:1 mol/mol)', u'values': [{u'response': 0.1961, u'dose': 0.0015}, {u'response': -0.0003637, u'dose': 0.003}, {u'response': 0.129, u'dose': 0.0061}, {u'response': 0.09207, u'dose': 0.012}, {u'response': -0.241, u'dose': 0.024}, {u'response': 0.1883, u'dose': 0.049}, {u'response': -0.020069999999999998, u'dose': 0.09699999999999999}, {u'response': 0.011290000000000001, u'dose': 0.19}, {u'response': -0.5448, u'dose': 0.39}, {u'response': -0.2828, u'dose': 0.78}, {u'response': -1.246, u'dose': 1.6}, {u'response': -1.827, u'dose': 3.1}, {u'response': -3.074, u'dose': 6.2}, {u'response': -2.6430000000000002, u'dose': 12.0}, {u'response': -4.47, u'dose': 25.0}, {u'response': -4.846, u'dose': 50.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 0.5, u'compound': u'pubchem:24978538'}, {u'ratio': 0.5, u'compound': u'pubchem:637858'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.9687}, {u'type': u'AUC', u'unit': u'uM', u'value': 10.331}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/navitoclax:piperlongumine (1:1 mol/mol)', u'values': [{u'response': -1.044, u'dose': 0.001}, {u'response': -0.061989999999999996, u'dose': 0.002}, {u'response': -0.0024460000000000003, u'dose': 0.0041}, {u'response': 0.08653, u'dose': 0.0081}, {u'response': -0.03174, u'dose': 0.016}, {u'response': -0.03232, u'dose': 0.032}, {u'response': 0.04825, u'dose': 0.065}, {u'response': -0.04052, u'dose': 0.13}, {u'response': -0.06175, u'dose': 0.26}, {u'response': -0.2726, u'dose': 0.52}, {u'response': -1.163, u'dose': 1.0}, {u'response': -1.6869999999999998, u'dose': 2.1}, {u'response': -3.18, u'dose': 4.2}, {u'response': -2.91, u'dose': 8.3}, {u'response': -4.0569999999999995, u'dose': 17.0}, {u'response': -3.9419999999999997, u'dose': 33.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:568763'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 4.47}, {u'type': u'AUC', u'unit': u'uM', u'value': 12.324}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/SMER-3', u'values': [{u'response': 0.04269, u'dose': 0.002}, {u'response': 0.031689999999999996, u'dose': 0.0041}, {u'response': 0.009276000000000001, u'dose': 0.0081}, {u'response': -0.008859, u'dose': 0.016}, {u'response': 0.002274, u'dose': 0.032}, {u'response': 0.1136, u'dose': 0.065}, {u'response': 0.044410000000000005, u'dose': 0.13}, {u'response': 0.009303, u'dose': 0.26}, {u'response': 0.09386, u'dose': 0.52}, {u'response': 0.06253, u'dose': 1.0}, {u'response': -0.08666, u'dose': 2.1}, {u'response': -0.9538, u'dose': 4.2}, {u'response': -2.8480000000000003, u'dose': 8.3}, {u'response': -2.8310000000000004, u'dose': 17.0}, {u'response': -0.3727, u'dose': 33.0}, {u'response': -1.217, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:119182'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.1058}, {u'type': u'AUC', u'unit': u'uM', u'value': 8.8058}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/clofarabine', u'values': [{u'response': 0.1249, u'dose': 0.002}, {u'response': 0.07028999999999999, u'dose': 0.0041}, {u'response': -0.7451, u'dose': 0.0081}, {u'response': -0.01061, u'dose': 0.016}, {u'response': -0.07529, u'dose': 0.032}, {u'response': -0.02767, u'dose': 0.065}, {u'response': -1.136, u'dose': 0.13}, {u'response': -1.787, u'dose': 0.26}, {u'response': -1.238, u'dose': 0.52}, {u'response': -1.3969999999999998, u'dose': 1.0}, {u'response': -1.357, u'dose': 2.1}, {u'response': -1.5930000000000002, u'dose': 4.2}, {u'response': -1.7819999999999998, u'dose': 8.3}, {u'response': -1.5759999999999998, u'dose': 17.0}, {u'response': -1.6369999999999998, u'dose': 33.0}, {u'response': -2.104, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 0.8, u'compound': u'pubchem:5311'}, {u'ratio': 0.2, u'compound': u'pubchem:24978538'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 1.128}, {u'type': u'AUC', u'unit': u'uM', u'value': 10.017}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/vorinostat:navitoclax (4:1 mol/mol)', u'values': [{u'response': -0.03573, u'dose': 0.001}, {u'response': -0.0399, u'dose': 0.002}, {u'response': -0.04513, u'dose': 0.0041}, {u'response': 0.031160000000000004, u'dose': 0.0081}, {u'response': -0.0524, u'dose': 0.016}, {u'response': -0.02814, u'dose': 0.032}, {u'response': -0.5619, u'dose': 0.065}, {u'response': -0.012209999999999999, u'dose': 0.13}, {u'response': -0.2488, u'dose': 0.26}, {u'response': -0.58, u'dose': 0.52}, {u'response': -0.7504, u'dose': 1.0}, {u'response': -1.485, u'dose': 2.1}, {u'response': -3.792, u'dose': 4.2}, {u'response': -4.018, u'dose': 8.3}, {u'response': -3.951, u'dose': 17.0}, {u'response': -4.104, u'dose': 33.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:49867926'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.8768}, {u'type': u'AUC', u'unit': u'uM', u'value': 13.941}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/XL765', u'values': [{u'response': 0.1919, u'dose': 0.002}, {u'response': 0.03658, u'dose': 0.0041}, {u'response': 0.07169, u'dose': 0.0081}, {u'response': 0.1118, u'dose': 0.016}, {u'response': 0.2408, u'dose': 0.032}, {u'response': -0.0533, u'dose': 0.065}, {u'response': 0.1392, u'dose': 0.13}, {u'response': 0.1842, u'dose': 0.26}, {u'response': 0.0193, u'dose': 0.52}, {u'response': -0.1525, u'dose': 1.0}, {u'response': -0.5424, u'dose': 2.1}, {u'response': 0.01891, u'dose': 4.2}, {u'response': -0.553, u'dose': 8.3}, {u'response': -0.5139, u'dose': 17.0}, {u'response': 0.00645, u'dose': 33.0}, {u'response': -0.2407, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:53301938'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 1.11}, {u'type': u'AUC', u'unit': u'uM', u'value': 16.409}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/ML258', u'values': [{u'response': 0.07468, u'dose': 0.002}, {u'response': -0.3932, u'dose': 0.0041}, {u'response': 0.1303, u'dose': 0.0081}, {u'response': 0.1859, u'dose': 0.016}, {u'response': 0.07153999999999999, u'dose': 0.032}, {u'response': 0.1737, u'dose': 0.065}, {u'response': -0.1329, u'dose': 0.13}, {u'response': 0.1472, u'dose': 0.26}, {u'response': 0.2489, u'dose': 0.52}, {u'response': 0.01346, u'dose': 1.0}, {u'response': 0.209, u'dose': 2.1}, {u'response': 0.2695, u'dose': 4.2}, {u'response': 0.1287, u'dose': 8.3}, {u'response': 0.2449, u'dose': 17.0}, {u'response': 0.2284, u'dose': 33.0}, {u'response': 0.2867, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:44241473'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.5053}, {u'type': u'AUC', u'unit': u'uM', u'value': 13.825}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/SR1001', u'values': [{u'response': 0.08559, u'dose': 0.002}, {u'response': 0.1308, u'dose': 0.0041}, {u'response': -0.4168, u'dose': 0.0081}, {u'response': 0.033710000000000004, u'dose': 0.016}, {u'response': 0.1404, u'dose': 0.032}, {u'response': 0.1775, u'dose': 0.065}, {u'response': 0.1135, u'dose': 0.13}, {u'response': 0.049530000000000005, u'dose': 0.26}, {u'response': -0.2004, u'dose': 0.52}, {u'response': -0.2995, u'dose': 1.0}, {u'response': -0.5728, u'dose': 2.1}, {u'response': -0.09107, u'dose': 4.2}, {u'response': -0.5243, u'dose': 8.3}, {u'response': -0.4473, u'dose': 17.0}, {u'response': 0.00916, u'dose': 33.0}, {u'response': -0.04193, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json", "error": "missing 'to' in /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Edge.json AttrDict({u'to': u'', u'fromLabel': u'Biosample', u'from': u'ccle:TUHR4TKB_KIDNEY', u'data': {u'responseType': u'ACTIVITY', u'compounds': [{u'ratio': 1.0, u'compound': u'pubchem:400769'}], u'_label': u'ResponseCurve', u'summary': [{u'type': u'EC50', u'unit': u'uM', u'value': 0.8052}, {u'type': u'AUC', u'unit': u'uM', u'value': 8.9512}], u'sample': u'ccle:TUHR4TKB_KIDNEY', u'gid': u'ccle-response:TUHR4TKB_KIDNEY/bardoxolone methyl', u'values': [{u'response': 0.2978, u'dose': 0.002}, {u'response': 0.0689, u'dose': 0.0041}, {u'response': 0.0071189999999999995, u'dose': 0.0081}, {u'response': -0.02263, u'dose': 0.016}, {u'response': -0.05786, u'dose': 0.032}, {u'response': 0.08782000000000001, u'dose': 0.065}, {u'response': 0.026619999999999998, u'dose': 0.13}, {u'response': -0.0394, u'dose': 0.26}, {u'response': -0.09788999999999999, u'dose': 0.52}, {u'response': -2.166, u'dose': 1.0}, {u'response': -3.537, u'dose': 2.1}, {u'response': -3.6460000000000004, u'dose': 4.2}, {u'response': -5.008, u'dose': 8.3}, {u'response': -5.471, u'dose': 17.0}, {u'response': -4.332, u'dose': 33.0}, {u'response': -5.206, u'dose': 66.0}]}, u'gid': u'(ccle:TUHR4TKB_KIDNEY)--responseTo->()', u'toLabel': u'Compound', u'label': u'responseTo'})\nassert False\n +  where False = _exists('')"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ctdd/ctdd.ResponseCurve.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         207 INFO     {"project": "ctdd", "project_error_count": 11}
_________________________________ test_ensembl _________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_ensembl(protograph):
        """ assert ensembl data is ok """
        project_error_count = _validate_project(protograph, 'ensembl')
>       assert project_error_count == 0
E       assert 3 == 0

tests/test_protograph.py:254: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/ensembl
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Exon.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Exon.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ensembl/ensembl.Exon.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Gene.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ensembl/ensembl.Gene.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Transcript.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Transcript.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/ensembl/ensembl.Transcript.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/ensembl/ensembl.Gene.Edge.json
test_protograph.py         207 INFO     {"project": "ensembl", "project_error_count": 3}
___________________________________ test_go ____________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_go(protograph):
        """ assert go data is ok """
        project_error_count = _validate_project(protograph, 'go')
>       assert project_error_count == 0
E       assert 1 == 0

tests/test_protograph.py:260: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/go
test_protograph.py          74 ERROR    {"path": "go", "error": ""}
test_protograph.py         207 INFO     {"project": "go", "project_error_count": 1}
___________________________________ test_mc3 ___________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_mc3(protograph):
        """ assert go data is ok """
        project_error_count = _validate_project(protograph, 'mc3')
>       assert project_error_count == 0
E       assert 2 == 0

tests/test_protograph.py:266: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/mc3
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/mc3/mc3.Variant.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/mc3/mc3.Variant.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/mc3/mc3.VariantAnnotation.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/mc3/mc3.VariantAnnotation.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/mc3/mc3.VariantAnnotation.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/mc3/mc3.Variant.Edge.json
test_protograph.py         207 INFO     {"project": "mc3", "project_error_count": 2}
__________________________________ test_tcga ___________________________________

protograph = AttrDict({'Cohort': AttrDict({'vertexes': [{'filter': ['hasMember'], 'merge': ...'}, 'toLabel': 'Gene', 'label': 'variantIn'}], 'label': 'VariantAnnotation'})})

    def test_tcga(protograph):
        """ assert go data is ok """
        project_error_count = _validate_project(protograph, 'tcga')
>       assert project_error_count == 0
E       assert 10 == 0

tests/test_protograph.py:272: AssertionError
------------------------------ Captured log call -------------------------------
test_protograph.py          83 DEBUG    loading paths from /SWIFT/biostream/protograph/tcga
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Biosample.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNASegment.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNASegment.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNASegment.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.GeneExpression.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.GeneExpression.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.GeneExpression.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Individual.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.Individual.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "missing 'data' in /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json AttrDict({u'gid': u'term:', u'data': {}, u'label': u'OntologyTerm'})\nassert False\n +  where False = _exists({})"}
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Biosample.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNASegment.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNASegment.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNASegment.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.GeneExpression.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.GeneExpression.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.GeneExpression.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Individual.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.Individual.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNACallSet.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNACallSet.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNACallSet.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-BRCA.CNACallSet.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-BRCA.Individual.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.Individual.Edge.json
test_protograph.py         100 DEBUG    /SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNACallSet.Vertex.json
test_protograph.py          74 ERROR    {"path": "/SWIFT/biostream/protograph/tcga/TCGA-LUAD.CNACallSet.Vertex.json", "error": "unsupported operand type(s) for +=: 'int' and 'ErrorCount'"}
test_protograph.py         207 INFO     {"project": "TCGA-LUAD", "project_error_count": 10}
===================== 7 failed, 2 passed in 17.12 seconds ======================

```
