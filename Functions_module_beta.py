import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand




def rounding(L, digits = 6):                        #L is a list of numbers, digits is jjust number ofdigits after decimal upto which we want rounding
    factor = 10**digits
    for i in range(len(L)):
        L_new = (abs(L[i])*factor)//1
        if L[i] < 0:
            L[i] = float(-1*L_new/factor)
        else:
            L[i] = float(L_new/factor)
    return L
# print(rounding([.657,55.6789]))       # Ex. use


# print(rounding([.0099]))



six_states_0 = [0,0]                                                               # defining the six possilbe output state
six_states_1 = [1,0]
six_states_2 = [0,1]
six_states_3 = [1,1]
six_states_4 = [2,0]
six_states_5 = [0,2]
empty_two = []

ten_states_0 = [0,0,0,0]                                                        # defining the ten possilbe output state
ten_states_1 = [1,1,0,0]
ten_states_2 = [1,0,1,0]
ten_states_3 = [1,0,0,1]
ten_states_4 = [0,1,1,0]
ten_states_5 = [0,1,0,1]
ten_states_6 = [0,0,1,1]
ten_states_7= [2,0,0,0]
ten_states_8 = [0,2,0,0]
ten_states_9= [0,0,2,0]
ten_states_10 = [0,0,0,2]


TenStateBasis = [ten_states_1,ten_states_2,ten_states_3,ten_states_4,ten_states_5,ten_states_6,ten_states_7,ten_states_8,ten_states_9,ten_states_10]
TenEmptyBasis = [ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0,ten_states_0]
TenZeroCoeffs = [0,0,0,0,0,0,0,0,0,0]

# defining bell states: list of vectors n coeffs
phiplus_V = [[1,0,1,0],[0,1,0,1]]
phiplus_C = [1/(sym.sqrt(2)),1/(sym.sqrt(2))]

phiminus_V = [[1,0,1,0],[0,1,0,1]]
phiminus_C = [1/(sym.sqrt(2)),-1/(sym.sqrt(2))]

psiplus_V = [[1,0,0,1],[0,1,1,0]]
psiplus_C = [1/(sym.sqrt(2)),1/(sym.sqrt(2))]

psiminus_V =[[1,0,0,1],[0,1,1,0]]
psiminus_C = [1/(sym.sqrt(2)),-1/(sym.sqrt(2))]





def create_ten_lists(V,C):
    new_V = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    new_C = [0,0,0,0,0,0,0,0,0,0]
    ten_V = TenStateBasis
    for i in range(len(V)):
        pos = TenStateBasis.index(V[i])      # findinfg position of each vector in basis list
        new_C[pos] += C[i]           # creating corresponding ten coeff list
        # new_V[pos] = V[i]            # corresponding ten basis list with oither vecotrs zero
    return [ten_V,new_C]



def ordering(L):        # L is a ket like [1,0,0,1]
    if L == [1,1,0,0]:
        position = 0
    elif L == [1,0,1,0]:
        position = 1
    elif L == [1,0,0,1]:
        position = 2
    elif L == [0,1,1,0]:
        position = 3
    elif L == [0,1,0,1]:
        position = 4
    elif L == [0,0,1,1]:
        position = 5
    elif L == [2,0,0,0]:
        position = 6
    elif L == [0,2,0,0]:
        position = 7
    elif L == [0,0,2,0]:
        position = 8
    elif L == [0,0,0,2]:
        position = 9
    return position


