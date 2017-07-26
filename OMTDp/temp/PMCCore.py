# PMCCore
# Created by JKChang
# 26/07/2017, 15:49
# Tag:
# Description: core

import urllib2
from lxml import etree


class Core(str):
    def __new__(cls, value):
        return str.__new__(cls, value)

    def prettyCore(self):
        root = etree.fromstring(self)
        print etree.tostring(root, pretty_print=True)
