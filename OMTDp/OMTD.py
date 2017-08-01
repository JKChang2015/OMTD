# OMTD
# Created by JKChang
# 27/07/2017, 15:19
# Tag:
# Description: API basic function

import urllib.request, urllib.error, urllib.parse
from lxml import etree

from lxml.html.soupparser import fromstring
from lxml.etree import tostring
from xml.dom.minidom import parseString

class searcher():
    xml = ''
    result = []

    def searching(self, keyword):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s' % keyword
        print(url)
        self.xml = urllib.request.urlopen(url).read()
        return self.xml

    def getSearchResult(self):

        return self.result

def XMLPretty(string):
        root = etree.fromstring(string)
        return etree.tostring(root, pretty_print=True)


k = 'paracetamol'
s = searcher()
xml = s.searching(k)
print(XMLPretty(xml))
