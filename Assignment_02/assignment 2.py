# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:10:26 2025

@author: Grant & Matt
"""

def present_value(cash_flow: float, interest_rate: float, num_years: float) -> float:
    """ Return the present value of a future cash flow
    >>>present_value(100, .12, 2)
    79.72
    >>>present_value(50, .07, 3)
    40.81
    """
    
    return cash_flow / ((1 + interest_rate) ** num_years)

present_value(100, .12, 2)



def future_value(cash_flow: float, interest_rate: float, num_years: float) -> float:
    """ Return the future value of a present cash flow
    >>>future_value(100,.05,3)
    115.76
    >>>future_value(200,.07,2)
    228.98
    """
 
    return cash_flow * ((1 + interest_rate) ** num_years)

future_value(100, .05, 3)



def total_revenue(num_units: float, price: float) -> float:
    """ Return the revenue the firm would earn selling a product at a fixed price
    >>>total_revenue(10,70)
    700
    >>>total_revenue(15,25)
    375
    """
 
    return (num_units * price)

total_revenue(10, 70)



def total_cost(units_produced: float, constant: float, fixed_cost: float) -> float:
    """ Return the total cost incurred by a firm to produce a product
    >>>total_cost(64,16,25)
    65,561
    >>>total_cost(100,20,50)
    200,050
    """
    
    return constant * (units_produced ** 2) + fixed_cost

total_cost(100,20,50)



def CESutility(good_x: float, good_y: float, parameter: float) -> float:
    """ Return the value of Constant Elasticity of Substitution utility function,
    measuring the degree of satisfaction a consumer may get from two goods
    >>>CESutility(100,50,20)
    100
    >>>CESutility(50,25,10)
    50.005
    """
    
    return ((good_x ** parameter) + (good_y ** parameter)) ** (1 / parameter)

CESutility(50, 25, 10)
