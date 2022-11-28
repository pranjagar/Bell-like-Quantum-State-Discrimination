import numpy as n
import pandas as pd
# import dummy as D
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
phi_values = [0, (m.pi)/2, (m.pi)/4, m.pi, -(m.pi/4)]
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

# print(Big_resultant)  # BIG LIST



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

# print(len(Big_discrimination_list))
# print(Good_lists)
# print(Good_choices)




# Actual_List = []
# for i in range(len(Good_choices)):
#     Actual_List.append(Big_resultant[i])

# print(Actual_List)
def NewNewlatex_conversion(coeff, vects):                                    # 'A' is a the output (a list of strings) that you wanna convert into latex code

    AA = [(str(coeff[i])+str(vects[i])+ '+') for i in range(len(vects))]       #adding the  + at the end of each term for display purpose    
    B = ''.join(AA)                                        # making a huge string by adding all the elements of the list
    C = [i for i in B]                                         # making a huge list composed of The letters of the huge string above
    C.insert(0,'\\begin{align*} & ')                        # adding begin align command for latex type setting, and adding also at the end
    C.pop()                                               # removing the extra last + sign

    counter = 0                                                    # Dummy variable forkeeping track of even and odd,for adding slashes appropriately
    for i in range(len(C)):                                      # loop that converts symbols into their corresponding latex format
        if C[i] == '*':
            if C[i+1] == '*':
                C[i] = '^{'
                C[i+2] += '}'
            else:
                C[i] = '' 
        elif C[i] == '_' and C[i+1] != '{' :                        # added the 'and' part on 10/18 10 AM
            C[i] = '_{'
            C[i+2] += '}'
        elif C[i] == '[' and C[i+2] != ']':
            C[i] = '|' 
        elif i < (len(C)-7) and C[i] == 'S' and C[i+1] == 'q' and C[i+2] == 'r' and C[i+3] == 't' and C[i+4] == '[' and C[i+6] == ']':
            for j in range(8):
                if j != 5:
                    C[i+j] = '' 
            C[i+5] = '\\sqrt{'+C[i+5]+'}' 
        elif i > 2 and C[i] == ']' and C[i-2] != '[':
            counter += 1
            if counter%1 ==0:                                 # change '1' to '2' or whatever for making new line (adding \\) after 2 terms
                C[i] = '\\rangle \\\\ & '
            else:
                C[i] = '\\rangle'
        elif C[i] == '+' and C[i+1] == '-':
            C[i] = ''
    out = ''.join(C)

    C.append(' \\end{align*}')                         
    out = ''.join(C)                                                             # recombining into a final string for display 
    return out

def compare_outputs(L):             # L is a list of ten bell outputs for four bell states, or a four list  
    compared_list = []
    for i in range(len(L[0])):
        S = []
        for j in range(len(L)):
            S.append(L[j][i])
        compared_list.append(S)
    return compared_list
    # Ex : print(compare_outputs(Big_resultant[0]))





# # print(len(Good_choices))




# Big_resultant_compared = []               # the big list in the alternative format
# for i in range(len(Big_resultant)):
#     Big_resultant_compared.append(compare_outputs(Big_resultant[i]))


ab = [302, 304, 310, 311, 313, 317, 319, 320, 321, 323, 352, 354, 360, 361, 363, 367, 369, 370, 371, 373, 552, 554, 560, 561, 563, 567, 569, 570, 571, 573, 602, 604, 610, 611, 613, 617, 619, 620, 621, 623, 1262, 1264, 1272, 1274, 1337, 1339, 1347, 1349, 1637, 1639, 1647, 1649, 1712, 1714, 1722, 1724, 2177, 2179, 2185, 2186, 2188, 2192, 2194, 2195, 2196, 2198, 2227, 2229, 2235, 2236, 2238, 2242, 2244, 2245, 2246, 2248, 2427, 2429, 2435, 2436, 2438, 2442, 2444, 2445, 2446, 2448, 2477, 2479, 2485, 2486, 2488, 2492, 2494, 2495, 2496, 2498, 2512, 2514, 2522, 2524, 2587, 2589, 2597, 2599, 2887, 2889, 2897, 2899, 2962, 2964, 2972, 2974, 3427, 3429, 3435, 3436, 3438, 3442, 3444, 3445, 3446, 3448, 3477, 3479, 3485, 3486, 3488, 3492, 3494, 3495, 3496, 3498, 3677, 3679, 3685, 3686, 3688, 3692, 3694, 3695, 3696, 3698, 3727, 3729, 3735, 3736, 3738, 3742, 3744, 3745, 3746, 3748, 4387, 4389, 4397, 4399, 4462, 4464, 4472, 4474, 4762, 4764, 4772, 4774, 4837, 4839, 4847, 4849, 5302, 5304, 5310, 5311, 5313, 5317, 5319, 5320, 5321, 5323, 5352, 5354, 5360, 5361, 5363, 5367, 5369, 5370, 5371, 5373, 5552, 5554, 5560, 5561, 5563, 5567, 5569, 5570, 5571, 5573, 5602, 5604, 5610, 5611, 5613, 5617, 5619, 5620, 5621, 5623, 5637, 5639, 5647, 5649, 5712, 5714, 5722, 5724, 6012, 6014, 6022, 6024, 6087, 6089, 6097, 6099, 9677, 9679, 9685, 9686, 9688, 9692, 9694, 9695, 9696, 9698, 9727, 9729, 9735, 9736, 9738, 9742, 9744, 9745, 9746, 9748, 9927, 9929, 9935, 9936, 9938, 9942, 9944, 9945, 9946, 9948, 9977, 9979, 9985, 9986, 9988, 9992, 9994, 9995, 9996, 9998, 10637, 10639, 10647, 10649, 10712, 10714, 10722, 10724, 11012, 11014, 11022, 11024, 11087, 11089, 11097, 11099, 11552, 11554, 11560, 11561, 11563, 11567, 11569, 11570, 11571, 11573, 11602, 11604, 11610, 11611, 11613, 11617, 11619, 11620, 11621, 11623, 11802, 11804, 11810, 11811, 11813, 11817, 11819, 11820, 11821, 11823, 11852, 11854, 11860, 11861, 11863, 11867, 11869, 11870, 11871, 11873, 11887, 11889, 11897, 11899, 11962, 11964, 11972, 11974, 12262, 12264, 12272, 12274, 12337, 12339, 12347, 12349]


Blah = [Big_resultant[i] for i in ab]    #RAW GOOD LIST

# Final_List = compare_outputs(list(Blah))

Na = []
for i in range(len(Blah)):
    Na.append(compare_outputs(Blah[i]))

# print(Na)   #COMPARED GOOD LIST
# print(Final_List)

# latexgoodlist = str(Na)

# print(NewNewlatex_conversion(latexgoodlist, TenZeroCoeffs))

# for i in ab:
#     print(f'\text{Outputs {i}} : {compare_outputs(Big_resultant[i])}')




def choice_mirrors(choice_number,n = 6, L = [0, (m.pi)/2, (m.pi)/4, m.pi, -(m.pi/4)]):              # N is a number, n is number of mirrors, L is list of possible vaules of t, .707 correspoinds to 1/(n.sqrt(2))
    out = []
    a = len(L)
    for i in range(n):
        number = choice_number//(a**(n-i-1))
        t = L[number]
        out.append(t)
        choice_number = choice_number%(a**(n-i-1))
    return out


for i in range(len(ab)):
    print(f'Choice {ab[i]} mirrors : {choice_mirrors(ab[i])}')