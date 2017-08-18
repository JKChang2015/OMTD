# tt
# Created by JKChang
# 26/07/2017, 14:31
# Tag:
# Description: function test

import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom

id = 9843981
url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%s&resulttype=core' % id
print(url)
core_str = urllib.request.urlopen(url).read().decode('utf-8')
rr = []
root = ET.fromstring(core_str)

for results in root.iter('result'):
    for res in results.findall('title'):
        rr.append(res.text)

print(rr)









