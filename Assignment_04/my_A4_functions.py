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
import math
import doctest

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def matrix_inverse(mat_in): # expected input/output? (-2)
    """
    Replicate the numpy method linalg.inv() that calculates the inverse of 
    a two-by-two matrix mat in.
    The inverse of the matrix A denoted A−1, is a matrix the same size as A 
    such that A * A−1 = I, where I is the identity matrix with ones on the
    diagonal and zeros elsewhere. It can be used to solve the systems of 
    equations A * x = b by multiplying A−1 with b toget x = A−1 * b
    >>> np.array([[1, 0], [0, 1]])
    
    >>> mat2 = np.array([[4, 7], [2, 6]])
    
    >>> mat3 = np.array([[3, 5], [1, 2]])

    """
    
    # incomplete test cases (-3)
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
    
    return mat_out # does not follow instructions (-5)

# Exercise 2

def logit_like(x, beta_0, beta_1): # use function from earlier assignment
    
    z= beta_0 + x * beta_1
    
    return np.exp(z) / (1 + np.exp(z))

def logit_like_sum(y: list[int], x:list[float], beta_0: float, beta_1: float) -> float: # expected input/output? (-2)
    """Calculates the sum of the Log-Likelihood across all observations
    (y_i, x_i, i = 1, ..., n) using the Logistic regression model. Lists x and y respresent
    the pairs of observations,with thr intercept coefficient beta_0 and the slope coefficient beta_1.

    Each observation / list item in y must be 1 or 0. Lists x and y must have the same length,
    corresponding to the number of observations. 
    
    >>> logit_like_sum([1,0,1],[3,2,5],2,3)
    -8.000352
    >>> logit_like_sum([0,1,0,1],[2,4,1,5],0,1)
    -3.465055
    >>> logit_like_sum([0,2,2],[2,4,1,5],0,1)
    Error: All values in list y must be either 0 or 1
    Error: Lists x and y must have the same length
    """
    # incorrect test cases (-3)
    # missing checks for lengths and issues with y values. (-2)

    # code fails because arguments not provided in parts of the function (-3)
    
    invalid_y = False
    invalid_length = False
    for i in y:
        if i l= 1 and l= 0: 
            invalid_y = True
    if invalid_y == True:
        print("Error: All values in list y must be either 0 or 1")
    if len(x) l= len(y): 
        print("Error: Lists x and y must have the same length")
        invalid_length = True
    if invalid_length == True or invalid_y == True:
        return None
    log_likelihood = 0
    for i in range(len(y)):

        log_likelihood_summed += logit_like(y[i],x[i],beta_0,beta_1)

    return log_likelihood_summed

# Exercise 3

def logit_like_grad(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the gradient vector of the likelihood function
    for the bivariate logistic regression model.
    for sevaral pairs of observations in the lists x and y,
    coefficients beta_0 and beta_1
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
    [-2/3, -2.0]"""
    
    
    # missing checks for lengths and issues with y values. (-2)
    
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
   """Calculate the Constant Elasticity of Substitution utility for multiple goods.
    >>> CESutility_multi([1, 1], [1, 1], 0.5)  
    4.0
    >>> CESutility_multi([1, 2, 3], [0.5, 0.3, 0.2], 0.5) 
    5.090890230020665
    >>> CESutility_multi([1, -1], [1, 1], 0.5)
    None"""
    
    
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
       return None
   
    # Should add message for each of the issues above
    
   power_terms = np.power(a, 1-r) * np.power(x, r)
   sum_term = np.sum(power_terms)
   if sum_term <= 0:
       return None
   result = np.power(sum_term, 1/r)
   if not np.isreal(result) or np.isnan(result) or np.isinf(result):
       return None
   return float(result) # while this works, it is a bit off from when we worked on the code in class.

# Only function definitions above this point. 

##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. Didn't do this (-7)

# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################
