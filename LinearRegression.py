# -*- coding: utf-8 -*-

import numpy as np

def __init__():
    pass

def desc():
    print('''         Model Name: Linear Regression.
          
             Goal: Learn a global (1+d) by 1 vector Ws.
             
             Mathematics: f(Xs,Ws) = phi(Xs) * Ws.
             
             Method: pseudo-inverse.
             
             Procedure: 1. Upon calling of train method, Xs is converted to design matrix phi;
                        2. Weight Ws is found by using psudo-inverse of phi.''')
    
