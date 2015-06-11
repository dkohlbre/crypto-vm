#!/bin/bash

PROBLEM="ASISquals2015-cross-check"
files=("all.txt" "cross_check.py" "write-up.pdf")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done