def MatrixAction_old(matrix_index, input_vectors, input_coeffs, phi = 3000):
    total_index = int(matrix_index)                                                              # finding the numbers 1, 2 ,12 etc so to choose appropriate elts from the full vectors etc.                            
    first_matrix_index = int(matrix_index[0]) 
    second_matrix_index = int(matrix_index[1])
    t = sym.Symbol('t'+f'_{total_index}')                                                        # creating matching coeficients
    r = sym.Symbol('r'+f'_{total_index}')


   
    if phi != 3000:
        t = m.cos(phi)
        r = m.sin(phi)
        

    input_state_display = [('(' + str(input_coeffs[i]) + ')*'+ str(input_vectors[i])) for i in range(len(input_coeffs)) if input_coeffs[i] != 0 ]          # list for displaying purpose so its easy to read. it's product of corresponding coeffs and the vectors
    working_states = [[input_vectors[i][first_matrix_index-1], input_vectors[i][second_matrix_index-1]] for i in range(len(input_vectors))]                 # 'reducing' the dimensionality of the given input states, so to apply the 2d matrices

    basis = [six_states_0,six_states_1, six_states_2,six_states_3,six_states_4,six_states_5]                 
    new_states = [[i for i in input_vectors[j]] for j in range(len(input_vectors))]                 # copy of input state list to change them into results
    output_vectors_full = []                                                                       # main lists of new vectors and coeffs 
    output_coeffs_full = []
    output_coeffs_display = []
    output_vectors_display = []                                                                     # new vectors/coeff lists for display purposes

    for k in range(len(working_states)):
        output_vectors_intermediate = []                                                             # intermediate lists of new_states, to be later dumped into the main full output lists
        output_coeff_intermediate = []

        output_vectors_intermediate_display = []                                                   # corresponding intermediate lists for display prurpposes
        output_coeff_intermediate_display = []

        if working_states[k] == [1,0] and input_coeffs[k] != 0 :                                     # these are the equations, exculding the states whose coeffs are zero
            Coeff_list = [0,(t),(-r),0,0,0]                                                         # coeff vector with appropriate values at places such that multiplication results in correct output equations
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:                                                              #making sure that zero vectors do not do not come in our calculations
                    new_states[k][first_matrix_index-1] = basis[i][0]                                # changing elts of the input state so to get the new states with 4 positons
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    output_vectors_intermediate.append(n.array(new_states[k]))                          # adding results to the intermediate lists
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,1] and input_coeffs[k] != 0:
            Coeff_list = [0,(r),(t),0,0,0]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    # fullcoeff_basis(outputbasiscoeff_numbering(new_states[k])) += Coeff_list[i]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,0] and input_coeffs[k] != 0:
            Coeff_list = [(1),0,0,0,0,0]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    # fullcoeff_basis(outputbasiscoeff_numbering(new_states[k])) += Coeff_list[i]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [1,1] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(t**2-r**2),(n.sqrt(2)*t*r),(-n.sqrt(2)*t*r)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    # fullcoeff_basis(outputbasiscoeff_numbering(new_states[k])) += Coeff_list[i]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [2,0] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(-n.sqrt(2)*t*r),(t**2),(r**2)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    # fullcoeff_basis(outputbasiscoeff_numbering(new_states[k])) += Coeff_list[i]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])

        elif working_states[k] == [0,2] and input_coeffs[k] != 0:
            Coeff_list = [0,0,0,(n.sqrt(2)*t*r),(r**2),(t**2)]
            for i in range(len((Coeff_list))):
                if Coeff_list[i] != 0:
                    new_states[k][first_matrix_index-1] = basis[i][0]              
                    new_states[k][second_matrix_index-1] = basis[i][1]
                    # fullcoeff_basis(outputbasiscoeff_numbering(new_states[k])) += Coeff_list[i]
                    output_vectors_intermediate.append(n.array(new_states[k]))
                    output_coeff_intermediate.append(input_coeffs[k]*Coeff_list[i])
        
        output_vectors_full.extend(output_vectors_intermediate)                                            # Adding the data from intermediate lists to the full output lists
        output_coeffs_full.extend(output_coeff_intermediate)
        output_vectors_display.append(output_vectors_intermediate)                                            # same but for display purposes
        output_coeffs_display.append(output_coeff_intermediate)

    for i in range(len(output_vectors_full)):                                      # Grouping algorithm: taking and vectors from the vector list andcomparing them element by element.
        for j in range(i+1,len(output_vectors_full)):                                   # it's something doesn't match then we replace that with zero vector andsimilarly the corresponding 
            z = 0                                                                   # coefficient with a dummy $$$ sign. in the final step we remove these dummy lists and signs.
            for k in range(len(output_vectors_full[i])):
                if output_vectors_full[i][k] != output_vectors_full[j][k]:
                    z = 1
            # print(f'output_coeffs_full[i],[j] : {output_coeffs_full[i]} and {output_coeffs_full[j]}')
            if z ==0 :
                if output_coeffs_full[j] != '$$$' and output_coeffs_full[i] != '$$$' :
                    output_coeffs_full[i] = output_coeffs_full[i]+output_coeffs_full[j]
                output_vectors_full[j] = n.zeros(len(output_vectors_full[j]))    
                output_coeffs_full[j] = '$$$'

    output_coeffs_full_reduced = [i for i in output_coeffs_full if i!= '$$$']
    output_vectors_full_flattened = [list(i) for i in output_vectors_full]
    output_vectors_full_reduced = [i for i in output_vectors_full_flattened if i != list(n.zeros(len(output_vectors_full[0])))]

    # print(output_coeffs_full_reduced, output_vectors_full_reduced)
    output_state_display = [ ('(' +str(output_coeffs_full_reduced[i]) + ')*' +str(output_vectors_full_reduced[i])) for i in range(len(output_vectors_full_reduced))]      # final output state for display 

    output = [output_vectors_full_reduced, output_coeffs_full_reduced, output_state_display]                                         # final list to be returned by the function, in this form so that it can be looped later on
    return output
