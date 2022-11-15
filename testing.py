import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym


six_states_0 = n.array([0,0])                                                                # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])

ten_states_0 = n.array([0,0,0,0])                                                           # defining the ten possilbe output states
ten_states_1 = n.array([1,1,0,0])
ten_states_2 = n.array([1,0,1,0])
ten_states_3 = n.array([1,0,0,1])
ten_states_4 = n.array([0,1,1,0])
ten_states_5 = n.array([0,1,0,1])
ten_states_6 = n.array([0,0,1,1])
ten_states_7= n.array([2,0,0,0])
ten_states_8 = n.array([0,2,0,0])
ten_states_9= n.array([0,0,2,0])
ten_states_10 = n.array([0,0,0,2])


six_states_0 = n.array([0,0])                                                                # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])

ten_states_0 = n.array([0,0,0,0])                                                           # defining the ten possilbe output states
ten_states_1 = n.array([1,1,0,0])
ten_states_2 = n.array([1,0,1,0])
ten_states_3 = n.array([1,0,0,1])
ten_states_4 = n.array([0,1,1,0])
ten_states_5 = n.array([0,1,0,1])
ten_states_6 = n.array([0,0,1,1])
ten_states_7= n.array([2,0,0,0])
ten_states_8 = n.array([0,2,0,0])
ten_states_9= n.array([0,0,2,0])
ten_states_10 = n.array([0,0,0,2])


def MatrixAction(matrix_index, input_vectors, input_coeffs, specific_splitter = []):
    total_index = int(matrix_index)                                                              # finding the numbers 1, 2 ,12 etc so to choose appropriate elts from the full vectors etc.                            
    first_matrix_index = int(matrix_index[0]) 
    second_matrix_index = int(matrix_index[1])
    t = sym.Symbol('t'+f'_{total_index}')                                                        # creating matching coeficients
    r = sym.Symbol('r'+f'_{total_index}')

    if specific_splitter != [] :
        t = specific_splitter[0]
        r = specific_splitter[1]

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


phi_12 = (MatrixAction('12',[[0,1,0,1],[1,0,1,0]],[1,1],[0,1]))
phi_13 = MatrixAction('13', phi_12[0],phi_12[1],[1,0])
phi_14 = MatrixAction('14', phi_13[0],phi_13[1],[1/(n.sqrt(2)), 1/(n.sqrt(2))])
phi_23 = MatrixAction('23', phi_14[0],phi_14[1],[1/(n.sqrt(2)), 1/(n.sqrt(2))])
phi_24 = MatrixAction('24', phi_23[0],phi_23[1],[1/(n.sqrt(2)), 1/(n.sqrt(2))])
phi_34 = MatrixAction('34', phi_24[0],phi_24[1],[0,1])


# #omdify grouping algo to accomodate closeby irrationals
# print(phi_12)
# print(phi_13)
# print(phi_14)
# print(phi_23)
# print(phi_24)
# print(phi_34)


