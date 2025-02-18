# -*- coding: utf-8 -*-
"""
##################################################
#
# QMB 3311: Python for Business Analytics
#
# Name: Matthew Mockabee & Grant Heisey
#
# Date: 2/17/2025
# 
##################################################
#
# Sample Script for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy as np

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def matrix_inverse(mat_in):
    """
    Replicate the numpy method linalg.inv() that calculates the inverse of 
    a two-by-two matrix mat in.
    The inverse of the matrix A denoted A−1, is a matrix the same size as A 
    such that A * A−1 = I, where I is the identity matrix with ones on the
    diagonal and zeros elsewhere. It can be used to solve the systems of 
    equations A * x = b by multiplying A−1 with b toget x = A−1 * b
    """
    if mat_in.shape != (2, 2):
        print("Error: Input must be a 2x2 matrix")
        return None
        
    a11, a12 = mat_in[0, 0], mat_in[0, 1]
    a21, a22 = mat_in[1, 0], mat_in[1, 1]
    
    det = a11*a22 - a12*a21
    
    if det == 0:
        print("Error: Determinant cannot be zero")
        return None
    else: mat_out = np.zeros((2, 2))
    mat_out[0, 0] = a22/det
    mat_out[0, 1] = -a12/det
    mat_out[1, 0] = -a21/det
    mat_out[1, 1] = a11/det
    
    return mat_out

# Exercise 2

def logit_like(x, beta_0, beta_1):
    
    z= beta_0 + x * beta_1
    
    return np.exp(z) / (1 + np.exp(z))

def logit_like_sum(y,x,beta_0, beta_1):
    
    log_likelihood = 0
    for i in range(len(y)):
        log_likelihood += logit_like(y[i],x[i],beta_0,beta_1)
        
        if y[i] == 1:
            log_likelihood += np.log(logit_like)
        else:
            log_likelihood += np.log(1 - logit_like)
       
        return log_likelihood

# Exercise 3

def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model.
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1"""
    
    grad_beta_0 = 0.0
    grad_beta_1 = 0.0
   
    for i in range(len(y)):
        l_val = logit_like(x[i], beta_0, beta_1)
          
        if y[i] == 1:
            grad_beta_0 += (1 - l_val)
            grad_beta_1 += x[i] * (1 - l_val)
        else:
            grad_beta_0 += (-l_val)
            grad_beta_1 += x[i] * (-l_val)
    
    return np.array([grad_beta_0, grad_beta_1])


# Exercise 4

def CESutility_multi(x, a, r):
   """Calculate the Constant Elasticity of Substitution utility for multiple goods."""
   if not isinstance(x, (list, np.ndarray)) or not isinstance(a, (list, np.ndarray)):
       return None 
   x = np.array(x, dtype=float)
   a = np.array(a, dtype=float)
   if len(x) != len(a) or len(x) == 0:
       return None
   if np.any(x < 0) or np.any(a < 0):
       return None
   if np.all(a == 0):
       return None
   if not isinstance(r, (int, float)):
       return None
   r = float(r)
   if r == 0:
       return float(np.prod(np.power(x, a)))
   power_terms = np.power(a, 1-r) * np.power(x, r)
   sum_term = np.sum(power_terms)
   if sum_term <= 0:
       return None
   result = np.power(sum_term, 1/r)
   if not np.isreal(result) or np.isnan(result) or np.isinf(result):
       return None
   return float(result)

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 
Exercise 3:
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], 0.0, 0.0)
    [0.0, 0.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(3), 0.0)
    [-1.0, -10.0]
    >>> logit_like_grad([1, 1, 0, 0], [15.0, 5.0, 15.0, 5.0], math.log(7), 0.0)
    [-1.5, -15.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(2))
    [0.0, 0.0]
    >>> logit_like_grad([1, 0, 1], [1, 1, 1], 0.0, math.log(5))
    [-0.5, -0.5]
    >>> logit_like_grad([1, 0, 1], [3, 3, 3], 0.0, math.log(2))
    [-2/3, -2.0]


Exercise 4:
    >>> (CESutility_multi([1, 1], [1, 1], 0.5))  
    4.0
    >>> (CESutility_multi([1, 2, 3], [0.5, 0.3, 0.2], 0.5))  
    5.090890230020665
    >>> (CESutility_multi([1, -1], [1, 1], 0.5))
    None

# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################
