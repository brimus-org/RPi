#!/bin/bash
set -x

for i in `cat AF.txt`
do
	git clone $i
done

for i in `ls | grep Adafruit`
do
        echo $i
        cd $i || exit 1
        git pull
        sudo python setup.py install
        sudo python3 setup.py install
        cd ..
done

