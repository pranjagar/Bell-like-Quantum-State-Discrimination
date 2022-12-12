

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rand
import math as m
import sympy as sym
import sympy.printing as printing
import sys
sys.path.append('C:/Users/pranj/Desktop/Python/Research_python')
import Functions_module_new as fn 
# import Data
from Functions_module_new import MatrixAction












ProcessLookupError(fn.ten_states_0)




 


def equations14(v,c,angle = False):
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            phi = angle
        elif type(angle) is str:
            print('please input a number for angle!!')
    else:
        phi = sym.symbols('phi')
    if list(v) == fn.ten_states_1: 
        C = [c*sym.cos(phi), 0, 0, 0, -c*sym.sin(phi), 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_2: 
        C = [0, c*sym.cos(phi), 0, 0, 0, -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == fn.ten_states_4: 
        C = [0, 0, 0, c, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_5: 
        C = [c*sym.sin(phi), 0, 0, 0, c*sym.cos(phi), 0, 0, 0, 0, 0] 
    elif list(v) == fn.ten_states_6: 
        C = [0, c*sym.sin(phi), 0, 0, 0, c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_7: 
        C = [0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.cos(phi)**2, 0, 0, c*sym.sin(phi)**2]
    elif list(v) == fn.ten_states_8: 
        C = [0, 0, 0, 0, 0, 0, 0, c, 0, 0] 
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.sin(phi)**2, 0, 0, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)

def equations23(v,c,angle = False):
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            phi = angle
        elif type(angle) is str:
            print('please input a number for angle!!')
    else:
        phi = sym.symbols('phi')
    if list(v) == fn.ten_states_1: 
        C = [c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_2: 
        C = [c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [0, 0, c, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_4: 
        C = [0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0]
    elif list(v) == fn.ten_states_5: 
        C = [0, 0, 0, 0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_6: 
        C = [0, 0, 0, 0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == fn.ten_states_8: 
        C = [0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2, 0]
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.sin(phi)**2, c*sym.cos(phi)**2, 0]
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)

def equations24(v,c,angle = False):
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            phi = angle
        elif type(angle) is str:
            print('please input a number for angle!!')
    else:
        phi = sym.symbols('phi')
    if list(v) == fn.ten_states_1: 
        C = [c*sym.cos(phi), 0, -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_2: 
        C = [0, c, 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [c*sym.sin(phi), 0, c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_4: 
        C = [0, 0, 0, c*sym.cos(phi), 0, -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_5: 
        C = [0, 0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == fn.ten_states_6: 
        C = [0, 0, 0, c*sym.sin(phi), 0, c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == fn.ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == fn.ten_states_8: 
        C = [0, 0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.cos(phi)**2, 0, c*sym.sin(phi)**2]
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.sin(phi)**2, 0, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)

def equations34(v,c,angle = False):
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            phi = angle
        elif type(angle) is str:
            print('please input a number for angle!!')
    else:
        phi = sym.symbols('phi')
    if list(v) == fn.ten_states_1: 
        C = [c, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_2: 
        C = [0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_4: 
        C = [0, 0, 0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_5: 
        C = [0, 0, 0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0]
    elif list(v) == fn.ten_states_6: 
        C = [0, 0, 0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == fn.ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == fn.ten_states_8: 
        C = [0, 0, 0, 0, 0, 0, 0, c, 0, 0]
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2]
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.sin(phi)**2, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)










