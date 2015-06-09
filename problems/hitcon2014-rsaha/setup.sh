#!/bin/bash

PROBLEM="hitcon2014-rsaha"
files=("redacted_server.py")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done


# we need sympy
pip install sympy

#setup xinetd server
cp /vagrant/problems/$PROBLEM/$PROBLEM.xinetd /etc/xinetd.d/$PROBLEM
echo -e "\n$PROBLEM 5454/tcp\n" >> /etc/services

# setup the service
files=("server.py")
#Copy service files over
for fname in "${files[@]}"
do
	mkdir -p /home/vagrant/problems/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /home/vagrant/problems/$PROBLEM/$fname
done

service xinetd restart
