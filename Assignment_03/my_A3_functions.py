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

def CESutility(good_x: float, good_y: float, r: float) -> float:
    """Calculate the constant elasticity of subsitution utility function for two goods.
    
    >>> CESutility(3, 4, 2)
    5.0
    >>> CESutility(1, 1, 2)
    1.4142135623730951
    >>> CESutility(3**0.5, 4**0.5, 4)
    2.23606797749979
    """
    
    utility = (good_x**r + good_y**r)**(1/r)
    return utility
#1
# Exercise A

def CESutility_valid(good_x: float, good_y: float, parameter: float) -> float:
    """ Return the same value as CESutility() when x and y are non-negative
    numbers and r is strictly positive.
    Return the value None otherwise"""
    
    # examples in description? (-3)
    if good_x < 0:
        print("Error: good_x cannot be negative.")
        return None
@@ -50,7 +64,7 @@
    if parameter <= 0:
        print("Error: paramter must be strictly positive")
        return None
    return ((good_x ** parameter) + (good_y ** parameter)) ** (1 / parameter)
    return CESutility(good_x, good_y, parameter)

# Exercise B

@@ -59,13 +73,11 @@
    """ Evaluate CESutility valid() when the consumer’s choice of goods x and y
    are within budget. 
    Return the value None otherwise"""
    
    # examples in description? (-3)
    if p_x < 0 or p_y < 0:
        print("Error: Prices cannot be negative")
        return None
    if r <= 0:
        print("Error: Parameter must be strictly positive")
        return None
# handled in CESutility_vaild()
    if w < (p_x * x + p_y * y):
        print("Error: Consumer's choice exceeds their budget")
        return None
@@ -74,23 +86,29 @@
# Exercise C


def logit(x, beta0, beta1):
def logit(x, beta0, beta1): # expected input/output? (-2)
    """Computes the logit function ℓ(x; β0, β1)."""
    # examples in description? (-3)
    exponent = beta0 + x * beta1
    return math.exp(exponent) / (1 + math.exp(exponent))


#Exercise D


def logit_like(yi, xi, beta0, beta1):
def logit_like(yi, xi, beta0, beta1): # expected input/output? (-2)
    """Computes the log-likelihood of an observation (yi, xi)."""
    p = logit(xi, beta0, beta1)
    
    if yi == 1:
        return math.log(p)
    # examples in description? (-3)
    link = logit(xi, beta0, beta1)
    if yi == 0:
        like = math.log(1 - link)
    elif yi == 1:
        like = math.log(link)
    else:
        return math.log(1 - p)
        print("Warning: y is not binary. y should be either 1 or 0.")
        like = None
    return like # missed case where yi could be not zero or 1 (-1)


# Only function definitions above this point.
