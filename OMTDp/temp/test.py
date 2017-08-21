# test
# Created by JKChang
# 03/08/2017, 10:37
# Tag:
# Description:

import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    # rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(elem)
    return reparsed.toprettyxml(indent="\t")


def extractAttri(root, tag):
    try:
        res = []
        for ele in root.findall(tag):
            res.append(ele.text)
        return res
    except:
        raise TypeError('Fail to find attribute %s' % tag)


url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=paracetamol&resulttype=core&pageSize=3'
xml_str = urllib.request.urlopen(url).read().decode('utf-8')
# print(prettify(xml_str))

root = ET.fromstring(xml_str)

count = 0
for result in root.iter('result'):
    abstract = extractAttri(result, 'abstractText')
    print(abstract)





#
#
# id = 9843981
# url = r'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % id
# print(url)
#
# xml_str = request.urlopen(url).read().decode('utf8')
# root = ET.fromstring(xml_str)
# # print(prettify(root))  # pretty print
# # print(root.tag) #print out the root
#
# # ==================Child level=======================
# for child in root:
#     print (child.tag)



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
