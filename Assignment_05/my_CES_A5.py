import numpy as np
from typing import List

# Question 1


def CESutility(good_x: float, good_y: float, r: float) -> float:
    """Return the value of Constant Elasticity of Substitution utility function,
    measuring the degree of satisfaction a consumer may get from two goods.
    
    >>> CESutility(3, 4, 1)
    7.0
    >>> CESutility(100,50,20)
    100
    >>> CESutility(50,25,10)
    50.005
    """
    
    utility = (good_x**r + good_y**r)**(1/r)
    return utility


def CESutility_valid(good_x: float, good_y: float, r: float) -> float:
    """Return the same value as CESutility() when x and y are non-negative
    numbers and r is strictly positive.
    Return the value None otherwise 
    
    >>> CESutility_valid(3, 4, 1)
    5.0
    >>> CESutility_valid(1, 3, 2)
    3.1622776601683795
    >>> CESutility_valid(-3, 5, 4)
    Error in CESutility_valid: good_x is negative.
    """
    
    if good_x < 0 or good_y < 0 or r <= 0:
        if (good_x < 0):
            print('Error: good_x is negative.')
        if (good_y < 0):
            print('Error: good_y is negative.')
        if (r <= 0):
            print('Error: r is not positive.')
        return None
    else :
        utility = CESutility(good_x, good_y, r)
        return utility


def CESutility_in_budget(x: float, y: float, r: float, 
                         p_x: float, p_y: float, w: float) -> float:
    """Calculate the constant elasticity of substitution utility function for 
    two goods. This version first checks that budget constraint is satisfied
    
    >>> CESutility_in_budget(4, 4, 2, 1, 1, 15)
    5.656854249492381
    >>> CESutility_in_budget(2, 3, 2, 2, 25, 10)
    Error in CESutility_in_budget: budget constraint not satisfied.
    >>> CESutility_in_budget(3, 1, 3, 2, 2, 20)
    3.0365889718756622
    """

    if p_x*x + p_y*y > w:
        print('Error: budget constraint not satisfied.')
        return None
    else :
        utility = CESutility_valid(x, y, r)
        return utility


# Question 2

# Exercise C

def CESdemand_calc(r: float, p_x: float, p_y: float, w: float) -> List[float]:
    
    """
    Calculates the optimal bundle of goods x and y 
    to maximize the Constant Elasticity of Substitution utility function.
    
    >>> CESdemand_calc(1/2, 2, 5, 14)
    [5.0, 0.8]
    >>> CESdemand_calc(1/4, 10, 15, 20)
    [1.067474836359107, 0.621683442427262]
    >>> CESdemand_calc(1/3, 1, 3, 6)
    [3.8038475772933684, 0.7320508075688774]
    """
    x_num = p_x**(1/(r - 1))
    y_num = p_y**(1/(r - 1))
    denom = p_x**(r/(r - 1)) + p_y**(r/(r - 1))
    
    x_star = x_num/denom*w
    y_star = y_num/denom*w
    
    return [x_star, y_star]



# Exercise D

def max_CES_xy(x_min: float, x_max: float, y_min: float, y_max: float, 
        step: float, r: float, p_x: float, p_y: float, w: float) -> List[float]:
    """
    Calculates the optimal bundle of goods x and y to maximize the 
    Constant Elasticity of Substitution utility function.
    
    >>> max_CES_xy(0, 4/5, 0, 4, 0.5, 1/2, 2, 4, 20)
    [0.5, 3.5]
    >>> max_CES_xy(0, 1/4, 0, 20, 1, 1/3, 80, 9, 100)
    [0.0, 11]
    >>> max_CES_xy(0, 8, 0, 8, 1, 1, 5, 4, 6)
    [0, 1]
    """
    x_list = np.arange(x_min, x_max, step)
    y_list = np.arange(y_min, y_max, step)
    
    max_CES = float('-inf')
    i_max = None
    j_max = None

    for i in range(len(x_list)):
        for j in range(len(y_list)):
            
            x_i = x_list[i]
            y_j = y_list[j]
            
            if p_x*x_i + p_y*y_j <= w:
                CES_ij = CESutility_in_budget(x_i, y_j, r, p_x, p_y, w)
            else:
                CES_ij = None
            if not CES_ij == None and CES_ij > max_CES:
                max_CES = CES_ij
                i_max = i
                j_max = j
                
    if (i_max is not None and j_max is not None):
        return [x_list[i_max], y_list[j_max]]
    else:
        print("No utility is higher than the initial value.")
        print("Choose different values for x and y.")
        return None



# Doc Test

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
