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
import Data


""" 

def equations12(v,c, angle = False):            # v,c are vector, corresponding coeff. 
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            c_phi,s_phi = m.cos(angle),m.sin(angle)
        elif type(angle) is str:
            print('please input a number for angle!!')
    elif angle is False:
        phi, c_phi, s_phi = sym.symbols('phi, cos(phi), sin(phi)')

    if list(v) == fn.ten_states_1: 
        C = [c*(-r12**2 + t12**2), 0, 0, 0, 0, 0, 1.4142135623731*c*r12*t12, -1.4142135623731*c*r12*t12, 0, 0]                    # TO BE CHECKED with the notes
    elif list(v) == fn.ten_states_2: 
        C = [0, c*t12, 0, -c*r12, 0, 0, 0, 0, 0, 0]                    # TO BE CHECKED by printing and comparing with notes
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [0,0,c*c_phi,0,c*(-s_phi),0,0,0,0,0]                    
    elif list(v) == fn.ten_states_4: 
        C = [0,c*(r12),0,c*t12,0,0,0,0,0,0]                    
    elif list(v) == fn.ten_states_5: 
        C = [0, 0, c*r12, 0, c*t12, 0, 0, 0, 0, 0]                    
    elif list(v) == fn.ten_states_6: 
        C = [0, 0, 0, 0, 0, c, 0, 0, 0, 0]                    
    elif list(v) == fn.ten_states_7: 
        C = [-1.4142135623731*c*r12*t12, 0, 0, 0, 0, 0, c*t12**2, c*r12**2, 0, 0]                    
    elif list(v) == fn.ten_states_8: 
        C =  [1.4142135623731*c*r12*t12, 0, 0, 0, 0, 0, c*r12**2, c*t12**2, 0, 0]                   
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]                    
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]                    

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)
    # print(equations12([1,0,0,1],.5,np.pi/2))          # Example use
    
"""


def Toss():
    L = ["H","T"]
    i =0
    outcomes = []
    while i < 10000:
        a = rand.choice(L)
        outcomes.append(a)
        i += 1
    H, T = outcomes.count('H'), outcomes.count('T')
    return H/T
# trial = [i for i in range(100)]
# result = [Toss() for i in trial]

def Toss(x):
    L = ["H","T"]
    i =0
    randoms = []
    while i < 10000:
        a = rand.random()
        randoms.append(a)
        i += 1
    outcomes = ['H' if i <= x else 'T' for i in randoms ]
    H, T = outcomes.count('H'), outcomes.count('T')
    return [H/T, H+T]

def create_ten_lists(V,C):
    new_V = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    new_C = [0,0,0,0,0,0,0,0,0,0]
    ten_V = fn.TenStateBasis
    for i in range(len(V)):
        pos = fn.TenStateBasis.index(V[i])      # findinfg position of each vector in basis list
        new_C[pos] += C[i]           # creating corresponding ten coeff list
        new_V[pos] = V[i]            # corresponding ten basis list with oither vecotrs zero
    return [new_V,new_C]


t12,r12 = sym.symbols('t12,r12')
phi = sym.symbols('phi')

# calling angle phi for python typing purposes

def equations12(v,c, angle = False):            # v,c are vector, corresponding coeff. 
    if angle is not False:
        if type(angle) is float or type(angle) is int:
            phi = angle
        elif type(angle) is str:
            print('please input a number for angle!!')
    else:
        phi = sym.symbols('phi')

    if list(v) == fn.ten_states_1: 
        C = [c*(sym.cos(2*phi)), 0, 0, 0, 0, 0, c*sym.sin(2*phi)/sym.sqrt(2), -c*sym.sin(2*phi)/sym.sqrt(2), 0, 0]                    # TO BE CHECKED with the notes
    elif list(v) == fn.ten_states_2: 
        C = [0, c*sym.cos(phi), 0, -c*sym.cos(phi), 0, 0, 0, 0, 0, 0]                    # TO BE CHECKED by printing and comparing with notes
    elif list(v) == fn.ten_states_3:                                # equations for the ten possible states input.
        C = [0,0,c*sym.cos(phi),0,c*(-sym.sin(phi)),0,0,0,0,0]                    
    elif list(v) == fn.ten_states_4: 
        C = [0,c*(sym.cos(phi)),0,c*sym.cos(phi),0,0,0,0,0,0]                    
    elif list(v) == fn.ten_states_5: 
        C = [0, 0, c*sym.cos(phi), 0, c*sym.cos(phi), 0, 0, 0, 0, 0]                    
    elif list(v) == fn.ten_states_6: 
        C = [0, 0, 0, 0, 0, c, 0, 0, 0, 0]                    
    elif list(v) == fn.ten_states_7: 
        C = [-c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2, 0, 0]                    
    elif list(v) == fn.ten_states_8: 
        C =  [c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, 0, c*sym.cos(phi)**2, c*sym.cos(phi)**2, 0, 0]                   
    elif list(v) == fn.ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]                    
    elif list(v) == fn.ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]                    

    if angle is False:                      # returning the coeff list
        return C
    else:
        return fn.rounding(C)
    # print(equations12([1,1,0,0],.5))          # Example use
    


def Matrix12(V,C,phi = False):
    ten_V = create_ten_lists(V,C)[0]
    ten_C = create_ten_lists(V,C)[1]
    result_C = np.array([0,0,0,0,0,0,0,0,0,0])
    for i in range(len(ten_V)):
        print(equations12(ten_V[i],ten_C[i], phi))
        result_C = result_C+ np.array(equations12(ten_V[i],ten_C[i], phi))
        # print(f'print(equations12({ten_V[i]},{ten_C[i]}))')
    return list(result_C)

belltest_V = [[1,0,0,1],[0,1,1,0]]
belltest_C = [1/(m.sqrt(2)),1/(m.sqrt(2))]


# print(Matrix12(belltest_V,belltest_C))

""" 
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))
print(equations12([1, 0, 0, 1],0.7071067811865475))
print(equations12([0, 1, 1, 0],0.7071067811865475))
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))
print(equations12([0, 0, 0, 0],0))

 """
 