# print(MatrixAction('12',[[1,0,0,1]],[1]))         # Eg use



def equations12(v,c, angle = False):            # v,c are vector, corresponding coeff. 
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')

    if list(v) == ten_states_1: 
        C = [c*(sym.cos(2*phi)), 0, 0, 0, 0, 0, c*sym.sin(2*phi)/sym.sqrt(2), -c*sym.sin(2*phi)/sym.sqrt(2), 0, 0]                    # TO BE CHECKED with the notes
    elif list(v) == ten_states_2: 
        C = [0, c*sym.cos(phi), 0, -c*sym.sin(phi), 0, 0, 0, 0, 0, 0]                    # TO BE CHECKED by printing and comparing with notes
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [0,0,c*sym.cos(phi),0,c*(-sym.sin(phi)),0,0,0,0,0]                    
    elif list(v) == ten_states_4: 
        C = [0,c*(sym.sin(phi)),0,c*sym.cos(phi),0,0,0,0,0,0]                    
    elif list(v) == ten_states_5: 
        C = [0, 0, c*sym.sin(phi), 0, c*sym.cos(phi), 0, 0, 0, 0, 0]                    
    elif list(v) == ten_states_6: 
        C = [0, 0, 0, 0, 0, c, 0, 0, 0, 0]                    
    elif list(v) == ten_states_7: 
        C = [-c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2, 0, 0]                    
    elif list(v) == ten_states_8: 
        C =  [c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, 0, c*sym.sin(phi)**2, c*sym.cos(phi)**2, 0, 0]                   
    elif list(v) == ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]                    
    elif list(v) == ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]   

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C

