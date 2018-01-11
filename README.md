# ratify a validator for bmeg

Tests:
* protocolbuffer conformance for files in `biostream/biostream`
* protograph conformance for files in `biostream/protograph`
* graph "join" simulation for files in `biostream/protograph`


## setup

Get the data

The environmental variable DATA_DIR needs to point to
https://exastack-00.ohsu.edu/dashboard/project/containers/container/biostream/

How you get access is up to you.  You can download the data, or mount it.

For example to map it via [The Swift Virtual File System](https://github.com/ovh/svfs)

```
# after sourcing the openstack rc file.

$ sudo ~/Downloads/svfs-darwin-amd64 mount --device CCCDEV --mountpoint /tmp/SWIFT  --os-auth-url $OS_AUTH_URL --os-password $OS_PASSWORD --os-username $OS_USERNAME --os-tenant-name $OS_TENANT_NAME  --default-uid $(id -u)

```

You will need to run:
```
pip install -r requirements.txt
```

Please verify protoc installed:
```
$ protoc --version
libprotoc 3.0.0
# Use proto-generate.sh to generate the python code
$ ./proto-generate.sh
$ ls -1 tests/generated
__init__.py
bmeg
ga4gh
```



## run the tests

```
# note: DATA_DIR should be set to the mountpoint for biostream
# note: SAMPLE_SIZE default to -1 (test all records)
$ DATA_DIR=<download/mapped dir> SAMPLE_SIZE=<number of records to test> py.test
```

## test description

### protograph conformance

The tests rely on the [yaml definitions of the graph](https://raw.githubusercontent.com/biostream/bmeg-etl/master/bmeg.protograph.yaml).
The test will download the yaml file to tests/ on first execution.
The tests will interrogate each file in the directory and compare it against the protograph definition.

Current checks include:
* vertex: ensure ['gid', 'data', 'label'] are ! empty
* vertex: ensure ['gid'] component fields e.g. "A:B:C" are not empty
* edge: ensure ['to', 'fromLabel', 'from', 'gid', 'toLabel', 'label'] are ! empty.  Ensure that `data` obj has specified fields and are not empty


### biostreams

The tests rely on protocol buffer definitions and python generated code.
**NOTE:** The proto files are manually committed to this repo.  Please update them.
Use `proto-generate.sh` to generate the python code

Current checks include:
* load json into proto object with ignore_unknown_fields=False


### graph joins

The biostreams and protograph tests parse schemas and dynamically interrogate known 'project' folders to validate data.
The `test_joins` tests are manually setup and follow the following form:

* for a known project
  * for a known edge
    * read to / from vertexes
    * validate edge to and from gids exist

You may not want to set SAMPLE_SIZE in order to read all records.
Currently the test validates `ensembl Transcript Vertex`

## example output

Each test will write a json formatted message to the standard python log output

### protograph

[DATA_DIR=/tmp/SWIFT  SAMPLE_SIZE=10 pytest  -s tests/test_protograph.py](https://github.com/biostream/bmeg-etl/issues/55)

### biostream

[DATA_DIR=/tmp/SWIFT  SAMPLE_SIZE=10 pytest  -s tests/test_biostream.py](https://github.com/biostream/bmeg-etl/issues/56)

## joins

[DATA_DIR=/tmp/SWIFT  pytest  -s tests/test_joins.py](https://github.com/biostream/bmeg-etl/issues/57)
