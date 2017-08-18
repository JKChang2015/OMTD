# fileExtractor
# Created by JKChang
# 26/07/2017, 13:56
# Tag:
# Description: extract PMC XML attributes

import urllib.error
import urllib.parse
import urllib.request

from lxml import etree

import PMCattribute


class PMCExtractor(object):
    def extractCore(self, PMID):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % PMID
        core = urllib.request.urlopen(url).read()
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
