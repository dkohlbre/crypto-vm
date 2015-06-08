#!/bin/bash

PROBLEM="hitcon2014-rsaha"
files=("server.py")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done

#TODO setup xinetd server
