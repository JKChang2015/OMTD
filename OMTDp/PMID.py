# PMID
# Created by JKChang
# 25/07/2017, 21:19
# Tag:
# Description: load abstract accoding to PMID

import urllib2
import xml.dom.minidom
import urllib
from lxml import etree

PMID = 9843981

def getCore(ID):
    url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % PMID
    html = urllib2.urlopen(url).read()
    return html



root = etree.fromstring(getCore(PMID))
print etree.tostring(root, pretty_print=True)



