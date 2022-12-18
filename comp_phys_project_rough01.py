import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rand
import math as m
import sympy as sym
import sympy.printing as printing
import sys
sys.path.append('C:/Users/pranj/Desktop/Python/Research_python')
import Functions_module_beta as fn 
# import Data
from Functions_module_beta import MatrixAction_old

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

def Toss_(x):
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


# print(Toss_(.5))




outs = [[1,0],[0,1]]

def MatrixAction_onephoton_reduced(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    t = m.cos(phi)
    r = m.sin(phi)
    prob_t = abs(t**2)
    prob_r = abs(r**2)
    upper = 10000
    x = rand.randint(1,upper)

    if reducedstate != [1,0] and reducedstate != [0,1]:
        print('bad input. Make sure redueced states is [1,0] or [0,1]!!')
    elif reducedstate == [1,0]:
        if x <= prob_t*upper:
            out = [1,0]
        else:
            out = [0,1]
    elif reducedstate == [0,1]:
        if x <= prob_t*upper:
            out = [0,1]
        else:
            out = [1,0]
    return out

# print(MatrixAction([0,1],.5))



def MatrixAction_reduced_complete(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    if reducedstate == [1,0] or reducedstate == [0,1]:
        out = MatrixAction_onephoton_reduced(reducedstate, phi)
    elif reducedstate == [2,0]:
        out_1 = MatrixAction_onephoton_reduced([1,0],phi)
        out_2 = MatrixAction_onephoton_reduced([1,0],phi)
    elif reducedstate == [0,2]:
        out_1 = MatrixAction_onephoton_reduced([0,1],phi)
        out_2 = MatrixAction_onephoton_reduced([0,1],phi)
    elif reducedstate == [1,1]:
        out_1 = MatrixAction_onephoton_reduced([1,0],phi)
        out_2 = MatrixAction_onephoton_reduced([0,1],phi)
    
    if reducedstate == [2,0] or reducedstate == [0,2] or reducedstate == [1,1]:
        if out_1 == [1,0] and out_2==[1,0]:
            out = [2,0]
        elif out_1 == [0,1] and out_2==[0,1]:
            out = [0,2]
        elif out_1 == [1,0] and out_2==[0,1]:
            out = [1,1]
        elif out_1 == [0,1] and out_2==[1,0]:
            out = [1,1]
    return out


# print(full_MatrixAction([2,0], m.pi/15))

counter,counter2,counter3,counter4,counter5,counter6,counterelse = 0,0,0,0,0,0,0
    
# print(counter)
# print([counter3,counter4,counter2, counter5,counter6, (counter2+counter3+counter4)])
#


def MatrixAction_full(matrix_index, inputstate, phi):            # matrixindex is a string like '12' etc, inputstate is a list like [1,0,0,1]
    matrix_index_12_1 = int(matrix_index[0])
    matrix_index_12_2 = int(matrix_index[1])
    reduced_inputstate = [inputstate[matrix_index_12_1-1],inputstate[matrix_index_12_2-1]]
    reduced_out = MatrixAction_reduced_complete(reduced_inputstate, phi)
    full_out = [i for i in inputstate]
    full_out[matrix_index_12_1-1] = reduced_out[0]
    full_out[matrix_index_12_2-1] = reduced_out[1]
    return full_out


 
def SystemAction(inputstate ,splitter_comb):                    # inputstate is a vector like [1,0,0,1], splitter_comb is a list of six splitter angles
    M12_out = MatrixAction_full('12', inputstate, splitter_comb[0])
    M13_out = MatrixAction_full('13', M12_out, splitter_comb[1])
    M14_out = MatrixAction_full('14', M13_out, splitter_comb[2])
    M23_out = MatrixAction_full('23', M14_out, splitter_comb[3])
    M24_out = MatrixAction_full('24', M23_out, splitter_comb[4])
    M34_out = MatrixAction_full('34', M24_out, splitter_comb[5])
    print([M12_out,M13_out,M14_out,M23_out,M24_out,M34_out])
    return M34_out

splitters = [m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4]  
    
# loop for checking probabilities
for i in range(10):
    x2 = MatrixAction_full('34',[1,0,1,0],splitters[0])
    print(f' and {x2}')
    if x2 == [1,0,1,0]:
        counter+=1
    elif x2 == [0,0,2,0]:
        counter2+=1
    elif x2 == [2,0,0,0]:
        counter3+=1
    elif x2 == [0,1,0,0]:
        counter4+=1
    elif x2 == [1,0,0,0]:
        counter5+=1
    elif x2 == [1,0,0,1]:
        counter6+=1
    else:
        counterelse +=1

print([counter, counter2,counter3,counter4,counter5,counter6,counterelse])


""" 
counter = [0,0,0,0,0,0,0]
    
for i in range(1000):
    x2 = MatrixAction_reduced_complete([1,1],splitters[0])
    print(f' and {x2}')
    if x2 == [1,0]:
        counter[0] += 1 
    elif x2 == [0,1]:
        counter[1] += 1 
    elif x2 == [2,0]:
        counter[2] += 1 
    elif x2 == [0,2]:
        counter[3] += 1 
    elif x2 == [1,1]:
        counter[4] += 1 
    # elif x2 == [0,1]:
    #     counter[5] += 1 
    else:
        counter[6] += 1 

    
print(counter)
"""
    
    
    
    
    
    



