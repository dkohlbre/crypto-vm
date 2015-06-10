#!/usr/bin/python

import os
import sys
import stat


print "What is the ctf your problem came from? Format as ctfnameyear. Ex: plaid2014, hitcon2014, defcon2013."
ctfname = raw_input("> ").strip()
print "What is the name of the ctf problem? Format with no spaces."
probname = raw_input("> ").strip().replace(" ","_")
name = ctfname+"-"+probname

print "Creating new problem \""+name+"\""

print "What is the category of your problem? (Ex: RSA, elliptic curves, classical ciphers)"
category = raw_input("> ").strip().replace(" ","_")

print "Does your problem require a server?"
srv = ""
while 'y' != srv and 'n' != srv:
    srv = raw_input("y/n> ").strip().lower()

if srv == 'y':
    print "Is the server fully self contained? (Does it handle connections etc over sockets?) It will use init if so. Otherwise it will run under xinetd."
    init = ""
    while 'y' != init and 'n' != init:
        init = raw_input("y/n> ").strip().lower()
    print "What port will your server run on?"
    port = "x"
    while not port.isdigit():
        port = raw_input("> ").strip()


print "Building problem files....\n\n\n"

# Create the problem
os.mkdir(name)
# Create all the base markdown files
basefiles = ["hint.md","flag.txt","description.md","solution.md"]
for fname in basefiles:
    with open(name+"/"+fname,'w') as f:
        f.write("TODO")

# Create the base config
with open(name+"/config.txt",'w') as f:
    f.write("CATEGORY: "+category+"\n")
    f.write("ENABLED: TRUE\n")

# Create the setup script
bconf = open("../templates/setup.sh",'r').read()
bconf = bconf.replace("PROBLEM=REPLACE","PROBLEM=\""+name+"\"")
if srv == 'y':
    if init == 'y':
        exconf = open("../templates/init.sh",'r').read()
        os.system("cp ../templates/PROBLEM.init "+name+"/"+name+".init")
        print "Fill out "+name+"/"+name+".init with server and problem info"
        st = os.stat(name+'/'+name+".init")
        os.chmod(name+'/'+name+".init", st.st_mode | stat.S_IEXEC)

    else:
        exconf = open("../templates/xinet.sh",'r').read()
        exconf = exconf.replace("PORT=REPLACE","PORT="+port)
        os.system("cp ../templates/PROBLEM.xinetd "+name+"/"+name+".xinetd")


    print "Fill out the SERVER files to copy in the setup.sh file"
    bconf = bconf+exconf

    print "Updating the ports file!"
    with open("ports",'a') as f:
        f.write(port+"\n")

print "Fill out the PUBLIC files to copy in the setup.sh file"
with open(name+"/setup.sh",'w') as f:
    f.write(bconf)

st = os.stat(name+'/setup.sh')
os.chmod(name+'/setup.sh', st.st_mode | stat.S_IEXEC)
