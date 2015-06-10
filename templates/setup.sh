#!/bin/bash

PROBLEM=REPLACE

# Fill in any files that should be copied to the PUBLIC webdir
files=()

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done
