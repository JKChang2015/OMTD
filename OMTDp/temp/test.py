# test
# Created by JKChang
# 03/08/2017, 10:37
# Tag:
# Description:



l1 = [23]
if len(l1) ==1:
    print(l1[0])
else:
    print(l1)
# import urllib.request
# import xml.etree.ElementTree as ET
#
#
# def extractAttri(root, tag):  # get single attribute (tag)
#     try:
#         res = []
#         for ele in root.findall(tag):
#             res.append(ele.text)
#         return res
#     except:
#         raise TypeError('Fail to find attribute %s' % tag)
#
#
# def getResult(root, *attri, ALL=False):  # get certain attribute from <result> ... </result>
#     resDict = {}
#     if ALL:
#         att = ('source', 'pmid', 'pmcid', 'doi', 'title', 'authorString', 'abstractText')
#     else:
#         att = attri
#
#     for ele in att:
#         if len(extractAttri(root, ele)) != 0:
#             resDict[ele] = extractAttri(root, ele)
#     return resDict
#
#
# def _getValues(attributeResult, dict):
#     values = 'None'
#     if dict.__contains__(attributeResult):
#         values = '\n'.join(dict[attributeResult])
#
#     return values
#
#
# def printit(resDict):
#     p = _getValues('title', resDict) + ' (https://www.ncbi.nlm.nih.gov/pubmed/?term=%s) \n' % _getValues(
#         'pmid', resDict)
#     p += 'Author: %s \n' % _getValues('authorString', resDict)
#     p += 'DOI: %s \n' % _getValues('doi', resDict)
#     p += 'Source: %s \n' % _getValues('source', resDict)
#     p += 'PMID: %s \n' % _getValues('pmid', resDict)
#     if resDict.__contains__('pmcid') and len(resDict['pmcid']) != 0:
#         p += 'PMCID: %s \n' % _getValues('pmcid', resDict)
#     p += 'Abstract: %s \n' % _getValues('abstractText', resDict)
#     return p
#
#
# url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=paracetamol&resulttype=core&pageSize=100'
# xml_str = urllib.request.urlopen(url).read().decode('utf-8')
# # print(prettify(xml_str))
#
# root = ET.fromstring(xml_str)
# print(type(root))
#
# count = 0
#
# # res = []
# for result in root.iter('result'):
#     print('-' * 130)
#     print(printit(getResult(result, ALL=True)))
#     print('-' * 130)


# abstract = extractAttri(result, 'source')
# print(abstract)





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
