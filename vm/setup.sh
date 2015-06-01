#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install python2.7 -y
apt-get install markdown -y
apt-get install python-pip -y

pip install markdown

# Setup the webdir
mkdir /var/www/html/files

# Copy the js
cp -r /vagrant/interface/* /var/www/html/

# For each problem do some things
for d in `find /vagrant/problems/ -type d`; do
echo "Running $d setup"
$d/setup.sh && /vagrant/vm/generate_page.py $d
done
