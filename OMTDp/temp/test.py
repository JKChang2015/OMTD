# test
# Created by JKChang
# 03/08/2017, 10:37
# Tag:
# Description:

from urllib import request
from xml.dom import minidom
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import lxml.etree as etree


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")


id = 9843981
url = r'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % id
print(url)

xml_str = request.urlopen(url).read().decode('utf8')
root = ET.fromstring(xml_str)
# print(prettify(root))  # pretty print
# print(root.tag) #print out the root

# ==================Child level=======================
for child in root:
    print (child.tag)



# # for child in root:
# #     print(child.tag)
# #
# # print('==========')
# #
#
# for  ab in root.iter("abstractText"):
#     print(ab.text)
#
# for results in root.findall("resultList"):
#     for result in results:
#         for elements in result:
#             for ab in elements.findall("abstractText"):
#                 print (ab[0].text)
#         # print(elements.tag)
#
#
# # ab = element.find('abstractText')
# #             print(ab.text)
#
# def perf_func(elem, func, level=0):
#     func(elem, level)
#     for child in elem.getchildren():
#         perf_func(child, func, level + 1)
#
#
# def print_level(elem, level):
#     print('\t' * level + elem.tag)
#
# # perf_func(root, print_level)
#
#
#
# # print('the root of the xml is ' + root.tag)
# # print(root.attrib)
# #
# # gen = (child for child in root if (child.tag == "resultList"))
# #
# # for x in gen:
# #     print(x.tag)
#
#
#
#
# # for child in root if child.name == "resultList ":
# #     print(child.tag, child.attrib)
