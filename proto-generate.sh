mkdir tests/generated
protoc -I=proto   --python_out=tests/generated proto/ga4gh/*.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/clinical.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/cna.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/genome.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/nlp.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/pfam.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/phenotype.proto
protoc -I=proto   --python_out=tests/generated proto/bmeg/rna.proto
touch tests/generated/__init__.py

cat >tests/generated/ga4gh/__init__.py <<EOL
import os, glob

modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(f)[:-3] for f in modules if not f.endswith("__init__.py")]
EOL


cat >tests/generated/bmeg/__init__.py <<EOL
import os, glob

modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [os.path.basename(f)[:-3] for f in modules if not f.endswith("__init__.py")]
EOL
