#!/usr/bin/env bash
set -euxo pipefail

pytest --mypy

rm -rf dist
pipenv lock -r | egrep -v '^-i http' > requirements.txt
python setup.py clean --all
python setup.py bdist_wheel
