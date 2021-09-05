#!/bin/bash

mkdir -p ./dist
rm -rf ./dist/*
python setup.py bdist_wheel
pip install `find dist -iname "zet*"`
