#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install python2.7 -y

# Run every problem setup file
for i in /vagrant/problems/*/setup.sh; do
$i
done
