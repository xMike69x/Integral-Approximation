import math

#Some single variable function with an interval
#Output an aproximation of the area under the curve using Riemann Sums

#Write a code that can get the point of the function
    #parse the string into math symbols and have a throw exception if
    #1. contains more than one value
    #2. doesn't have a number or variable at the end of an accepted symbol
    #3. Only have accepted values such as: (+,-,/,*, ^, (, ), x, .)
    #has braces in the right place


                

def getPoint(func, point):
        func = func.replace('x', str(point))
        func = func.replace('math.e', str(math.e))
        func = func.replace('math.pi', str(math.pi))

        result = eval(func)
        return float(result)

def getAproxArea(func, start, end, type):
    
    if type == "disc":   
        length = 1
    else:
         length = 0.01

    

    pointer = start
    riemannSum = 0
    while end >= pointer:
        riemannSum += getPoint(func, pointer) * length
        pointer += length

    return riemannSum

def normalDist( sigma, mu):
     return F"(1/({sigma} * math.sqrt(2 * math.pi))) * (math.e ** (-1*((x - {mu}) ** 2)/(2 * {sigma} ** 2)))"

def gammaFunction(n):
     gamma = F"x ** ({n} -1) * math.e ** (-1 * x)"
     return getAproxArea(gamma, 0, 100)



def betaDist(alpha, beta):
     firstPart = F"{gammaFunction(alpha + beta)} / ({gammaFunction(alpha)} * {gammaFunction(beta)}) "
     secondPart = F"* (1 -x) **({beta} -1) * x **({alpha} - 1)"
     combo = firstPart + secondPart
     return combo

def gammaDist(alpha, beta):
     return F"1/({beta} ** ({alpha}) * {gammaFunction(alpha)}) * x **({alpha} -1) * math.e **(-x/ {beta})"

def uniformDist(alpha, beta):
     return F"1/ {beta} - {alpha}"