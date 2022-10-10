import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym

print('----------------BEGIN-------------------------------')

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
    # output_state_display = [ ['(' +str(output_coeffs_full[i]) + ')*' +str(output_vectors_full[i])] for i in range(len(output_vectors_full))]
    output_state_display = [ ('(' +str(output_coeffs_full[i]) + ')*' +str(output_vectors_full[i])) for i in range(len(output_vectors_full))]
    
    output = [output_vectors_full, output_coeffs_full, output_state_display] 
    return output

# Notes : matrix index argument should be given as a two digit number, in ascendign order, and AS A STRING.



def latex_conversion(A):        # 'A' is a the output (a list of strings) that you wanna convert into latex code

    AA = [(i+'+') for i in A]
    B = ''.join(AA)
    C = [i for i in B]             # the strings joined and sliced letter-by-letter into a list
    # print(AA)
    # print(B)
    for i in range(len(C)):
        if C[i] == '*':
            C[i] = ''
        elif C[i] == '_':
            C[i] = '_{'
            C.insert(i+2+1,'}') 
        elif C[i] == '[':
            C[i] = '|'
        elif C[i] == ']':
            C[i] = '\\rangle'
        elif C[i] == '+' and C[i+1] == '-':
            C[i] = ''
    C.pop()                           # removing the extra last + sign
    out = ''.join(C)                     # recombining into a string
    return out




user_input_state = input("What state is input (enter as 1001 0200 etc.)? __")
user_input_matrix = int(input("Till which Beam splitter (enter input as 13, 14 etc.) ?__"))
user_input_list = [int(i) for i in user_input_state]

M12 = MatrixAction('12', [user_input_list],[1])
M13 = MatrixAction('13', M12[0], M12[1])
M14 = MatrixAction('14', M13[0], M13[1])
M23 = MatrixAction('23', M14[0], M14[1])
M24 = MatrixAction('24', M23[0], M23[1])
M34 = MatrixAction('34', M24[0], M24[1])


if user_input_matrix == 12:
    print('LATEX result = ', latex_conversion(M12[2]))
elif user_input_matrix == 13:
    print('LATEX result = ', latex_conversion(M13[2]))
elif user_input_matrix == 14:
    print('LATEX result = ', latex_conversion(M14[2]))
elif user_input_matrix == 23:
    print('LATEX result = ', latex_conversion(M23[2]))
elif user_input_matrix == 24:
    print('LATEX result = ', latex_conversion(M24[2]))
elif user_input_matrix == 34:
    print('LATEX result = ', latex_conversion(M34[2]))
else:
    print('Wrong Input!!') 





























































# print('----------------END-------------------------------')


























