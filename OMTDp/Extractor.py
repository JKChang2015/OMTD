# PMCCore
# Created by JKChang
# 26/07/2017, 20:37
# Tag:
# Description: search keyword return list from PMID

import textwrap
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom


class PMIDExtractor():
    def __init__(self):
        """initialisation, result restore in PMIDs[]"""
        self.PMIDs = []

    def search(self, keyword):
        """return list of PMIDs"""
        pageSize = 100
        resulttype = 'idlist'  # idlist, core or lite
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s&resulttype=%s&pageSize=%s' % (
            keyword, resulttype, pageSize)
        print(url)

        xml_str = urllib.request.urlopen(url).read().decode('utf-8')
        # print(prettify(xml_str))

        self.PMIDs = _extractAttri(xml_str, 'pmid')

        # print(self.PMIDs)
        return self.PMIDs


class CoreExtractor():
    def __init__(self):
        """initialisation, result restore in coreList []"""
        self.coreList = []

    def search(self, keyword):
        """return coreList"""
        pageSize = 100
        resulttype = 'core'  # idlist, core or lite
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s&resulttype=%s&pageSize=%s' % (
            keyword, resulttype, pageSize)
        print(url)

        xml_str = urllib.request.urlopen(url).read().decode('utf-8')
        root = ET.fromstring(xml_str)

        for result in root.iter('result'):
            core = _getResult(result, ALL=True)
            self.coreList.append(core)

        return self.coreList


def _extractAttri(root, tag):  # get single attribute (tag)
    try:
        attrib = []
        for ele in root.findall(tag):
            attrib.append(ele.text)
        return attrib
    except:
        raise TypeError('Fail to find attribute %s' % tag)


def _getResult(root, *attri, ALL=False):  # get certain attribute from <result> ... </result>
    resDict = {}
    if ALL:
        att = ('source', 'pmid', 'pmcid', 'doi', 'title', 'authorString', 'abstractText')
    else:
        att = attri

    for ele in att:
        attribute = _extractAttri(root, ele)

        if len(attribute) == 0 and ele != 'pmcid':
            resDict[ele] = 'None'
        elif len(attribute) == 1:
            resDict[ele] = attribute[0]
        else:
            resDict[ele] = attribute

    return resDict


def _prettyCore(resDict):  # print result in format
    # if len(resDict) == 0:
    #     self.getAttribute(ALL=True)
    # # remove empty elements attri
    # printList = ['title', 'doi', 'pmid', 'pmcid', 'source', 'authorString', 'abstractText']
    p = '%(title)s (https://www.ncbi.nlm.nih.gov/pubmed/?term=%(pmid)s) \n' % resDict
    p += 'Author: %(authorString)s \n' % resDict
    p += 'DOI: %(doi)s \n' % resDict
    p += 'Source: %(source)s \n' % resDict
    p += 'PMID: %(pmid)s \n' % resDict
    if resDict.__contains__('pmcid') and len(resDict['pmcid']) != 0:
        p += 'PMCID: %(pmcid)s \n' % resDict
    p += 'Abstract: %(abstractText)s \n' % resDict
    return p


def _getValues(attributeResult, dict):  # get values from result dict
    values = 'None'
    if dict.__contains__(attributeResult):
        values = '\n'.join(dict[attributeResult])

    return values


def _prettyXML(elem):
    """Return a pretty-printed XML string for the Element."""
    if isinstance(elem, ET.Element):
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
    elif isinstance(elem, str):
        reparsed = minidom.parseString(elem)
    else:
        return
    return reparsed.toprettyxml(indent="\t")


ex = CoreExtractor()
results = ex.search('paracetamol')

for article in results:
    print('-' * 200)
    # print('{:<250s}'.format(_prettyCore(article)))
    print(textwrap.fill(_prettyCore(article), width=200, break_long_words=False, replace_whitespace=False))
    # print(_prettyCore(article))
