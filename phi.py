import numpy as n
import pandas as pd
import dummy as D
import math as m
import sympy as sym

# Dummy = np.loadtxt('dummy.csv', delimiter=',', dtype=int)
# # Dummy = pd.read_csv('dummy.csv', delimiter=',',dtype=None)
# print(Dummy)


# List= []
# D.Data(List)


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

TenStateBasis = [ten_states_1,ten_states_2,ten_states_3,ten_states_4,ten_states_5,ten_states_6,ten_states_7,ten_states_8,ten_states_9,ten_states_10]
TenZeroCoeffs = [0,0,0,0,0,0,0,0,0,0]




def MatrixAction(matrix_index, input_vectors, input_coeffs, phi = 3000):
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



    

# phi_12 = (MatrixAction('12',[[0,1,0,1],[1,0,1,0]],[1,1],(m.pi)/2))
phi_12 = (MatrixAction('12',[[0,1,0,1],[1,0,1,0]],[1,1]))
# print(phi_12)




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




def BellOutput(InputBellState, Coeffs_or_Out = 'Out', phi_list =False, roundoff = 'no'):   #for rounding, make sure to include "no" within argument and yes in the if statement
    if phi_list == False:
        phi_list = [3000,3000,3000,3000,3000,3000]              #input one one of the four bell states as string, second input is what is needed : list of coeffs or list of vectors or full output as a string, input a list of six lists of t and r respectively for splitters 12,13,..34 respectively. Choose 'C' for coeff lists, 'Out' for full state output
    if InputBellState == 'phiplus':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/n.sqrt(2), 1/n.sqrt(2)]
    elif InputBellState == 'phiminus':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/n.sqrt(2), -1/n.sqrt(2)]
    elif InputBellState == 'psiplus':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/n.sqrt(2), 1/n.sqrt(2)]
    elif InputBellState == 'psiminus':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/n.sqrt(2), -1/n.sqrt(2)]
    else:
        print('[(00+11) = phiplus, (00-11) = phiminus, (01+10) = psiplus, (10-10) = psiminus] \n V : vector list, C: Coeffs list, Out: full result (string)')

    # user_input_matrix = int(input("Till which Beam splitter (enter input as 13, 14 etc.) ? "))
    user_input_matrix = 34                                       # uncomment to avoid imput: matrix  = 34 
    M12 = MatrixAction('12', user_input_list, user_input_coeffs , phi_list[0])                                         # making use of the beam splitter function, looping it over and over
    M13 = MatrixAction('13', M12[0], M12[1], phi_list[1])
    M14 = MatrixAction('14', M13[0], M13[1], phi_list[2])
    M23 = MatrixAction('23', M14[0], M14[1], phi_list[3])
    M24 = MatrixAction('24', M23[0], M23[1], phi_list[4])
    M34 = MatrixAction('34', M24[0], M24[1], phi_list[5])

    if user_input_matrix == 12:                                                            #this is just so the output matches the corresponding input
        nonzeroVectors = M12[0]
        nonzeroCoefficients = (M12[1])
    elif user_input_matrix == 13:
        nonzeroVectors = M13[0]
        nonzeroCoefficients = (M13[1])
    elif user_input_matrix == 14:
        nonzeroVectors = M14[0]
        nonzeroCoefficients = (M14[1])
    elif user_input_matrix == 23:
        nonzeroVectors = M23[0]
        nonzeroCoefficients = (M23[1])
    elif user_input_matrix == 24:
        nonzeroVectors = M24[0]
        nonzeroCoefficients = (M24[1])
    elif user_input_matrix == 34:
        nonzeroVectors = M34[0]
        nonzeroCoefficients = (M34[1])

    if roundoff == 'roundoff':          
        roundoffs = [.5,.707,1,0,.353]
        for j in roundoffs:
            for i in range(len(nonzeroCoefficients)):              # removing the .499999, .70734.. etc. roundoff errors
                # if abs(nonzeroCoefficients[i]) < 1e-12:
                #     nonzeroCoefficients[i] = 0
                if abs((abs(nonzeroCoefficients[i])-j)) < .002:
                    if nonzeroCoefficients[i] > 0:
                        nonzeroCoefficients[i] = j
                    elif nonzeroCoefficients[i] < 0:
                        nonzeroCoefficients[i] = -j
    
    output_coeffs = [i for i in TenZeroCoeffs]         # ten zero list
    
    for i in range(len(nonzeroVectors)):
        a = ordering(nonzeroVectors[i])
        output_coeffs[a] = nonzeroCoefficients[i]

    # print(nonzeroCoefficients,nonzeroVectors,output_coeffs)

    output_display = [str(output_coeffs[i])+'*'+str(TenStateBasis[i]) for i in range(10) if output_coeffs[i] != 0 ]

    if Coeffs_or_Out == 'C':
        return output_coeffs
    elif Coeffs_or_Out == 'V':
        return nonzeroVectors
    elif Coeffs_or_Out == 'Out':
        return output_display

