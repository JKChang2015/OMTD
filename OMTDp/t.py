# -*- coding: utf-8 -*-
# t
# Created by JKChang
# 27/07/2017, 20:26
# Tag:
# Description: 

import urllib.request, urllib.parse, urllib.error
from lxml import etree

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

id = 9843981
url = r'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % id
print(url)

xml_str = urllib.request.urlopen(url).read().decode("utf8")
root = etree.fromstring(xml_str)
print(etree.tostring(root, pretty_print=True))

# xml_str = urllib.request.urlopen(url).read()
#
# content = ET.fromstring(xml_str)
# print(content)
#
#
# abs = content.find('abstractText')
#
# print(abs)

# root = etree.fromstring(xml_str)
# print etree.tostring(root,pretty_print= True)

# soup = BeautifulStoneSoup(s)
# inputTags = soup.findAll(attrs='abstractText')
#
# output = [x['abstractText'] for x in inputTags]
#
# print output
