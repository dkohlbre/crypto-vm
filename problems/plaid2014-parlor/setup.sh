#!/bin/bash

PROBLEM="plaid2014-parlor"
files=("redacted-server.py" "write-up.pdf")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done


# setup the init script
cp /vagrant/problems/$PROBLEM/$PROBLEM.init /etc/init.d/$PROBLEM

# setup the service
files=("server.py")
#Copy service files over
for fname in "${files[@]}"
do
	mkdir -p /home/vagrant/problems/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /home/vagrant/problems/$PROBLEM/$fname
done

# Start the service
update-rc.d $PROBLEM defaults
service $PROBLEM start &
