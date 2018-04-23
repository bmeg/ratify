FROM python:2.7
COPY . .
RUN pip install -r requirements.txt
CMD DATA_DIR=$DATA_DIR SAMPLE_SIZE=$SAMPLE_SIZE pytest  tests/test_biostream.py; \
    DATA_DIR=$DATA_DIR SAMPLE_SIZE=$SAMPLE_SIZE pytest  tests/test_protograph.py; \
    DATA_DIR=$DATA_DIR SAMPLE_SIZE=$SAMPLE_SIZE pytest  tests/test_joins.py;
