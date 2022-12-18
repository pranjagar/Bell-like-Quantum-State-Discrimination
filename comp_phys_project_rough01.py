import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random as rand
import math as m
import sympy as sym
import sympy.printing as printing
import sys
import Functions_module_beta as fn 
from Functions_module_beta import MatrixAction_old
# import Data
sys.path.append('C:/Users/pranj/Desktop/Python/Research_python')



# def Toss():
#     L = ["H","T"]
#     i =0
#     outcomes = []
#     while i < 10000:
#         a = rand.choice(L)
#         outcomes.append(a)
#         i += 1
#     H, T = outcomes.count('H'), outcomes.count('T')
#     return H/T

# def Toss_(x):
#     L = ["H","T"]
#     i =0
#     randoms = []
#     while i < 10000:
#         a = rand.random()
#         randoms.append(a)
#         i += 1
#     outcomes = ['H' if i <= x else 'T' for i in randoms ]
#     H, T = outcomes.count('H'), outcomes.count('T')
#     return [H/T, H+T]

outs = [[1,0],[0,1]]
def MatrixAction_onephoton_reduced(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    t = m.cos(phi)
    r = m.sin(phi)
    prob_t = abs(t**2)
    prob_r = abs(r**2)
    upper = 10000
    x = rand.randint(1,upper)

    if reducedstate == [1,0]:
        if x <= prob_t*upper:
            out = [1,0]
        else:
            out = [0,1]
    elif reducedstate == [0,1]:
        if x <= prob_t*upper:
            out = [0,1]
        else:
            out = [1,0]
    elif reducedstate == [0,0]:
        out = [0,0]
    return out
# print(MatrixAction([0,1],.5))

def MatrixAction_reduced_complete(reducedstate, phi= m.pi/4):                # reduced state is either [1,0] or [0,1]. phi is splitter angle
    if reducedstate == [1,0] or reducedstate == [0,1] or reducedstate == [0,0]:
        out_full = MatrixAction_onephoton_reduced(reducedstate, phi)
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
            out_full = [2,0]
        elif out_1 == [0,1] and out_2==[0,1]:
            out_full = [0,2]
        elif out_1 == [1,0] and out_2==[0,1]:
            out_full = [1,1]
        elif out_1 == [0,1] and out_2==[1,0]:
            out_full = [1,1]
    return out_full
# print(full_MatrixAction([2,0], m.pi/15))

counter,counter2,counter3,counter4,counter5,counter6,counterelse = 0,0,0,0,0,0,0
# print([counter3,counter4,counter2, counter5,counter6, (counter2+counter3+counter4)])


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
    return M34_out

splitters = [m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4,m.pi/4]  
# SystemAction(fn.ten_states_9, splitters)
    

# loop for checking probabilities
# for i in range(10):
#     x2 = MatrixAction_full('34',[1,0,1,0],splitters[0])
#     # print(f' and {x2}')
#     if x2 == [1,0,1,0]:
#         counter+=1
#     elif x2 == [0,0,2,0]:
#         counter2+=1
#     elif x2 == [2,0,0,0]:
#         counter3+=1
#     elif x2 == [0,1,0,0]:
#         counter4+=1
#     elif x2 == [1,0,0,0]:
#         counter5+=1
#     elif x2 == [1,0,0,1]:
#         counter6+=1
#     else:
#         counterelse +=1

# print([counter, counter2,counter3,counter4,counter5,counter6,counterelse])



def probabilities(inputstate_list, coeff_list, splitter_comb, n = 10000):            # n is #of trials
    numbers = [0,0,0,0,0,0,0,0,0,0]
    input_prob_list = [abs(i)**2 for i in coeff_list ] 
    for i in range(n):
        collapsed_state = rand.choices(inputstate_list, input_prob_list, k =1)[0]           # [0] coz the choices fn outputs a list but we just want the element
        counterrr.append(collapsed_state)
        # print(collapsed_state)
        out = SystemAction(collapsed_state, splitter_comb)
        j = fn.TenStateBasis.index(out)             # tells the position where we want to add +1
        numbers[j] +=1
    out_prob_list = [i/n for i in numbers] 
    return out_prob_list


















    




