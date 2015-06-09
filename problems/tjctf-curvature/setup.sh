#!/bin/bash


PROBLEM="tjctf-curvature"
files=("redacted-server.py")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done

# setup an init
cp /vagrant/problems/$PROBLEM/$PROBLEM.init /etc/init.d/$PROBLEM

# setup the service
files=("server.py")
#Copy service files over
for fname in "${files[@]}"
do
	mkdir -p /home/vagrant/problems/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /home/vagrant/problems/$PROBLEM/$fname
done

#start it
update-rc.d $PROBLEM defaults
service $PROBLEM start &
