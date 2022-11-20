import math as m
import numpy as n
import scipy as s
import sympy as sym
import pandas as p
import testing as t

# Splitter_combinations_list = p.read_csv('data.csv', sep= ',', header= None)

# Splitter_combinations_list = n.genfromtxt('data.csv', delimiter=',')
# print(Splitter_combinations_list[1])

# print(t.Big_resultant[449])

a = [[0, 0, 0, 0, 0, 0.0, 0.5, 0.5, -0.5, -0.5], [0, 0, 0, 0, 0, 0.707, 0.5, -0.5, 0.0, 0.0], [0.707, 0, 0, 0, 0, 0, 0, 0, -0.5, 0.5], [0, 0.5, 0.5, -0.5, 0.5, 0, 0, 0, 0, 0]]
b = t.compare_outputs(a)
print(b)

def Discrimination(L, a = 'p'):        # L is list of ten outputs
    nonzero_positions_list = []
    for i in range(len(L[0])):
        zeroes = 0
        nonzero_position = 0
        for j in range(len(L)):
            if L[j][i] == 0:
                zeroes +=1
            elif L[j][i] != 0:
                nonzero_position += j
            print(zeroes,nonzero_position)
        print('----------------')
        if zeroes == 3:
            nonzero_positions_list.append(nonzero_position+1)    # +1 is to have discrimination 1,2,3,4 instead of 0,1,2,3
        print(nonzero_positions_list)
        print('----------------')
    # print(nonzero_positions_list)
    discriminated_bell_states = []
    for k in range(len(nonzero_positions_list)):
        if nonzero_positions_list[k] not in discriminated_bell_states:
            discriminated_bell_states.append(nonzero_positions_list[k])
    if a == 'nonzero':
        return nonzero_positions_list
    else:
        return discriminated_bell_states


print(Discrimination(a))























































































