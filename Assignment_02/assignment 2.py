# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:10:26 2025

@author: grant
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
