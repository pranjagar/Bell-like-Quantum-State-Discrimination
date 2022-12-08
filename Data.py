import sympy as sym
import numpy as np
import random as r
import matplotlib.pyplot as plt
from pyparsing import original_text_for
import scipy.constants as const
import math as m



phi_values = ['(m.pi)/2','(m.pi)/4', '0', '-(m.pi/4)', 'm.pi']           # these five possible selections for each splitter, input each value as string

def phi_combination_list_new(abstract = False):          # works for only 5 inputs. delete/add the extra symbols phi5 etc for other lengths 


    if abstract == False:
        phi0 = eval(phi_values[0])
        phi1 = eval(phi_values[1])
        phi2 = eval(phi_values[2])
        phi3 = eval(phi_values[3])
        phi4 = eval(phi_values[4])
    else:
        phi0 = sym.symbols(str(phi_values[0]))
        phi1 = sym.symbols(str(phi_values[1]))
        phi2 = sym.symbols(str(phi_values[2]))
        phi3 = sym.symbols(str(phi_values[3]))
        phi4 = sym.symbols(str(phi_values[4]))
    phi_values_symbols = [phi0,phi1,phi2,phi3,phi4]
    print(phi_values_symbols)

    phi_combinations_list = []                                                                        
    length = len(phi_values)
    for i in range(length):              # creating all possible combinations, the big phi list
        for j in range(length):
            for k in range(length):
                for l in range(length):
                    for o in range(length):
                        for w in range(length):
                            combination = [phi_values_symbols[i],phi_values_symbols[j],phi_values_symbols[k],phi_values_symbols[l],phi_values_symbols[o],phi_values_symbols[w]]
                            phi_combinations_list.append(combination)
    return phi_combinations_list



# print(phi_combination_list_new())



