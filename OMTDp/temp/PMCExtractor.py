# fileExtractor
# Created by JKChang
# 26/07/2017, 13:56
# Tag:
# Description: extract PMC XML attributes

import urllib.request, urllib.error, urllib.parse
from lxml import etree

import PMCattribute
from PMCCore import Core


class PMCExtractor(object):

    def extractCore(self, PMID):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % PMID
        core = Core(urllib.request.urlopen(url).read())
        print(core)
        return core

    def prettyCore(self):
        root = etree.fromstring(self.core)
        print(etree.tostring(root, pretty_print=True))
        # return etree.tostring(root, pretty_print=True)

    def extractAbstract(self, PMID):
        core = self.extractCore(PMID)

    def __getPMDattri(self, atriName):
        return PMCattribute.PMDattribute.__getattribute__(atriName)
