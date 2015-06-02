#!/bin/bash


PROBLEM="tjctf-curvature"
files=("redacted-server.py")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
a	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done

# setup an init
cp /vagrant/problems/$PROBLEM/$PROBLEM.init /etc/init.d/$PROBLEM

#start it
service $PROBLEM start &