def equations13(v,c,angle = False):
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')

    if list(v) == ten_states_1: 
        C = [c*sym.cos(phi), 0, 0, -c*sym.sin(phi), 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_2: 
        C = [0, c*(sym.cos(2*phi)), 0, 0, 0, 0, c*sym.sin(2*phi)/sym.sqrt(2), 0, -c*sym.sin(2*phi)/sym.sqrt(2), 0]
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [0, 0, c*sym.cos(phi), 0, 0, -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_4: 
        C = [c*sym.sin(phi), 0, 0, c*sym.cos(phi), 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_5: 
        C = [0, 0, 0, 0, c, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_6: 
        C = [0, 0, c*sym.sin(phi), 0, 0, c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_7: 
        C =[0, -c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, c*sym.cos(phi)**2, 0, c*sym.sin(phi)**2, 0]
    elif list(v) == ten_states_8: 
        C = [0, 0, 0, 0, 0, 0, 0, c, 0, 0]
    elif list(v) == ten_states_9: 
        C = [0, c*sym.sin(2*phi)/sym.sqrt(2), 0, 0, 0, 0, c*sym.sin(phi)**2, 0, c*sym.cos(phi)**2, 0]
    elif list(v) == ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C

def equations14(v,c,angle = False):
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')
        
    if list(v) == ten_states_1: 
        C = [c*sym.cos(phi), 0, 0, 0, -c*sym.sin(phi), 0, 0, 0, 0, 0]
    elif list(v) == ten_states_2: 
        C = [0, c*sym.cos(phi), 0, 0, 0, -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == ten_states_4: 
        C = [0, 0, 0, c, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_5: 
        C = [c*sym.sin(phi), 0, 0, 0, c*sym.cos(phi), 0, 0, 0, 0, 0] 
    elif list(v) == ten_states_6: 
        C = [0, c*sym.sin(phi), 0, 0, 0, c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_7: 
        C = [0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.cos(phi)**2, 0, 0, c*sym.sin(phi)**2]
    elif list(v) == ten_states_8: 
        C = [0, 0, 0, 0, 0, 0, 0, c, 0, 0] 
    elif list(v) == ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]
    elif list(v) == ten_states_10: 
        C = [0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.sin(phi)**2, 0, 0, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C

def equations23(v,c,angle = False):
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')

    if list(v) == ten_states_1: 
        C = [c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_2: 
        C = [c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [0, 0, c, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_4: 
        C = [0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0]
    elif list(v) == ten_states_5: 
        C = [0, 0, 0, 0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_6: 
        C = [0, 0, 0, 0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == ten_states_8: 
        C = [0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2, 0]
    elif list(v) == ten_states_9: 
        C = [0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, 0, c*sym.sin(phi)**2, c*sym.cos(phi)**2, 0]
    elif list(v) == ten_states_10: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, 0, c]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C

def equations24(v,c,angle = False):
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')
    
    if list(v) == ten_states_1: 
        C = [c*sym.cos(phi), 0, -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_2: 
        C = [0, c, 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [c*sym.sin(phi), 0, c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_4: 
        C = [0, 0, 0, c*sym.cos(phi), 0, -c*sym.sin(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_5: 
        C = [0, 0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == ten_states_6: 
        C = [0, 0, 0, c*sym.sin(phi), 0, c*sym.cos(phi), 0, 0, 0, 0]
    elif list(v) == ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == ten_states_8: 
        C = [0, 0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.cos(phi)**2, 0, c*sym.sin(phi)**2]
    elif list(v) == ten_states_9: 
        C = [0, 0, 0, 0, 0, 0, 0, 0, c, 0]
    elif list(v) == ten_states_10: 
        C = [0, 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.sin(phi)**2, 0, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C

def equations34(v,c,angle = False):
    if angle is not False:
        phi = angle
    else:
        phi = sym.symbols('phi')

    if list(v) == ten_states_1: 
        C = [c, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_2: 
        C = [0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_3:                                # equations for the ten possible states input.
        C = [0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0, 0, 0]
    elif list(v) == ten_states_4: 
        C = [0, 0, 0, c*sym.cos(phi), -c*sym.sin(phi), 0, 0, 0, 0, 0]
    elif list(v) == ten_states_5: 
        C = [0, 0, 0, c*sym.sin(phi), c*sym.cos(phi), 0, 0, 0, 0, 0]
    elif list(v) == ten_states_6: 
        C = [0, 0, 0, 0, 0, c*(sym.cos(phi)**2 - sym.sin(phi)**2), 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), -1.4142135623731*c*sym.cos(phi)*sym.sin(phi)]
    elif list(v) == ten_states_7: 
        C = [0, 0, 0, 0, 0, 0, c, 0, 0, 0]
    elif list(v) == ten_states_8: 
        C = [0, 0, 0, 0, 0, 0, 0, c, 0, 0]
    elif list(v) == ten_states_9: 
        C = [0, 0, 0, 0, 0, -1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.cos(phi)**2, c*sym.sin(phi)**2]
    elif list(v) == ten_states_10: 
        C = [0, 0, 0, 0, 0, 1.4142135623731*c*sym.cos(phi)*sym.sin(phi), 0, 0, c*sym.sin(phi)**2, c*sym.cos(phi)**2]

    if angle is False:                      # returning the coeff list
        return C
    else:
        return C
    # print(equations13([1,0,1,0],.5, np.pi/8))          # Example use


def MatrixAction(V,C, index, angle12 = False):
    ten_V = create_ten_lists(V,C)[0]
    ten_C = create_ten_lists(V,C)[1]
    result_C = np.array([0,0,0,0,0,0,0,0,0,0])
    for i in range(len(ten_V)):
        if index == 12:
            result_C = result_C+ np.array(equations12(ten_V[i],ten_C[i], angle12))
        elif index == 13:
            result_C = result_C+ np.array(equations13(ten_V[i],ten_C[i], angle12))
        elif index == 14:
            result_C = result_C+ np.array(equations14(ten_V[i],ten_C[i], angle12))
        elif index == 23:
            result_C = result_C+ np.array(equations23(ten_V[i],ten_C[i], angle12))
        elif index == 24:
            result_C = result_C+ np.array(equations24(ten_V[i],ten_C[i], angle12))
        elif index == 34:
            result_C = result_C+ np.array(equations34(ten_V[i],ten_C[i], angle12))
        else:
            result_C = ['Error! Index argument has to be within the set { 12,13,14,23,24,34}']
        # print(result_C)
        # print(f'print(equations12({ten_V[i]},{ten_C[i]}))')
    Matrix_result = [list(ten_V),list(result_C)]
    return Matrix_result
        #print(MatrixAction(phiplus_V,phiplus_C, 12, np.pi/2))      #  Ex. use


def SystemAction(V,C, angles = False, stop = 34, roundoff = False):                # angles is a list of six numbers namely [angle12, angle13,..., angle34], Stop tells till which splitter output is desired (defualt 34 means whole interferometer)
    if angles is False:
        angle12,angle13,angle14,angle23,angle24,angle34 = False,False,False,False,False,False 
    else:
        angle12,angle13,angle14,angle23,angle24,angle34 = angles[0],angles[1],angles[2],angles[3],angles[4],angles[5] 

    Matrix_result12 = MatrixAction(V,C,12,angle12) 
    Matrix_result13 = MatrixAction(Matrix_result12[0],Matrix_result12[1],13,angle13) 
    Matrix_result14 = MatrixAction(Matrix_result13[0],Matrix_result13[1],14,angle14) 
    Matrix_result23 = MatrixAction(Matrix_result14[0],Matrix_result14[1],23,angle23) 
    Matrix_result24 = MatrixAction(Matrix_result23[0],Matrix_result23[1],24,angle24) 
    Matrix_result34 = MatrixAction(Matrix_result24[0],Matrix_result24[1],34,angle34) 

    y = [12,13,14,23,24,34]
    X = [Matrix_result12,Matrix_result13,Matrix_result14,Matrix_result23,Matrix_result24,Matrix_result34]
    System_result = X[y.index(stop)] 
    if roundoff is False:
        return System_result
    else:
        return [System_result[0], rounding(System_result[1])]
    # print(SystemAction([[1,0,0,1]],[1], False, 12))     # Ex use#1
    # print(SystemAction(psiminus_V,psiminus_C, [0,sym.pi/2,sym.pi/4,0,0,0], 14))     # Ex use#2



# print(SystemAction(psiplus_V,psiplus_C, [sym.pi/2,0,sym.pi/4,sym.pi/4,sym.pi/4,sym.pi/2],14))     # Ex use#3

