
from matplotlib.dates import ConciseDateConverter

import sympy as sym
import numpy as n
import random as r
import matplotlib.pyplot as plt
from pyparsing import original_text_for
import scipy.constants as const
import math as m







# phi_combinations_list = []                                                                        
# phi_values = [0, (m.pi)/2, (m.pi)/4, m.pi, -(m.pi/4)]           # these five possible selections for each splitter
# length = len(phi_values)
# for i in range(length):              # creating all possible combinations, the big phi list
#     for j in range(length):
#         for k in range(length):
#             for l in range(length):
#                 for o in range(length):
#                     for w in range(length):
#                         combination = [phi_values[i],phi_values[j],phi_values[k],phi_values[l],phi_values[o],phi_values[w]]
#                         phi_combinations_list.append(combination)




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






























