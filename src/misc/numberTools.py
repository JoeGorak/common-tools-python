'''
Created on Sep 20, 2013

@author: anuvrat
'''

import math
from misc.memoize import Memoize

@Memoize
def numberOfDigitsIn(number):
    if number > 0: return int( math.log10( number ) ) + 1
    elif number == 0: return 1
    else: return int( math.log10( -number ) ) + 2

@Memoize
def getDigitsIn( number ):
    if number < 0:
        number *= -1

    digits = []
    while number > 0:
        digits.append( number % 10 )
        number = int( number / 10 )
    digits.reverse()
    return digits

def getNumberFrom( digits ):
    num = 0
    for digit in digits:
        num = num * 10 + digit
    return num

def gcd( a, b ):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

if __name__ == '__main__':
    print( getDigitsIn( -1234 ) )
    print( getNumberFrom( [1, 2, 3, 4] ) )
