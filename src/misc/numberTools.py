'''
Created on Sep 20, 2013

@author: anuvrat
'''

import math

def numberOfDigitsIn(number):
    if number > 0: return int( math.log10( number ) ) + 1
    elif number == 0: return 1
    else: return int( math.log10( -number ) ) + 2
