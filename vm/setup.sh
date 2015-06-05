#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install python2.7 -y
apt-get install markdown -y
apt-get install python-pip -y

pip install markdown

# Copy the js
cp -r /vagrant/interface/* /var/www/html/

# For each problem do some things
for d in `find /vagrant/problems/ -type d`; do
echo "Running $d setup"
/vagrant/vm/generate_page.py $d && $d/setup.sh
done

#generate the overpages
/vagrant/vm/generate_categories.py
