# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 17:21:46 2025

@author: grant
"""

# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Matthew Mockabee & Grant Heisey
#
# Date: 2/3/2025
# 
##################################################
#
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import math



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def CESutility_valid(good_x: float, good_y: float, parameter: float) -> float:
    """ Returns the same value as CESutility() when x and y are non-negative
    numbers and r is strictly positive but
    returns the value None otherwise"""
    
    if good_x < 0:
        print("Error: good_x cannot be negative.")
        return None
    if good_y < 0:
        print("Error: good_y cannot be negative.")
        return None
    if parameter <= 0:
        print("Error: paramter must be strictly positive")
        return None
    return ((good_x ** parameter) + (good_y ** parameter)) ** (1 / parameter)

# ...

# Exercise C


def logit(x, beta0, beta1):
    """Computes the logit function ℓ(x; β0, β1)."""
    exponent = beta0 + x * beta1
    return math.exp(exponent) / (1 + math.exp(exponent))


#Exercise D


def logit_like(yi, xi, beta0, beta1):
    """Computes the log-likelihood of an observation (yi, xi)."""
    p = logit(xi, beta0, beta1)
    
    if yi == 1:
        return math.log(p)
    else:
        return math.log(1 - p)


# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Code goes here.

#A
print(CESutility_valid(4, 5, 1))
print(CESutility_valid(-4, 5, 1))
print(CESutility_valid(8, -10, 2))
print(CESutility_valid(8, 10, -2))

#B

#C
print(logit(0, 0, 0))
print(logit(1, math.log(1), math.log(2)))
print(logit(2, math.log(1/2), math.log(3)))

#D
print(logit_like(1, 0, 0, 0))
print(logit_like(0, 1, 0, 1))
print(logit_like(1, 2, 1, 1))

##################################################
# End
##################################################
