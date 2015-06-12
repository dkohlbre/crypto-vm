#!/usr/bin/env python2

portlines = open("../problems/ports",'r').readlines()

ports = []

for l in portlines:
    if l[0] == "#":
        continue
    else:
        ports.append(l.strip())


print "Asking Vagrant to forward the following ports:"+str(ports)

vfile = open("base.Vagrantfile",'r')
vdata = vfile.read()
vfile.close()

portstring = ""
for port in ports:
    portstring+="cryptovm.vm.network :forwarded_port, guest: "+str(port)+", host: "+str(port)+"\n"

vdata = vdata.replace("#PORTS",portstring)
vfile = open("Vagrantfile",'w')
vfile.write(vdata)
vfile.close()
