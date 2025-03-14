# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 20:37:04 2025

@author: grant
"""

import math

# Question 1


def logit(x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the logit link function
     for variable x and beta_0 and beta_1.
    >>> logit(1, 0, 1)
    0.7310585786300049
    >>> logit(2, 15, 5)
    0.9999999999861121
    >>> logit(3, 1, 0)
    0.7310585786300049
    """
    link = math.exp(beta_0 + x*beta_1)/(1 + math.exp(beta_0 + x*beta_1))

    return link


def logit_like(y: int, x: float, beta_0: float, beta_1: float) -> float:
    """Calculates the value of the likelihood function for x and y.
    
    >>> logit_like(1, 17, 2, 0)
    -0.12692801104297252
    >>> logit_like(0, 0, 4, 2)
    -4.01814992791781
    >>> logit_like(1, 1, 2, 1/2)
    -0.07888973429254963
    """
    link = logit(x, beta_0, beta_1)
    if y == 0:
        like = math.log(1 - link)
    elif y == 1:
        like = math.log(link)
    else:
        print("y is not binary. y should be either 1 or 0.")
        like = None

    return like



def logit_like_sum(y: list, x: list, beta_0: float, beta_1: float) -> float:
    """Calculates the sum of the Log-Likelihood across all observations
    (y_i, x_i, i = 1, ..., n) using the Logistic regression model. Lists x and 
    y respresent the pairs of observations,with thr intercept coefficient 
    beta_0 and the slope coefficient beta_1.

    Each observation / list item in y must be 1 or 0. Lists x and y 
    must have the same length, corresponding to the number of observations. 
    
    >>> logit_like_sum([1,0,1],[3,2,5],2,3)
    -8.000352
    >>> logit_like_sum([0,1,0,1],[2,4,1,5],0,1)
    -3.465055
    >>> logit_like_sum([0,2,2],[2,4,1,5],0,1)
    Observations in y must be either zero or one.
    """
    
    like_sum = 0
    for i in range(len(y)):
        if y[i] in [0,1]:
            like_sum_i = logit_like(y[i], x[i], beta_0, beta_1)
            like_sum = like_sum + like_sum_i
        else:
            print('Observations in y must be either zero or one.')
            return None
        
    
    return like_sum



# Question 2

# Exercise A


def logit_di(x_i: float, k: int) -> float:
    """
    >>> logit_di(2, 1) 
    2
    >>> logit_di(22, 0)
    1
    >>> logit_di(69, 1)
    69
    """
    if k == 0:
        di = 1
    elif k == 1:
        di = x_i
    return di


# Exercise B


def logit_dLi_dbk(y_i: float, x_i: float, k: int, beta_0: float, beta_1: float) -> float:
    
    """
    >>> logit_dLi_dbk(1, 2, 1, 2, 1)
    0.0359724199241831
    >>> logit_dLi_dbk(0, 12, 0, 2, 16)
    -1.0
    >>> logit_dLi_dbk(1, 3, 0, 1, 1)
    0.01798620996209155
    """
    if y_i in [0, 1] :
        dLi_dbk = logit_di(x_i, k)*(y_i - logit(x_i, beta_0, beta_1))
    else:
            print('Observations in y must be zero or one.')
            dLi_dbk =  None
    return dLi_dbk





# Doc Test


if __name__ == "__main__":
    import doctest
    doctest.testmod()