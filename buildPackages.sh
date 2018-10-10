#!/bin/bash
pip3 install -r requirements.txt
rm -rf dist/
python3 setup.py sdist bdist_egg bdist_wheel
for filename in dist/*; do
	twine upload $filename
done
