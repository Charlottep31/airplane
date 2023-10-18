# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:10:45 2023

@author: ewanb
"""

gravity = 9.81
p = 1.0065
V = 100
y = 0.05
# Wing surface
Sref = 20.0  

# airfoil chord
cbar = 1.75 

# Mass of the airplane
acMass = 1300.0 

# Moment of inertia
inertia_yy = 7000


CL = 0.1427593939303899 
CD = 0.027564954661158696
CM = -0.018581848451852095

L = 0.5*p*(V**2)*Sref*CL
D = 0.5*p*(V**2)*Sref*CD
M = 0.5*p*(V**2)*Sref*cbar*CM

print(L, D, M)

 