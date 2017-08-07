# newString
# Created by JKChang
# 26/07/2017, 16:44
# Tag:
# Description: 

class newString(str):
    def __new__(cls, value):
        obj = str.__new__(cls, value)
        return obj


a = newString('abic')
