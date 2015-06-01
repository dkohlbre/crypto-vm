#!/bin/bash
# check that they have python, vbox and vagrant
if ! hash python 2>/dev/null; then
    echo "You need to install python! (\"sudo apt-get install python2.7\" or similar)"
    exit -1
fi
if ! hash VirtualBox 2>/dev/null; then
    echo "You need to install VirtualBox! (\"sudo apt-get install virtualbox\" or similar)"
    exit -1
fi
if ! hash vagrant 2>/dev/null; then
    echo "You need to install vagrant! (\"sudo apt-get install vagrant\" or similar)"
    exit -1
fi


# TODO get port info!


# Run the vagrant script!
cd vm
vagrant up
