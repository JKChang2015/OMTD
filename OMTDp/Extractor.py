# PMCCore
# Created by JKChang
# 26/07/2017, 20:37
# Tag:
# Description: PMC core file

import urllib.request, urllib.error, urllib.parse
from lxml import etree
from PMCattribute import PMC_Attrib
import xml.etree.ElementTree as ET


class XMLExtractor(str):
    # def __new__(cls, value):
    #     return str.__new__(cls, value)

    # def getSource(self):
    #     return self.__extractAttri(PMC_Attrib.SOURCE)
    #
    # def getPMID(self):
    #     return self.__extractAttri(PMC_Attrib.PMID)
    #
    # def getPMCID(self):
    #     return self.__extractAttri(PMC_Attrib.PMCID)
    #
    # def getDOI(self):
    #     return self.__extractAttri(PMC_Attrib.DOI)
    #
    # def getTitle(self):
    #     return self.__extractAttri(PMC_Attrib.TITLE)
    #
    # def getAbstract(self):
    #     return self.__extractAttri(PMC_Attrib.ABSTRACT)
    #
    # def getAuthor(self):
    #     return self.__extractAttri(PMC_Attrib.AUTHOR)

    def extract(self, xml_str, tag):
        # if not isinstance(tag, PMC_Attrib):
        #     raise TypeError('The xml file does not include tag called ' + tag)
        res = []
        root = ET.fromstring(xml_str)
        for ele in root.iter(tag):
            res.append(ele.attrib)
        return res
