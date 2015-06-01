#!/bin/bash

# Are we turning off?
if [ $# -eq 1 ]; then
    if [ $1 == "off" ]; then
        cd vm
        vagrant halt
        echo -e "\n\nJust run \"runme.sh\" to restart the vm!"
        exit 0
    fi
fi
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


# Setup ports
cd vm
./ports.py


# Run the vagrant script!
vagrant up

# Now update the user!
if  [ ! $? == 0 ]; then
echo -e "\n\n\nSomething may have gone wrong with the VM setup, you can try running the problems, or read the vagrant output above."
fi
echo -e "\n\n\nAll setup! Go to a webbrowser on this machine and visit \"localhost:8082\"\nTo turn off the VM when done do \"runme.sh off\"."
