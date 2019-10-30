#interesting conversion

base_length = ("centi","cm","mm","mili","km","kilo","meter","m")


def any2meter(x,unit)
    if (unit == "centi") or (unit== "cm"):
        return x/100.0
    elif (unit == "mm") or (unit== "mili"):
        return x/1000.0
    elif (unit == "km") or (unit=="kilo"):
        return x*1000.0
    else :
        return x

def meter2furlongs(x) :
     return x/201.168
    
def meter2parsecs(x) :
    return x/3.086e+16
    
def meter2cubits :
    return x/0.4572

def meter2smoots :
    return x/1.7018

def meter2planck :
    return x/6.25e+34

def meter2lightyrs :
    return x/9.461e+15

def meter2astro :
    return x/1.496e+11

def meter2shakus :
    return x/0.30303
    