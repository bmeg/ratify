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
