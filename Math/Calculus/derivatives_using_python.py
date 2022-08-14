# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 12:56:34 2021

@author: umave
"""

import sympy as sp
from scipy.misc import derivative
import numpy as np


# x = sp.Symbol('x')
# # eq = x**4 + 2*(x**3) - x**2 + 4*x - 1
# eq = 3*x**2 +1
# yp = sp.diff(eq,x)

# print(yp)

# def syf(x):
#     # return 4*x**3 + 6*x**2 - 2*x + 4
#     return 6*x

# print(syf(2))


# from scipy.misc import derivative

# def f(x):
#     return 3*x**2 +1
#     # return x**4 + 2*x**3- x**2 + 4*x - 1
#     # return x**4 + 2*(x**3) - x**2 + 4*x - 1

# derivative(f,2)


x = sp.Symbol('x')
# eq = 3*x**2 +1
# eq = x**4 + 2*(x**3) - x**2 + 4*x - 1
# eq = (x**2+ 5*x -6)**9
eq = np.e**(5*x)

# sympy_method
def get_dydx_sym(eq,pt):
    derv =  sp.diff(eq,x)
    print('derv of {} w.r.t x is {}'.format(eq, derv))
    derv_val = eval(str(derv).replace('x',str(pt)))
    print('val of deriv {} @ x={} is {}'.format(derv,pt, derv_val))
    return derv_val

# scipy.misc.derivative method
def get_dydx_sci(eq,xx):
    new_eq = str(eq)
    new_eq = new_eq.replace('x','xx')
    def f(xx):
        expr = eval(str(new_eq))
        print(expr)
        return expr

    derv = derivative(f,xx)
    print(derv)
    return derv

get_dydx_sym(eq,2)
get_dydx_sci(eq,2)


def fg(x):
    return np.e**(5*x)

from sympy import *

x,y,z = sp.symbols('x y z')
sp.init_printing(use_unicode=True)
# expr = sp.exp(x*y*z)
# expr = sp.exp(5*x*y)
expr = x*y
print(expr)
print(sp.diff(expr,x,y))
# sp.diff(expr, x, y, y, z, z, z, z)


# =============================================================================
# 
# expr = sp.exp(x - 6).series(x, 6)
# print(expr)
# 
# expr = exp(x - 6).series(x, 6).removeO().subs(x, x - 6)
# print(expr)
# =============================================================================
