# Core
# Created by JKChang
# 18/08/2017, 09:20
# Tag:
# Description: @input: PMID
#              @output: each component of core file

import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom


# source pmid pmcid doi title authorString abstractText


class Core(object):


    def __init__(self, PMID):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%s&resulttype=core' % PMID
        # print(url)
        self.core_str = urllib.request.urlopen(url).read().decode('utf-8')
        self.resDict ={}
        # print(_prettify(self.core_str))

    def getAttribute(self, *attri, ALL=False):  # get results in dict for *attri
        if ALL:
            att = ('source', 'pmid', 'pmcid', 'doi', 'title', 'authorString', 'abstractText')
        else:
            att = attri

        for ele in att:
            value = _attriExtract(self.core_str, ele)
            self.resDict[ele] = value

        if self.resDict.__contains__('pmcid') and len(self.resDict['pmcid']) == 0:
            self.resDict.pop('pmcid')

        return self.resDict

    def __str__(self):
        if len(self.resDict) == 0:
            self.getAttribute(ALL=True)

        # remove empty elements attri

        # printList = ['title', 'doi', 'pmid', 'pmcid', 'source', 'authorString', 'abstractText']
        p = _getValues('title', self.resDict) + ' (https://www.ncbi.nlm.nih.gov/pubmed/?term=%s) \n' % _getValues(
            'pmid', self.resDict)
        p += 'Author: %s \n' % _getValues('authorString', self.resDict)
        p += 'DOI: %s \n' % _getValues('doi', self.resDict)
        p += 'Source: %s \n' % _getValues('source', self.resDict)
        p += 'PMID: %s \n' % _getValues('pmid', self.resDict)
        if self.resDict.__contains__('pmcid') and len(self.resDict['pmcid']) != 0:
            p += 'PMCID: %s \n' % _getValues('pmcid', self.resDict)
        p += 'Abstract: %s \n' % _getValues('abstractText', self.resDict)
        return p


def _getValues(attributeResult, dict):
    values = '\n'.join(dict[attributeResult])
    return values


def _attriExtract(content_str, attri):
    try:
        res = []
        root = ET.fromstring(content_str)
        for results in root.iter('result'):
            for ele in results.findall(attri):
                res.append(ele.text)
        return res
    except:
        raise TypeError('The core file does not include attribute called ' + attri)


def _prettify(elem):
    reparsed = minidom.parseString(elem)
    return reparsed.toprettyxml(indent="\t")

