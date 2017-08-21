# PMCCore
# Created by JKChang
# 26/07/2017, 20:37
# Tag:
# Description: search keyword return list from PMID

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
        self.coreList = _extractInResults(xml_str)

        print(self.coreList)
        return self.coreList


def _extractAttri(root, tag):
    '''extract specified attribute according to the tag'''
    try:
        res = []
        for ele in root.iter(tag):
            res.append(ele.text)
        return res
    except:
        raise TypeError('The xml file does not include tag called ' + tag)


def _extractInResults(xml_str):
    try:
        att = ('source', 'pmid', 'pmcid', 'doi', 'title', 'authorString', 'abstractText')
        res = []
        root = ET.fromstring(xml_str)
        for result in root.iter('result'):  # for each article
            resDict = {}
            for attri in att:  # for each attribute
                for ele in result.findall(attri):
                    pass

        return res
    except:
        raise TypeError('Fail to load result list')


def _printCore(resDict):
    if len(resDict) == 0:
        self.getAttribute(ALL=True)

    # remove empty elements attri

    # printList = ['title', 'doi', 'pmid', 'pmcid', 'source', 'authorString', 'abstractText']
    p = _getValues('title', resDict) + ' (https://www.ncbi.nlm.nih.gov/pubmed/?term=%s) \n' % _getValues(
        'pmid', resDict)
    p += 'Author: %s \n' % _getValues('authorString', resDict)
    p += 'DOI: %s \n' % _getValues('doi', resDict)
    p += 'Source: %s \n' % _getValues('source', resDict)
    p += 'PMID: %s \n' % _getValues('pmid', resDict)
    if resDict.__contains__('pmcid') and len(resDict['pmcid']) != 0:
        p += 'PMCID: %s \n' % _getValues('pmcid', resDict)
    p += 'Abstract: %s \n' % _getValues('abstractText', resDict)
    return p


def _getValues(attributeResult, dict):
    values = '\n'.join(dict[attributeResult])
    return values


def _prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    # rough_string = ET.tostring(elem, 'utf-8')
    # reparsed = minidom.parseString(rough_string)
    reparsed = minidom.parseString(elem)
    return reparsed.toprettyxml(indent="\t")


ex = CoreExtractor()
res = ex.search('paracetamol')
print(res)