def BellOutput(InputBellState, V_or_C_or_Out = 'Out', specific_splitters = []):              #input one one of the four bell states as string, second input is what is needed : list of coeffs or list of vectors or full output as a string, input a list of six lists of t and r respectively for splitters 12,13,..34 respectively. 
    if InputBellState == 'phiplus':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/(n.sqrt(2)), 1/(n.sqrt(2))]
    elif InputBellState == 'phiminus':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/(n.sqrt(2)), -1/(n.sqrt(2))]
    elif InputBellState == 'psiplus':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/(n.sqrt(2)), 1/(n.sqrt(2))]
    elif InputBellState == 'psiminus':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/(n.sqrt(2)), -1/(n.sqrt(2))]
    else:
        print('[(00+11) = phiplus, (00-11) = phiminus, (01+10) = psiplus, (10-10) = psiminus] \n V : vector list, C: Coeffs list, Out: full result (string)')

    # user_input_matrix = int(input("Till which Beam splitter (enter input as 13, 14 etc.) ? "))
    user_input_matrix = 34                                       # uncomment to avoid imput: matrix  = 34 

    M12 = MatrixAction('12', user_input_list,user_input_coeffs, specific_splitters[0])                                         # making use of the beam splitter function, looping it over and over
    M13 = MatrixAction('13', M12[0], M12[1],specific_splitters[1])
    M14 = MatrixAction('14', M13[0], M13[1],specific_splitters[2])
    M23 = MatrixAction('23', M14[0], M14[1],specific_splitters[3])
    M24 = MatrixAction('24', M23[0], M23[1],specific_splitters[4])
    M34 = MatrixAction('34', M24[0], M24[1],specific_splitters[5])

    if user_input_matrix == 12:                                                            #this is just so the output matches the corresponding input
        output_vectors = (M12[0])
        output_coefficients = (M12[1])
        output_display = (M12[2])
    elif user_input_matrix == 13:
        output_vectors = (M13[0])
        output_coefficients = (M13[1])
        output_display = (M13[2])
    elif user_input_matrix == 14:
        output_vectors = (M14[0])
        output_coefficients = (M14[1])
        output_display = (M14[2])
    elif user_input_matrix == 23:
        output_vectors = (M23[0])
        output_coefficients = (M23[1])
        output_display = (M23[2])
    elif user_input_matrix == 24:
        output_vectors = (M24[0])
        output_coefficients = (M24[1])
        output_display = (M24[2])
    elif user_input_matrix == 34:
        output_vectors = (M34[0])
        output_coefficients = (M34[1])
        output_display = (M34[2])

    if V_or_C_or_Out == 'V':
        return output_vectors
    elif V_or_C_or_Out == 'C':
        return output_coefficients
    elif V_or_C_or_Out == 'Out':
        return output_display

choice159_splittes = [[0,1],[1,0],[1/(n.sqrt(2)),1/(n.sqrt(2))],[1/(n.sqrt(2)),1/(n.sqrt(2))],[1/(n.sqrt(2)),1/(n.sqrt(2))],[0,1]]
""" 
choice401_splittes = [[1,0],[1,0],[1/(n.sqrt(2)),1/(n.sqrt(2))],[1/(n.sqrt(2)),1/(n.sqrt(2))],[1,0],[1/(n.sqrt(2)),1/(n.sqrt(2))]]
choice0_splittes = [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]
choice1_splittes = [[0,1],[0,1],[0,1],[0,1],[0,1],[1/(n.sqrt(2)),1/(n.sqrt(2))]]

# print(BellOutput('psiplus','Out', choice159_splittes))
print(BellOutput('psiplus','Out', choice1_splittes))
# correct 0 : [[0,0,-(1/1.414),0,-(1/1.414),0,0,0,0,0], we get ['(-0.7071067811865475)*[1, 0, 0, 1]', '(-0.7071067811865475)*[0, 1, 1, 0]']
# correct 1 : [0,1/1.414,0,0,0,-(1/1.414),0,0,0,0]
 """

def Dummy(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34):
    # f below is a trial
    f= t12+r12+t13+r13+t14+r14+t23+r23+t24+r24+t34+r34
    return f 

# choices = [0,.5]#, 1/(n.sqrt(2))] #, -1/(n.sqrt(2)),-1]


choices = [[0,1],[ 1,0],[1/(n.sqrt(2)), 1/(n.sqrt(2))]]



count = 0
Splitter_choices_list = []
for i in range(len(choices)):
    M12 = choices[i]
    for j in range(len(choices)):
        M13 = choices[j]
        for k in range(len(choices)):
            M14 = choices[k]
            for l in range(len(choices)):
                M23 = choices[l]
                for m in range(len(choices)):
                    M24 = choices[m]
                    for n in range(len(choices)):
                        M34 = choices[n]
                        Splitter_choices_list.append([M12,M13,M14,M23,M24,M34])

# print(len(Big_splitters_list[0]))

# for i in range(len(Splitter_choices_list)):
# print(Splitter_choices_list[159])
print(BellOutput('psiplus','Out', choice159_splittes))












