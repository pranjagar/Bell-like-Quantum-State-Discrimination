import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand
import Functions_module as fn
import Data

from Functions_module import MatrixAction, SystemAction


bell_V = [fn.phiplus_V,fn.phiminus_V,fn.psiplus_V,fn.psiminus_V]
bell_C = [fn.phiplus_C,fn.phiminus_C,fn.psiplus_C,fn.psiminus_C]


y = [12,13,14,23,24,34]
angles = [sym.pi/2,0,sym.pi/4,sym.pi/4,sym.pi/4,sym.pi/2]

for i in range(len(bell_C)):
    a = (SystemAction(bell_V[i],bell_C[i],angles, 34))
    # z= [f'{a[1][j]}*{a[0][j]}' for j in range(len(a[0]))]
    print(a[1])
    print('')

#Chekcs out:  phiplus







