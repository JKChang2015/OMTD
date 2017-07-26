# PMDattribute
# Created by JKChang
# 26/07/2017, 14:08
# Tag:
# Description: enums class of PMD attribute

from enum import Enum


class PMC_Attribute(Enum):
    ID = 'id'
    SOURCE = 'source'
    PMID = 'pmid'
    PMCID = 'pmcid'
    DOI = 'doi'
    TITLE = 'title'
    ABSTRACT = 'abstractText'
