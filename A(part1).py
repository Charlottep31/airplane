# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:25:08 2023

@author: ewanb

# importing modules
import numpy as np
import math
from scipy import optimize

#--------------------------------------
# importing module with aerodynamics model 
# as tables of CL CM vs alpha
#    tables of CD vs CL
# and tables of CL_el and CM_el vs delta_el 
import aero_table
#--------------------------------------

#--------------------------------------
# Lift vs alpha

# Initial guesses for the fitting
# i.e., initial values of a and b
CL_0 = 0.0410
CL_alpha = 0.1

# Functional form to fit to data
def CL_a_func(x, a, b):
    return a + b * x

# Fitting (find a and b of the above function)  
# using the python module optimize from scipy.
# params contains the fitted values of a and b
# params_covariance contains a measure of the achieved 
# accuracy 
params, params_covariance = optimize.curve_fit(CL_a_func, aero_table.alpha, aero_table.CL,
        p0=[CL_0, CL_alpha])

CL_0 = params[0]
CL_alpha = params[1]
#--------------------------------------

#--------------------------------------
#Lift vs delta_elevator
CL_delta = 0.003

def CL_d_func(x, a):
    return a * x

params, params_covariance = optimize.curve_fit(CL_d_func, aero_table.delta_el, aero_table.CL_el,
        p0=[CL_delta])

CL_delta = params[0]
#--------------------------------------

#--------------------------------------
# CD vs CL
CD_0 = 0.026
CD_k = 0.045

def CD_CL_func(x, a, b):
    return a + b * x**2.0

params, params_covariance = optimize.curve_fit(CD_CL_func, aero_table.CL, aero_table.CD,
        p0=[CD_0, CD_k])

CD_0 = params[0]
CD_k = params[1]
#--------------------------------------

#--------------------------------------
# Moment vs alpha
CM_0 = 0.
CM_alpha = -0.01

def CM_a_func(x, a, b):
    return a + b * x

params, params_covariance = optimize.curve_fit(CM_a_func, aero_table.alpha, aero_table.CM,
        p0=[CM_0, CM_alpha])
CM_0 = params[0]
CM_alpha = params[1]
#--------------------------------------

#--------------------------------------
#Moment vs delta_elevator
CM_delta = -0.004

# Functional form to fit to data
def CM_delta_func(x, a):
    return a * x

# Fitting (find a of the above function) for CM_delta
params, params_covariance = optimize.curve_fit(CM_delta_func, aero_table.delta_el, aero_table.CM_el,
        p0=[CM_delta])

CM_delta = params[0]

#--------------------------------------

#--------------------------------------
# Write results on screen (check)
print(CL_0, CL_alpha, CL_delta)
print(CD_0,CD_k)
print(CM_0, CM_alpha, CM_delta)

CL = CL_0 + CL_alpha + CL_delta #find values for CL and CD
CD = CD_0 + CD_k * CL**2
CM = CM_0 + CM_alpha + CM_delta
print(CL, CD, CM)




#--------------------------------------
