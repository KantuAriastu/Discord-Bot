#interesting conversion

from operator import methodcaller
from random import choice

class lengthconv() :
 
    def __init__(self ,x,unit) :
        self.unit = unit
        if (unit == "centi") or (unit== "cm"):
            self.val = x/100.0
            self.unit0 = "centimeter"
        elif (unit == "mm") or (unit== "mili"):
            self.val = x/1000.0
            self.unit0 = "millimeter"
        elif (unit == "km") or (unit=="kilo"):
            self.val = x*1000.0
            self.unit0 = "kilometer"
        else :
            self.val = x
            self.unit0 = "meter"
        self.val0 = x
        

    def furlongs(self) :
        self.val=  self.val/201.168
        self.unit = "furlongs"
        return self
    
    def parsecs(self) :
        self.val = self.val/3.086e+16
        self.unit = "parsecs"
        return self

    def cubits (self):
        self.val = self.val/0.4572
        self.unit = "cubits"
        return self

    def smoots (self):
        self.val = self.val/1.7018
        self.unit = "smoots"
        return self

    def planck (self):
        self.val = self.val/6.25e+34
        self.unit = "planck"
        return self

    def lightyrs (self):
        self.val = self.val/9.461e+15
        self.unit = "light years"
        return self

    def astro (self):
        self.val = self.val/1.496e+11
        self.unit = "astro"
        return self

    def shakus (self):
        self.val = self.val/0.30303
        self.unit = "shakus"
        return self

    def randomconversion(self):
        methods = 'furlongs','parsecs','astro','shakus','cubits','smoots','planck','lightyrs'
        method = methodcaller(choice(methods))
        return method(self)

    def print (self) :
        print (str(self.val) + " " + str(self.unit)) 
        return self
    
    def msgconstruct (self) :
        msg = str(self.val0)+" "+str(self.unit0)+" is equal too "+str(self.val)+" "+str(self.unit)
        return msg

