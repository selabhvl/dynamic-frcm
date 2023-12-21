#!/bin/bash

set -e

python3 fireriskmodel/test_compute.py

python3 datamodel/test_utils.py
python3 datamodel/test_datamodel.py

python3 weatherdata/test_client_met.py
python3 weatherdata/test_utils.py
python3 weatherdata/test_extractor_met.py

python3 test_frcapi.py
