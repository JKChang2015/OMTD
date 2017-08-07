# PMDattribute
# Created by JKChang
# 26/07/2017, 14:08
# Tag:
# Description: enums class of PMC tags

from enum import Enum


class PMC_Attrib(Enum):
    SOURCE = 'source'
    PMID = 'pmid'
    PMCID = 'pmcid'
    DOI = 'doi'
    TITLE = 'title'
    AUTHOR = 'authorString'
    ABSTRACT = 'abstractText'
    


