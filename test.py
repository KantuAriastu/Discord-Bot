import re 
from conversion import *
from random import choice
#interesting conversion

from operator import methodcaller
from random import choice

conversion_dict = {}
with open("conversionkey.txt", "r") as keys :
    for lines in keys :
        if lines[0] != "#":
            name,factor = lines.split(",")
            conversion_dict[name] = float(factor)
    

class lengthconv() :
 
    def __init__(self ,x,unit) :
        self.unit = unit
        if (unit == "centimeter") or (unit== "cm") :
            self.val = x/100.0
            self.unit0 = "centimeter"
        elif (unit == "mm") or (unit == "millimeter"):
            self.val = x/1000.0
            self.unit0 = "millimeter"
        elif (unit == "km") or (unit=="kilometer"):
            self.val = x*1000.0
            self.unit0 = "kilometer"
        else :
            self.val = x
            self.unit0 = "meter"
        self.val0 = x
    
    def conversion(self,name):
        self.val = self.val/conversion_dict[name]
        self.unit = name
        return self
        
    def randomconversion(self):
        name = choice(list(conversion_dict.keys()))
        self.conversion(name)

    def printself (self) :
        print (str(self.val) + " " + str(self.unit)) 
        return self
    
    def msgconstruct (self) :
        msg = str(self.val0)+" "+str(self.unit0)+" is equal too "+str(self.val)+" "+str(self.unit)
        print (msg)
        return msg




regex = r"(\d+\s*)(centimeter|cm|mm|millimeter|km|kilometer|meter|m)"
length_find = re.compile(regex)

string = "aku beli 20 centimeter versi sih, 20meter,m, 30m"
matched = length_find.findall(string)

matched = length_find.findall(string)
for x, unit in matched :
    length = lengthconv(float(x),unit)
    length.randomconversion()
    length.msgconstruct()
    


