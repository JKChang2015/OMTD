# OMTD
# Created by JKChang
# 27/07/2017, 15:19
# Tag:
# Description: API basic function

import urllib.request, urllib.error, urllib.parse


class searcher():
    xml = ''
    IDResult = []
    count = 0

    def searching(self, keyword):
        url = 'http://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%s&resulttype=idlist' % keyword
        print(url)
        self.xml = urllib.request.urlopen(url).read()
        return self.xml

    def getIDList(self):
        return self.IDResult

    def getCount(self):
        return self.cout

    def __extract(self):
        pass





# def XMLPretty(string):
#         root = etree.fromstring(string)
#         return etree.tostring(root, pretty_print=True)
#
# k = 'paracetamol'
# s = searcher()
# xml = s.searching(k)
# print(XMLPretty(xml).decode('utf8'))
