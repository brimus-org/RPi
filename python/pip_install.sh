#!/bin/bash
set -x

for i in `cat pip.txt`
do
	sudo pip install $i
done
