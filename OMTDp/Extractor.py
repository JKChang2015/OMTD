# PMCCore
# Created by JKChang
# 26/07/2017, 20:37
# Tag:
# Description: PMC core file

import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from xml.dom import minidom

# from PMCattribute import PMC_Attrib
from Core import Core


class XMLExtractor(str):
    PMIDs = []

    def search(self, keyword):
        "return list of PMID "
        pageSize = 25
        resulttype = 'idlist'
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s&resulttype=%s&pageSize=%s' % (
            keyword, resulttype, pageSize)

        print(url)
        xml_str = urllib.request.urlopen(url).read().decode('utf-8')
        # print(prettify(xml_str))

        self.PMIDs = extract(xml_str, 'pmid')
        print(self.PMIDs)

    def getCore(self, PMID):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%s&resulttype=core' % PMID
        core_str = urllib.request.urlopen(url).read().decode('utf-8')
        print(prettify(core_str))
        return core_str


# def extractAttri(attri):
#     if isinstance('PMC_Attrib.' + attri, PMC_Attrib):
#         print('it\'s super OK')
#
#
#     else:
#         raise TypeError('attribute must be an instance of PMC_Attrib')


def extract(xml_str, tag):
    # if not isinstance(tag, PMC_Attrib):
    # raise TypeError('The xml file does not include tag called ' + tag)
    try:
        res = []
        root = ET.fromstring(xml_str)
        for ele in root.iter(tag):
            res.append(ele.text)
        return res
    except:
        raise TypeError('The xml file does not include tag called ' + tag)


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    # rough_string = ET.tostring(elem, 'utf-8')
    # reparsed = minidom.parseString(rough_string)


    reparsed = minidom.parseString(elem)
    return reparsed.toprettyxml(indent="\t")


ext = XMLExtractor()
ext.search('paracetamol')
for id in ext.PMIDs:
    core = Core(id)
    # core.getAttribute(ALL=True)
    print(core)
    print('--' * 50)


# idd = '28644687'
# ext.getCore(idd)



# extractAttri('HI')
