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
    configtxt = open(pdir + "/config.txt", 'r').readlines()
except IOError:
    print("Unable to find some files for this problem! Bailing...")
    exit(-1)

category = ""

for l in configtxt:
    if l.startswith("ENABLED"):
        if "FALSE" in l:
            print("Problem is disabled")
            exit(1)
    if l.startswith("CATEGORY"):
        category = l.split("CATEGORY: ")[-1].strip()

basepname = sys.argv[1].split("/")[-1]
pname = basepname.replace("_", " ")

args = {'title': pname, 'desc': desc, 'hint': hint, 'solution': solution, 'flagtxt': flagtxt}
page = """
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <!-- Bootstrap -->
    <link type="text/css" rel="stylesheet" href="/css/bootstrap.min.css"/>
    <link type="text/css" rel="stylesheet" href="/css/bootstrap-theme.min.css"/>
    <link type="text/css" rel="stylesheet" href="/css/style.css" />
    <link type="text/css" rel="stylesheet" href="/css/pilcrow.css" />
    <link type="text/css" rel="stylesheet" href="/css/hljs-github.min.css"/>
    <script src="/js/jquery-2.1.1.min.js"></script>
    <script src="/js/bootstrap.min.js"></script>
</head>
<body>
    <script src="/stuff.js"></script>

    <h1 class="page-header">{title}</h1>
    <div class="well">
        {desc}
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">
          <button type="button" class="btn btn-default btn-small spoiler-trigger" data-toggle="collapse"
          onclick="javascript:{{$(this).parent().next().collapse('toggle');}}" style="font-weight: bold;">Hints</button>
        </div>
        <div class="panel-collapse collapse out">
          <div class="panel-body">
            {hint}
          </div>
        </div>
    </div>
    <hr>
    <div>
        <h2>Flag:</h2>
        <form class="form-inline" role="form">
            <input type="text" class="form-control" id="guess" placeholder="your flag" style="width: 25em;">
            <button type="button" class="btn btn-primary" onclick="flagcheck('{flagtxt}');">Submit</button>
        </form>
        <br>
        <div id="success"></div>
    </div>
    <div>
        <h2>Solution</h2>
        <button type="button" class="btn btn-primary" onclick="blocktoggle('solution');" id="showsolution" value="Show" style="margin-bottom: 1em;"/>
        <br>
        <div id=solution class="well" style=display:none>{solution}</div>
    </div>
</body>
</html>
""".format(**args)

os.system("mkdir /var/www/html/" + pname)

of = codecs.open("/var/www/html/" + pname + "/index.html", encoding='utf-8', mode='w')

of.write(page)
of.close()

print "Problem \""+pname+"\" setup complete"


# Handle category stuff
category = category.replace(" ","_")
if category == "":
    print "No category for problem \""+pname+"\", it will be in MISC."
    category = "misc"

cfile = open("tmp_cat_"+category,"a")
cfile.write(basepname+"\n")
