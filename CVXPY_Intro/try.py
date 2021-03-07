# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 09:30:30 2021

@author: Lokesh
"""

import numpy as np
import cvxpy as cp

if __name__ == "__main__":

    
    capacity = np.array([350, 600]) # 1x2
    demand = np.array([325, 300, 275]) #1x3
    distance = np.array([[2.5, 1.7, 1.8], #2x3
                [2.5, 1.8, 1.4]])
    freight = 90
    cost = freight*distance/1000 #2x3
    
    #------ set up LP data --------
    C = cost
    d = demand
    s = capacity
    
    #---- matrix formulation ----
    
    ei = np.ones(s.shape)
    ej = np.ones(d.shape)
    
    X = cp.Variable(C.shape,"X")
    prob = cp.Problem(
        cp.Minimize(cp.trace(C.T@X)),
        [X.T@ei >= d, 
         X@ej <= s, 
         X>=0])
    prob.solve(verbose=True)
    print("status:",prob.status)
    print("objective:",prob.value)
    print("levels:",X.value)
    