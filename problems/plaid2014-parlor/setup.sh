#!/bin/bash

# copy the redacted server file
cp /vagrant/problems/plaid2014-parlor/public-server.py /var/www/html/plaid2014-parlor/plaid2014-parlor-redacted-server.py

# setup the init script
cp /vagrant/problems/plaid2014-parlor/plaid2014-parlor.init /etc/init.d/plaid2014-parlor

# Start the service
service plaid2014-parlor start &
