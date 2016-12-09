#!/bin/bash
set -x

#for i in `cat AF.txt`
#do
#	git clone $i
#done

#for i in `ls | grep Adafruit`
for i in `find . -maxdepth 1 -type d`
do
        echo $i
	if [ "$i" = "." ]
	then
		echo "skipping \".\""
	else
	        cd $i || exit 1
	        git pull
		if [ -f setup.py ]
		then
        		sudo python setup.py install
		fi
#        sudo python3 setup.py install
	        cd ..
	fi
done

