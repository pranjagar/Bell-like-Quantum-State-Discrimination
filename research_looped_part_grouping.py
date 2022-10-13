import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym

print('------BEGIN----------BEGIN---------BEGIN-----------BEGIN--------BEGIN-------------BEGIN---------BEGIN-----------BEGIN--')

# Side functions stored here


# LATEX function: to convert our output display state into latex code that can be directly copied and result can be seen easily
def latex_conversion(A):                                    # 'A' is a the output (a list of strings) that you wanna convert into latex code

    AA = [(i+'+') for i in A]                               #adding the  + at the end of each term for display purpose    
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
        elif C[i] == '_':
            C[i] = '_{'
            C[i+2] += '}'
        elif C[i] == '[':
            C[i] = '|'
        elif C[i] == ']':
            counter += 1
            if counter%1 ==0:
                C[i] = '\\rangle \\\\ & '
            else:
                C[i] = '\\rangle'
        elif C[i] == '+' and C[i+1] == '-':
            C[i] = ''

    C.append(' \\end{align*}')                         
    out = ''.join(C)                                                             # recombining into a final string for display 
    return out


# GROUPING FUNCTION


def grouping(A):                                                    # 'A' is list of strings particularly ending with string [1,0,0,1] etc.
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j][-9:] == A[i][-9:]:
                A[i] = '('+(A[i][0:(len(A[i])-10)] +'+' + A[j][0:(len(A[j])-10)]) + ')*' + A[i][-9:]
                A[j] = '@@@'
    grouped_A = [i for i in A if i != '@@@']
    return grouped_A














six_states_0 = n.array([0,0])                                                                # defining the six possilbe output states
six_states_1 = n.array([1,0])
six_states_2 = n.array([0,1])
six_states_3 = n.array([1,1])
six_states_4 = n.array([2,0])
six_states_5 = n.array([0,2])
empty = n.array([])

ten_states_0 = n.array([0,0,0,0])                                                           # defining the ten possilbe output states
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
    total_index = int(matrix_index)                                                              # finding the numbers 1, 2 ,12 etc so to choose appropriate elts from the full vectors etc.                            
    first_matrix_index = int(matrix_index[0]) 
    second_matrix_index = int(matrix_index[1])
    t = sym.Symbol('t'+f'_{total_index}')                                                        # creating matching coeficients
    r = sym.Symbol('r'+f'_{total_index}')

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

# Notes : matrix index argument should be given as a two digit number, in ascendign order, and AS A STRING.

choice = input("Bell state input or basis state input ? (type 'bell' or 'basis')" )

if choice == 'bell':
    InputBellState = (input("Input bell state (type 'def' for symbols): " ))
    if InputBellState == 'def':
        print('[(00+11) = phi+, (00-11) = phi-, (01+10) = psi+, (10-10) = psi-]')
    elif InputBellState == 'phi+':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/(n.sqrt(2)), 1/(n.sqrt(2))]
    elif InputBellState == 'phi-':
        user_input_list = [ten_states_2,ten_states_5]
        user_input_coeffs = [1/(n.sqrt(2)), -1/(n.sqrt(2))]
    elif InputBellState == 'psi+':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/(n.sqrt(2)), 1/(n.sqrt(2))]
    elif InputBellState == 'psi-':
        user_input_list = [ten_states_3,ten_states_4]
        user_input_coeffs = [1/(n.sqrt(2)), -1/(n.sqrt(2))]
elif choice == 'basis':
    user_input_state = input("input state (enter as 1001 0200 etc.)? ")
    user_input_list = [[int(i) for i in user_input_state]]
    user_input_coeffs = [1]
else: 
    print('unrecognized input!')












# use the second block below instead of the first one for custom user inputs

# user_input_matrix = 13
# user_input_list = [1,0,0,1]

user_input_matrix = int(input("Till which Beam splitter (enter input as 13, 14 etc.) ? "))
# user_input_state = input("What state is input (enter as 1001 0200 etc.)? ")                        #Inputting the required states etc.
# user_input_list = [[int(i) for i in user_input_state]]


M12 = MatrixAction('12', user_input_list,user_input_coeffs)                                         # making use of the beam splitter function, looping it over and over
M13 = MatrixAction('13', M12[0], M12[1])
M14 = MatrixAction('14', M13[0], M13[1])
M23 = MatrixAction('23', M14[0], M14[1])
M24 = MatrixAction('24', M23[0], M23[1])
M34 = MatrixAction('34', M24[0], M24[1])


if user_input_matrix == 12:                                                            #this is just so the output matches the corresponding input
    output_display = (M12[2])
    output_coefficients = (M12[1])
elif user_input_matrix == 13:
    output_display = (M13[2])
    output_coefficients = (M13[1])
elif user_input_matrix == 14:
    output_display = (M14[2])
    output_coefficients = (M14[1])
elif user_input_matrix == 23:
    output_display = (M23[2])
    output_coefficients = (M23[1])
elif user_input_matrix == 24:
    output_display = (M24[2])
    output_coefficients = (M24[1])
elif user_input_matrix == 34:
    output_coefficients = (M34[1])
    output_display = (M34[2])
else:
    print('Wrong Input!!') 


# print(M14[:2])
# print(M14[2])


print("")
print("")
# print(f'LATEX Grouped for: ',latex_conversion(output_display))
print(f'Grouped MATHEMATICA Code: ', sym.mathematica_code(output_coefficients))


























print('------END----------END---------END-----------END--------END-------------END---------END-----------END--')


