a = [0,0,0,0,0,0]
# print(BellOutput('phiplus', 'C', a, 'yes'))


def four_outputs(phi_vals_list, roundoff ='no'):                                     # splitters is a list of 6 elements for the six splitters. Order of output is phi+,phi-,psi+,psi-        
        if roundoff == 'roundoff':
            c = 'roundoff'
        elif roundoff == 'no':
            c = 'no'
        Four_resultant_Bellstates = []
        Four_resultant_Bellstates.append(BellOutput('phiplus','C', phi_vals_list, c))    # adding to create a list of the four resultant bell states, for the ith choice of the splitter configuration 
        Four_resultant_Bellstates.append(BellOutput('phiminus','C', phi_vals_list,c))
        Four_resultant_Bellstates.append(BellOutput('psiplus','C', phi_vals_list, c))
        Four_resultant_Bellstates.append(BellOutput('psiminus','C', phi_vals_list, c))
        return Four_resultant_Bellstates

# print(four_outputs(Splitter_combinations_list[159]))



phi_combinations_list = []                                                                        
phi_values = [0, (m.pi)/2, (m.pi)/4, -(m.pi)/2, -(m.pi/4)]
length = len(phi_values)
for i in range(length):
    for j in range(length):
        for k in range(length):
            for l in range(length):
                for o in range(length):
                    for w in range(length):
                        combination = [phi_values[i],phi_values[j],phi_values[k],phi_values[l],phi_values[o],phi_values[w]]
                        phi_combinations_list.append(combination)
                      



Big_resultant = [] 
for i in range(len(phi_combinations_list)):            # looping over all possible splitter combinations and appedning to make a big list of all possible four bell state outputs
    Big_resultant.append(four_outputs(phi_combinations_list[i], 'roundoff'))

print(Big_resultant)  # BIG LIST



def Discrimination(L):        # L is list of ten outputs
    nonzero_positions_list = []
    for i in range(len(L[0])):
        zeroes = 0
        nonzero_position = 0
        for j in range(len(L)):
            if L[j][i] == 0:
                zeroes +=1
            elif L[j][i] != 0:
                nonzero_position += j
        if zeroes == 3:
            nonzero_positions_list.append(nonzero_position+1)    # +1 is to have discrimination 1,2,3,4 instead of 0,1,2,3
    discriminated_bell_states = []
    for k in range(len(nonzero_positions_list)):
        if nonzero_positions_list[k] not in discriminated_bell_states:
            discriminated_bell_states.append(nonzero_positions_list[k])
    return discriminated_bell_states


Big_discrimination_list = []

for i in range(len(Big_resultant)):
    Big_discrimination_list.append(Discrimination(Big_resultant[i]))        # A big list of discriminations like [1,2,3] indiccatiing bell states 1,2,3 got discriminated 


Good_lists = []
Good_choices = []

for i in range(len(Big_discrimination_list)):
    if len(Big_discrimination_list[i]) >= 3:
        Good_lists.append(Big_discrimination_list[i])
        Good_choices.append(i)           # so choices are counted from zero, not 1.  

print(len(Big_discrimination_list))
print(Good_lists)
print(Good_choices)