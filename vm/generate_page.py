#!/usr/bin/python

import markdown
import os
import sys



pdir = sys.argv[1]

try:
    desc = markdown.markdown(open(pdir+"/description.md",'r').read())
    hint = markdown.markdown(open(pdir+"/hint.md",'r').read())
    solution = markdown.markdown(open(pdir+"/solution.md",'r').read())
    flagtxt = open(pdir+"/flag.txt",'r').read().strip()
except IOError:
    print "Unable to find some files for this problem! Bailing..."

pname = sys.argv[1].split("/")[-1].replace("_"," ")

page = "<html><head><title>"+pname+"</title>\n</head>\n<body>\n<script src=\"/stuff.js\"></script>"
page+=""+desc+"<br>"
page+="Hint <input type=\"button\" onclick=\"javascript:blocktoggle('hint');\" id=\"showhint\" value=\"Show\"/><br><div id=hint style=display:none>"+hint+"</div>"
page+="Solution <input type=\"button\" onclick=\"blocktoggle('solution');\" id=\"showsolution\" value=\"Show\"/><br><div id=solution style=display:none>"+solution+"</div>"

page+="Flag: <input id=\"guess\"/><br/>\n<input type=\"button\" onclick=\"flagcheck('"+flagtxt+"');\" value=\"Submit\"/><div id=\"success\"></div><br/>"

page += "</body></html>"

os.system("mkdir /var/www/html/"+pname)

of = open("/var/www/html/"+pname+"/index.html",'w')

of.write(page)
of.close()

print "Problem setup complete"
