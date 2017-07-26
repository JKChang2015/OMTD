# fileExtractor
# Created by JKChang
# 26/07/2017, 13:56
# Tag:
# Description: extract PMC XML attributes

import urllib2
from lxml import etree
import PMDattribute


class PMCExtractor(object):
    core = ''

    def extractCore(self, PMID):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:%d&resulttype=core' % PMID
        self.core = urllib2.urlopen(url).read()
        return self.core

    def prettyCore(self):
        root = etree.fromstring(self.core)
        print etree.tostring(root, pretty_print=True)
        return etree.tostring(root, pretty_print=True)

    def extractAbstract(self,PMID):
        core = self.extractCore(PMID)

    def __getPMDattri(self,atriName):
        return PMDattribute.PMDattribute.__getattribute__(atriName)

