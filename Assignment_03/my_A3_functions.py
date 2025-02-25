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

def CESUtility_in_budget(x: float, y: float, r: float, p_x: float, p_y: float, w: float) -> float:
    """Calculate the constant elasticity of substitution utility function for two goods. This version first checks that budget constraint is satisfied" 
    >>> CESutility_in_budget(3,4,2,1,1,10)
    5.0
    >>> CESutility_in_budget(1,1,2,5,10,15)
    1.41421
    >>> CESutility_in_budget(3,4,0,1,1,10)
    Error in CESUtility_in_budget: budget constraint not satisfied.
    """
    
    if p_x*x + p_y*y > w: 
        print('Error in CESUtility_in_budget: budget constraint not satisfied.')
        return None
    else:
        utility = CESutility_valid(x, y, r)
        return utility 
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
