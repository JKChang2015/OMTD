# print_hyer
# Created by JKChang
# 03/08/2017, 15:42
# Tag:
# Description:

from xml.dom import minidom
import xml.etree.ElementTree as ET

def perf_func(elem, func, level=0):
    func(elem, level)
    for child in elem.getchildren():
        perf_func(child, func, level + 1)


def print_level(elem, level):
    print('\t' * level + elem.tag)

#======================================================

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")