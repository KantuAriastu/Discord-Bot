#interesting conversion

from operator import methodcaller
from random import choice


      
conversion = {}
def load_convtable():
    with open("conversionkey.txt", "r") as keys :
        for lines in keys :
            if lines[0] != "#":
                name,factor = lines.split(",")
                conversion[name] = float(factor)
    

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
    
    def conversion(self,convname):
        self.val = self.val/conversion[convname]
        self.unit = convname
        return self
        
    def randomconversion(self):
        name = choice(list(d.keys()))
        conversion(name)

    def print (self) :
        print (str(self.val) + " " + str(self.unit)) 
        return self
    
    def msgconstruct (self) :
        msg = str(self.val0)+" "+str(self.unit0)+" is equal too "+str(self.val)+" "+str(self.unit)
        return msg
