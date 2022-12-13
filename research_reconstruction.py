import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand
import scratch_research as sr
# import Data

from scratch_research import MatrixAction, SystemAction


bell_V = [sr.phiplus_V,sr.phiminus_V,sr.psiplus_V,sr.psiminus_V]
bell_C = [sr.phiplus_C,sr.phiminus_C,sr.psiplus_C,sr.psiminus_C]


y = [12,13,14,23,24,34]
angles = [sym.pi/2,0,sym.pi/4,sym.pi/4,sym.pi/4,sym.pi/2]

for i in y:
    if i == 34:
        # a = [k for k in SystemAction(bell_V[2],bell_C[2],angles, i)[1] if k != 0]
        print(SystemAction(bell_V[2],bell_C[2],angles, i))
        # z= [f'{a[1][j]}*{a[0][j]}' for j in range(len(a[0]))]
        # print(a)
print('above for state psi+')

#Chekcs out:  phiplus







