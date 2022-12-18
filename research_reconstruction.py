import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand
import Functions_module_beta as fn
# import Data

from Functions_module_beta import MatrixAction, SystemAction


bell_V = [fn.phiplus_V,fn.phiminus_V,fn.psiplus_V,fn.psiminus_V]
bell_C = [fn.phiplus_C,fn.phiminus_C,fn.psiplus_C,fn.psiminus_C]


y = [12,13,14,23,24,34]
angles = [sym.pi/2,0,sym.pi/4,sym.pi/4,sym.pi/4,sym.pi/2]


#Chekcs out:  phiplus

def radians(degrees):           # degrees  to radians
    rad = (sym.pi/180)*degrees
    return rad 


theta = sym.symbols('theta')
theta = 45                                          # theta in degrees, default 45 gives Bell states

phiplus_like_V = [fn.ten_states_2,fn.ten_states_5]
phiminus_like_V = [fn.ten_states_2,fn.ten_states_5]
psiplus_like_V = [fn.ten_states_3,fn.ten_states_4]
psiminus_like_V = [fn.ten_states_3,fn.ten_states_4]

phiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]                             # disturbing C slightly away from the perfect ones in bell states, like theta degrees instead of theta
phiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]
psiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]
psiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]


bell_like_V = [phiplus_like_V,phiminus_like_V,psiplus_like_V,psiminus_like_V]
bell_like_C = [phiplus_like_C,phiminus_like_C,psiplus_like_C,psiminus_like_C]

print(fn.SystemAction(psiminus_V,psiminus_C, [0,sym.pi/2,sym.pi/4,0,0,0], 7))












































