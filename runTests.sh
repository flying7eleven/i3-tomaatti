#!/bin/bash
PYTHONPATH=`pwd`:`pwd`/tomaatti:$PYTHONPATH
echo "PYTHONPATH: $PYTHONPATH"
#python3 -m unittest discover -s ./tests -v -p '*.py'
python3 setup.py test
