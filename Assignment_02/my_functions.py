# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 11:10:26 2025

@author: grant
"""

def future_value(cash_flow: float, interest_rate: float, num_years: float) -> float:
    """ Return the present value of a future cash flow
    >>>future_value(1000, 12, 2)
    5.9172
    >>>future_value(500, 4, 3)
    4.0
    """
    
    return cash_flow / ((1 + interest_rate) ** num_years)

future_value(500, 4, 3)
