#!/bin/bash
PYTHONPATH=`pwd`:$PYTHONPATH
echo "PYTHONPATH: $PYTHONPATH"
python3 -m unittest discover -s ./tests -v -p '*.py'
