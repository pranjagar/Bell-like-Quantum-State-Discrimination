import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym




six_states_0 = n.array([0,0])          # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])

ten_states_0 = n.array([0,0,0,0])          # defining the ten possilbe output states
ten_states_1 = n.array([1,1,0 ,0 ])
ten_states_2 = n.array([1,0,1,0])
ten_states_3 = n.array([1,0,0,1])
ten_states_4 = n.array([0,1,1,0])
ten_states_5 = n.array([0,1,0,1])
ten_states_6 = n.array([0,0,1,1])
ten_states_7= n.array([2,0,0,0])
ten_states_8 = n.array([0,2,0,0])
ten_states_9= n.array([0,0,2,0])
ten_states_10 = n.array([0,0,0,2])

input_state_list = [[1,0,0,1],[1,0,1,0], [1,1,0,0]]          # input and output pure state vectors be lists
input_coeff_list = [1]                                       # list of coeffcients t and r attached to the input states


matrix_index = "14"                                          # matrices be inputted according to choice
# input = (input('Action of matrix : '))                      #UNCOMMENT later
total_index = int(matrix_index)
first_matrix_index = int(matrix_index[0])
second_matrix_index = int(matrix_index[1])

working_state_list = [[input_state_list[i][first_matrix_index-1], input_state_list[i][second_matrix_index-1]] for i in range(len(input_state_list))]
# working "2 dimesnional" states of every input  

t = sym.Symbol('t'+f'_{total_index}')     # creating matching coeficients
r = sym.Symbol('r'+f'_{total_index}')


# Now applying this beams splitter on the inputs

resultant_state_1 = []
resultant_state = []
# full_result_state = []
output_vectors_list_full = []                           # list of new_states
basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5]
new_states = [[i for i in input_state_list[j]] for j in range(len(input_state_list))]  # copy of input state list to change in into results

for k in range(len(working_state_list)):
    output_vectors_list_intermediate = []                           # list of new_states
    if working_state_list[k] == [1,0]:
        Coeff_list = [0,(t),(-r),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])         # only keeping the non-zero lists (except the state_0)
                new_states[k][first_matrix_index-1] = basis[i][0]              # changing elts of the input state so to get the new states with 4 positons
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   # making a list of such new states as strings 
    elif working_state_list[k] == [0,1]:
        Coeff_list = [0,(r),(t),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])
                new_states[k][first_matrix_index-1] = basis[i][0]              
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif working_state_list[k] == [0,0]:
        Coeff_list = [(1),0,0,0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])
                new_states[k][first_matrix_index-1] = basis[i][0]              
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif working_state_list[k] == [1,1]:
        Coeff_list = [0,0,0,(t**2-r**2),(n.sqrt(2)*t*r),(-n.sqrt(2)*t*r)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])
                new_states[k][first_matrix_index-1] = basis[i][0]              
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif working_state_list[k] == [2,0]:
        Coeff_list = [0,0,0,(-n.sqrt(2)*t*r),(t**2),(r**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])
                new_states[k][first_matrix_index-1] = basis[i][0]              
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif working_state_list[k] == [0,2]:
        Coeff_list = [0,0,0,(n.sqrt(2)*t*r),(r**2),(t**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                resultant_state.append(Coeff_list[i]*basis[i])
                new_states[k][first_matrix_index-1] = basis[i][0]              
                new_states[k][second_matrix_index-1] = basis[i][1]
                output_vectors_list_intermediate.append(n.array(new_states[k]))
                # full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))  
    output_vectors_list_full.append((output_vectors_list_intermediate))            # making a list of lists of output vectors
    # results = [output_vectors_list, full_result_state, Coeff_list]
print('output_vectors_list_intermediate :' , output_vectors_list_intermediate)
print('output_vectors_list_full :' , output_vectors_list_full)
# print(resultant_state)



























""" 

def Beam_Splitter_Action(A):             # function to give appropriate output states
    result_state = []
    full_result_state = []
    resultant_vectors = []                            # list of new_states
    basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5]
    new_states = [i for i in input_state_list]
    if A == [1,0]:
        Coeff_list = [0,(t),(-r),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])         # only keeping the non-zero lists (except the state_0)
                new_states[first_matrix_index-1] = basis[i][0]              # changing elts of the input state so to get the new states with 4 positons
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   # making a list of such new states as strings 
    elif A == [0,1]:
        Coeff_list = [0,(r),(t),0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_matrix_index-1] = basis[i][0]              
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [0,0]:
        Coeff_list = [(1),0,0,0,0,0]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_matrix_index-1] = basis[i][0]              
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [1,1]:
        Coeff_list = [0,0,0,(t**2-r**2),(n.sqrt(2)*t*r),(-n.sqrt(2)*t*r)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_matrix_index-1] = basis[i][0]              
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [2,0]:
        Coeff_list = [0,0,0,(-n.sqrt(2)*t*r),(t**2),(r**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_matrix_index-1] = basis[i][0]              
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))                   
    elif A == [0,2]:
        Coeff_list = [0,0,0,(n.sqrt(2)*t*r),(r**2),(t**2)]
        for i in range(len((Coeff_list))):
            if Coeff_list[i] != 0:
                result_state.append(Coeff_list[i]*basis[i])
                new_states[first_matrix_index-1] = basis[i][0]              
                new_states[second_matrix_index-1] = basis[i][1]
                resultant_vectors.append(n.array(new_states))
                full_result_state.append('(' +str(Coeff_list[i]) + ')*' +str(n.array(new_states)))  
    results = [resultant_vectors, full_result_state, Coeff_list]
    return results   """

# A = Beam_Splitter_Action(working_state)

# print(Beam_Splitter_Action(working_state))
# print('result_state = ', result_state)
# print('resultant_vectors = ', resultant_vectors)
# print('full_result_state = ', full_result_state)
""" 
 
def BeamSPlitterLooped(mirror_index, input_vectors_list, coefficient_list):
    total_index = int(mirror_index)
    first_index = int(mirror_index[0])
    second_index = int(mirror_index[1])

    working_states_list = [[input_vectors_list[i][first_index-1], input_vectors_list[i][second_index-1]] for i in range(len(input_vectors_list))]
    # print(working_states_list)
    output_vector_list = [i for i in range(len(working_states_list))]
    # print(output_vector_list)
    first_coeff_list = Beam_Splitter_Action(working_states_list[i])[2]

    second_coeff_list = []
    # adding a 'for' loop to add the new coeff lists based on the six if-statements



    for i in range(len(working_states_list)):
        output_vector_list[i] = (Beam_Splitter_Action(working_states_list[i])[0])
    print(output_vector_list)

     

    # t = sym.Symbol('t'+f'_{total_index}')     # creating matching coeficients
    # r = sym.Symbol('r'+f'_{total_index}')    


B = []
(BeamSPlitterLooped('12',A[0], B))



 """

