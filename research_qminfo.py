import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym


input_state = [1,0,0,1]
# Matrices = ['M34'+'M24'+'M23'-'M14','M13','M12']    #useless rn

input = "14"
# input = (input('Action of matrix : '))              #UNCOMMENT later
total_index = int(input)
first_index = int(input[0])
second_index = int(input[1])

working_state = [input_state[first_index-1], input_state[second_index-1]]

t = sym.Symbol('t'+f'_{total_index}')     # creating matching coeficients
r = sym.Symbol('r'+f'_{total_index}')

six_states_0 = n.array([0,0])          # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])


def Beam_Splitter_Action(A):             # function to give appropriate output states
    result_state = []
    full_result_state = []
    resultant_vectors = []                            # list of new_states
    basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5]
    new_states = [i for i in input_state]
    if A == [1,0]:
        Coeff_list = [0,(t),(-r),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])         # only keeping the non-zero lists (except the state_0)
                new_states[first_index-1] = basis[i][0]              # changing elts of the input state so to get the new states with 4 positons
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   # making a list of such new states as strings 
    elif A == [0,1]:
        Coeff_list = [0,(r),(t),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_index-1] = basis[i][0]              
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [0,0]:
        Coeff_list = [(1),0,0,0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_index-1] = basis[i][0]              
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [1,1]:
        Coeff_list = [0,0,0,(t**2-r**2),(n.sqrt(2)*t*r),(-n.sqrt(2)*t*r)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_index-1] = basis[i][0]              
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [2,0]:
        Coeff_list = [0,0,0,(-n.sqrt(2)*t*r),(t**2),(r**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_index-1] = basis[i][0]              
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [0,2]:
        Coeff_list = [0,0,0,(n.sqrt(2)*t*r),(r**2),(t**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_index-1] = basis[i][0]              
                new_states[second_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))  
    results = [resultant_vectors, full_result_state]
    return results  

A = Beam_Splitter_Action(working_state)

# print(Beam_Splitter_Action(working_state))
# print('result_state = ', result_state)
# print('resultant_vectors = ', resultant_vectors)
# print('full_result_state = ', full_result_state)

 
def BeamSPlitterLooped(mirror_index, input_vectors_list, coefficient_list):
    total_index = int(mirror_index)
    first_index = int(mirror_index[0])
    second_index = int(mirror_index[1])

    working_states_list = [[input_vectors_list[i][first_index-1], input_vectors_list[i][second_index-1]] for i in range(len(input_vectors_list))]
    # print(working_states_list)
    output_vector_list = [i for i in range(len(working_states_list))]
    # print(output_vector_list)
    for i in range(len(working_states_list)):
        output_vector_list[i] = (Beam_Splitter_Action(working_states_list[i])[0])
    # print(output_vector_list)

    # t = sym.Symbol('t'+f'_{total_index}')     # creating matching coeficients
    # r = sym.Symbol('r'+f'_{total_index}')    


B = []
BeamSPlitterLooped('12',A[0], B)






""" 
def Beam_Splitter_Action(A):             # function to give appropriate output states
    basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5, empty]
    if A == [1,0]:
        R = [t*six_states_1, -r*six_states_2, empty]
    elif A == [0,1]:
        R = [t*six_states_2, r*six_states_1, empty]
    elif A == [0,0]:
        R = [six_states_0, empty, empty]
    elif A == [1,1]:
        R = [(t**2-r**2)*six_states_3, n.sqrt(2)*t*r*six_states_4, -n.sqrt(2)*t*r*six_states_5]
    elif A == [2,0]:
        R = [t**2*six_states_4, r**2*six_states_5, -n.sqrt(2)*t*r*six_states_3]
    elif A == [0,2]:
        R = [t**2*six_states_5, r**2*six_states_4, n.sqrt(2)*t*r*six_states_3]
    return R
 """
