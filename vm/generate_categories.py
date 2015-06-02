#!/usr/bin/env python2
from __future__ import unicode_literals
import markdown
import os
import sys
import codecs

categories = []

#find the categories
for p,dirs,files in os.walk("."):
    for f in files:
        if f.startswith("tmp_cat_"):
            categories.append(f.replace("tmp_cat_","").strip())
    break


# build each category
for cat in categories:
    cfile = open("/var/www/html/"+cat+".html",'w')
    cdata = open("tmp_cat_"+cat,'r').readlines()
    plist = ''.join(["<a href=\"/"+p.strip()+"/index.html\">"+p.replace("_"," ").strip()+"</a></br>\n" for p in cdata])
    # for now whatever
    args = {'title': cat, 'plist': plist}
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
{plist}
</body>
</html>""".format(**args)
    cfile.write(page)
    cfile.close()


# todo build category listing page
