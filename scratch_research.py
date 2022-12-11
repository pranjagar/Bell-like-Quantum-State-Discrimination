
from matplotlib.dates import ConciseDateConverter

import numpy as n
import random as r
import matplotlib.pyplot as plt
from pyparsing import original_text_for
import scipy.constants as const
import math as m
import sympy as sym





phi_values = ['(m.pi)/2','(m.pi)/4', '0', '-(m.pi/4)', 'm.pi']           # these five possible selections for each splitter, input each value as string


phi0 = sym.symbols(str(phi_values[0]))
phi1 = sym.symbols(str(phi_values[1]))
phi2 = sym.symbols(str(phi_values[2]))
phi3 = sym.symbols(str(phi_values[3]))
phi4 = sym.symbols(str(phi_values[4]))

phi_values_symbols = [phi0,phi1,phi2,phi3,phi4]

# phi1,phi2,phi3,phi4,phi5 = sym.symbols('phi1,phi2,phi3,phi4,phi5')




# phi0 = 100
# phi1 = -3

# print(phi0+phi1)



mydict = [0 , "Apple", 1 , "Orange", [1,5,7,0]]

import Functions_module as fn
from Functions_module import MatrixAction
import comp_phys_project_rough01 as comp
from comp_phys_project_rough01 import create_ten_lists
# print(type(fn.TenEmptyBasis.tolist()))

V = [fn.ten_states_0]
print(f'For------0--------------')
c = sym.symbols('c')
C = [c]

index = '12'

V_new = MatrixAction(index, V,C)[0]
C_new = MatrixAction(index, V,C)[1]

# print(f'{V_new}{C_new}')
# print(create_ten_lists(V_new,C_new))


# print(float(sym.sqrt(2)))





print('------------end-------------------')























