#!/usr/bin/env python2
from __future__ import unicode_literals
import markdown
import os
import sys
import codecs



pdir = sys.argv[1]

try:
    desc = markdown.markdown(codecs.open(pdir + "/description.md", encoding='utf-8', mode='r').read())
    hint = markdown.markdown(codecs.open(pdir + "/hint.md", encoding='utf-8', mode='r').read())
    solution = markdown.markdown(codecs.open(pdir + "/solution.md", encoding='utf-8', mode='r').read())
    flagtxt = open(pdir + "/flag.txt", 'r').read().strip()
except IOError:
    print("Unable to find some files for this problem! Bailing...")
    exit(-1)

pname = sys.argv[1].split("/")[-1].replace("_", " ")

args = {'title': pname, 'desc': desc, 'hint': hint, 'solution': solution, 'flagtxt': flagtxt}
page = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link type="text/css" rel="stylesheet" href="/css/style.css" />
    <link type="text/css" rel="stylesheet" href="/css/pilcrow.css" />
    <link type="text/css" rel="stylesheet" href="/css/hljs-github.min.css"/>
</head>
<body>
    <script src="/stuff.js"></script>
<h1>{title}</h1>
{desc}<br>
Hint <input type="button" onclick="javascript:blocktoggle('hint');" id="showhint" value="Show"/><br>
<div id=hint style=display:none>{hint}</div>
Flag: <input id="guess"/><br/>\n<input type="button" onclick="flagcheck('{flagtxt}');" value="Submit"/><div id="success"></div><br/>
Solution <input type="button" onclick="blocktoggle('solution');" id="showsolution" value="Show"/><br>
<div id=solution style=display:none>{solution}</div>
</body>
</html>
""".format(**args)

os.system("mkdir /var/www/html/" + pname)

of = codecs.open("/var/www/html/" + pname + "/index.html", encoding='utf-8', mode='w')

of.write(page)
of.close()

print("Problem setup complete")
