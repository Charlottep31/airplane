# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:06:29 2023

@author: ewanb
"""

import numpy as np
import math
from scipy import optimize

# Importing the aerodynamics model from aero_table
import aero_table

# Define the function to perform trim calculations
def perform_trim(V, gamma):
    # Initial guesses for the fitting
    alpha_0 = 0.0
    delta_E_0 = 0.0
    thrust_0 = 0.0  # Initial guess for thrust
    q_0 = 0.0
    theta_0 = 0.0
    uB_0 = V
    wB_0 = 0.0

    # Define the function to fit for alpha
    def alpha_func(x, a):
        return a

    # Fitting for alpha using initial guess alpha_0
    params, _ = optimize.curve_fit(alpha_func, aero_table.alpha, aero_table.CL, p0=[alpha_0])
    alpha = params[0]

    # Define the function to fit for delta_E (elevator angle)
    def delta_E_func(x, a):
        return a

    # Fitting for delta_E using initial guess delta_E_0
    params, _ = optimize.curve_fit(delta_E_func, aero_table.delta_el, aero_table.CL_el, p0=[delta_E_0])
    delta_E = params[0]

    # Calculate thrust (T) based on trim conditions
    # You can use your own model for thrust calculation

    # Calculate other state variables based on trim conditions
    # These calculations depend on your specific model

    # Return the trim results
    return alpha, delta_E, thrust, q, theta, uB, wB

# Define the values for V and gamma that you want to trim for
V_trim = 100.0  # Replace with your desired velocity
gamma_trim = 0.05  # Replace with your desired flight path angle

# Perform trim calculations for the specified V and gamma
alpha_trim, delta_E_trim, thrust_trim, q_trim, theta_trim, uB_trim, wB_trim = perform_trim(V_trim, gamma_trim)

# Print the trim results
print("Trim Results:")
print("Alpha:", alpha_trim)
print("Delta_E (Elevator Angle):", delta_E_trim)
print("Thrust:", thrust_trim)
print("q (Angular Velocity):", q_trim)
print("Theta (Pitch Angle):", theta_trim)
print("uB (Body Velocity in x-axis):", uB_trim)
print("wB (Body Velocity in z-axis):", wB_trim)
