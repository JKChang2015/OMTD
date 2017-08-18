# PMID
# Created by JKChang
# 25/07/2017, 21:19
# Tag:
# Description: load abstract accoding to PMID

import urllib.request, urllib.error, urllib.parse
import xml.dom.minidom

from lxml import etree

PMID = 9843981

def getCore(ID):
    url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % PMID
    html = urllib.request.urlopen(url).read()
    return html



root = etree.fromstring(getCore(PMID))
print(etree.tostring(root, pretty_print=True))


import sys, locale, os
print(sys.stdout.encoding)
print(sys.stdout.isatty())
print(locale.getpreferredencoding())
print(sys.getfilesystemencoding())
print(os.environ["PYTHONIOENCODING"])
print(chr(246), chr(9786), chr(9787))