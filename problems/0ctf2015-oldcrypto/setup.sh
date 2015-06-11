#!/bin/bash

PROBLEM="0ctf2015-oldcrypto"
files=("ciphertext" "oldcrypto.py" "write-up.pdf")

# Just copy the data file to the webdir
for fname in "${files[@]}"
do
#	mkdir -p /var/www/html/$PROBLEM
	cp /vagrant/problems/$PROBLEM/$fname /var/www/html/$PROBLEM/$PROBLEM\_$fname
done