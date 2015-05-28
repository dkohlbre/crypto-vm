#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install python2.7 -y

#todo run setup.sh for every /vagrant/problems/$foo/setup.sh
