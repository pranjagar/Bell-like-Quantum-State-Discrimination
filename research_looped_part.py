import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym

six_states_0 = n.array([0,0])                                       # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])

ten_states_0 = n.array([0,0,0,0])                                  # defining the ten possilbe output states
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



def MatrixAction(matrix_index, input_vectors, input_coeffs):
    total_index = int(matrix_index)
    first_matrix_index = int(matrix_index[0])
    second_matrix_index = int(matrix_index[1])
    t = sym.Symbol('t'+f'_{total_index}')                               # creating matching coeficients
    r = sym.Symbol('r'+f'_{total_index}')

    input_state_display = [('(' + str(input_coeffs[i]) + ')*'+ str(input_vectors[i])) for i in range(len(input_coeffs)) if input_coeffs[i] != 0 ]
    working_states = [[input_vectors[i][first_matrix_index-1], input_vectors[i][second_matrix_index-1]] for i in range(len(input_vectors))]
    
    basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5]
    new_states = [[i for i in input_vectors[j]] for j in range(len(input_vectors))]  # copy of input state list to change in into results

    output_vectors_full = []                                             # main lists of new vectors and coeffs 
    output_coeffs_full = []

    output_coeffs_display = []
    output_vectors_display = []                                           # lists for display purposes

    for k in range(len(working_states)):
        output_vectors_intermediate = []                                   # list of new_states
        output_coeff_intermediate = []

        output_vectors_intermediate_display = []                                     # intermediate lists for display prurpposes
        output_coeff_intermediate_display = []

        if working_states[k] == [1,0] and input_coeffs[k] != 0 :           # these are the equations, exculding the states whose coeffs are zero
            Coeff_list = [0,(t),(-r),0,0,0]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              # changing elts of the input state so to get the new states with 4 positons
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,1] and input_coeffs[k] != 0:
            Coeff_list = [0,(r),(t),0,0,0]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,0] and input_coeffs[k] != 0:
            Coeff_list = [(1),0,0,0,0,0]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [1,1] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(t**2-r**2),(n.sqrt(2)*t*r),(-n.sqrt(2)*t*r)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [2,0] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(-n.sqrt(2)*t*r),(t**2),(r**2)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,2] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(n.sqrt(2)*t*r),(r**2),(t**2)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])
        
        output_vectors_full.extend(output_vectors_intermediate)                # making a list of lists of output vectors
        output_coeffs_full.extend(output_coeff_intermediate)
        output_vectors_display.append(output_vectors_intermediate)                # making a list of lists of output vectors
        output_coeffs_display.append(output_coeff_intermediate)
    output_state_display = [ ['(' +str(output_coeffs_full[i]) + ')*' +str(output_vectors_full[i])] for i in range(len(output_vectors_full))]
    output = [output_vectors_full, output_coeffs_full, output_state_display] 
    return output

# Notes : matrix index argument should be given as a two digit number, in ascendign order, and AS A STRING.

A = MatrixAction('12', [[1,0,0,1]],[1])
B = MatrixAction('13', A[0], A[1])
C = MatrixAction('14', B[0], B[1])
D = MatrixAction('23', C[0], C[1])

print(D[2])










































































































