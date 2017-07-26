# PMCCore
# Created by JKChang
# 26/07/2017, 20:37
# Tag:
# Description: PMC core file

import urllib2
from lxml import etree
from PMCattribute import PMC_Attribute


class PMCCore(str):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def prettyPrint(self):
        def prettyCore(self):
            root = etree.fromstring(self)
            print etree.tostring(root, pretty_print=True)

    def getID(self):
        return self.__extractAttri__(PMC_Attribute.ID)

    def getSource(self):
        return  self.__extractAttri__(PMC_Attribute.SOURCE)

    def getPMID(self):
        return  self.__extractAttri__(PMC_Attribute.PMID)

    def getPMCID(self):
        return  self.__extractAttri__(PMC_Attribute.PMCID)

    def getDOI(self):
        return  self.__extractAttri__(PMC_Attribute.DOI)

    def getTitle(self):
        return  self.__extractAttri__(PMC_Attribute.TITLE)

    def getAbstract(self):
        return self.__extractAttri__(PMC_Attribute.ABSTRACT)



    def __extractAttri__(self, attri):
        if not isinstance(attri, PMC_Attribute):
            raise TypeError('The core does not include attribute called ' + attri)
        print attri.value

    def printContent(self):
        pass
