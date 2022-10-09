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



def MatrixAction(matrix_index, input_vectors, input_coefficients):
    total_index = int(matrix_index)
    first_matrix_index = int(matrix_index[0])
    second_matrix_index = int(matrix_index[1])
    t = sym.Symbol('t'+f'_{total_index}')                               # creating matching coeficients
    r = sym.Symbol('r'+f'_{total_index}')

    input_state = [('(' + str(input_coeff_list[i]) + ')*'+ str(input_vector_list[i])) for i in range(len(input_coeff_list)) if input_coeff_list[i] != 0 ]    # typesets the result, ignores zero coefficient terms
    working_state_list = [[input_vector_list[i][first_matrix_index-1], input_vector_list[i][second_matrix_index-1]] for i in range(len(input_vector_list))]


















































































































