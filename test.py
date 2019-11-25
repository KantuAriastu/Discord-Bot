import re 
from conversion import *

regex = r"(\d+\s*)(centi|cm|mm|mili|km|kilo|meter|m)"
length_find = re.compile(regex)

string = "aku beli 20 centi versi sih, 20meter,m, 30m"
matched = length_find.findall(string)





matched = length_find.findall(string)
for x, unit in matched :
    length = lengthconv(float(x),unit)
    length.randomconversion()
    msg = length.msgconstruct()
    print(msg)

