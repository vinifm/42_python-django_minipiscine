#!/bin/sh

pip3 -V
if pip install git+https://github.com/jaraco/path.git --target local_lib --upgrade >> install.log; then
	python3 my_program.py
fi
