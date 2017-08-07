# example
# Created by JKChang
# 03/08/2017, 11:13
# Tag:
# Description: 

import xml.etree.ElementTree as ET
from Extractor import XMLExtractor
from lxml import etree

stri = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

extract = XMLExtractor()
res = extract.extract(stri, 'neighbor')
for x in res:
    print(x)

    # tree = ET.parse('country_data.xml')
    # root = tree.getroot()

    # root = ET.fromstring(stri)
    #
    # for c in root.findall('country'):
    #     rank = c.find('rank').text
    #     print('rank is:' + rank)

    # for child in root:
    #     print(child.tag, child.attrib)
    #
    # for neighbor in root.iter('neighbor'):
    #     print(neighbor.attrib)
