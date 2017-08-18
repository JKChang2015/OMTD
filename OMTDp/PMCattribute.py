# PMDattribute
# Created by JKChang
# 26/07/2017, 14:08
# Tag:
# Description: enums class of PMC tags

from enum import Enum, unique


@unique
class PMC_Attrib(Enum):
    SOURCE = 'source'
    PMID = 'pmid'
    PMCID = 'pmcid'
    DOI = 'doi'
    TITLE = 'title'
    AUTHOR = 'authorString'
    ABSTRACT = 'abstractText'


# print(PMC_Attrib.__members__.keys())
# print(type(PMC_Attrib.__members__.keys()))
# key = PMC_Attrib.__members__.keys()
# print(key)
#
# if 'DOI' in key:
#     print('OK')
# else:
#     print('Not OK')



