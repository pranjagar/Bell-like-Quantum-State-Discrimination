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
        elif C[i] == '_' and C[i+1] != '{' :                        # added the 'and' part on 10/18 10 AM
            C[i] = '_{'
            C[i+2] += '}'
        elif C[i] == '[':
            C[i] = '|'
        elif C[i] == ']':
            counter += 1
            if counter%1 ==0:                                 # change '1' to '2' or whatever for making new line (adding \\) after 2 terms
                C[i] = '\\rangle \\\\ & '
            else:
                C[i] = '\\rangle'
        elif C[i] == '+' and C[i+1] == '-':
            C[i] = ''

    C.append(' \\end{align*}')                         
    out = ''.join(C)                                                             # recombining into a final string for display 
    return out


# new and better latex conversion (unchecked for orthodox cases)


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


    C.append(' \\end{align*}')                         
    out = ''.join(C)                                                             # recombining into a final string for display 
    return out


# fn from mathematica to latex

def MathematicaToLatex(A):    # A is the input string
    c = [i for i in A]
    for i in range(len(c)-2):
        if c[i] == 'r' or c[i] == 't':
            if c[i+1] == '1' or c[i+1] == '2' or c[i+1] == '3':
                if c[i+2]== '1' or c[i+2]== '2' or c[i+2]== '3' or c[i+2]== '4':
                    # print(c[i:i+3])
                    c[i+1] = '_{'+ c[i+1]
                    c[i+2] = c[i+2] + '}'
        # elif c[i] != 'r' or 't'           
    # c.insert(0,'\\begin{align*} & ')
    # c.append(' \\end{align*}')  
    out = ''.join(c)
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


#fn for removing '_' nad '1.4142' etc for mathematica and latex (uncomment) from input strings 
def removing_nSqrt(A):      
    b = [i for i in A]
    for i in range(len(b)):
        if b[i] == '_':
            b[i] = ''
    if len(b) > 15:
        for i in range(len(b)):            # removing the 1.4142 
            if b[i] == '1' and b[i+1] == '.' and b[i+2] == '4' and b[i+3] == '1' and b[i+4] == '4':
                b[i] = 'Sqrt[2]'
                # b[i] = '\\sqrt{2}'              # uncomment for latex output without 1.4142
                for j in range(14):
                    b[i+1+j] = ''
    if len(b) > 17:        
        for i in range(len(b)):            # removing the 0.7071
            if b[i] == '0' and b[i+1] == '.' and b[i+2] == '7' and b[i+3] == '0' and b[i+4] == '7':
                b[i] = '(1/Sqrt[2])'                  
                # b[i] = '\\frac{1}{\\sqrt{2}}'                  # uncomment for latex output without 1.4142
                for j in range(16):
                    b[i+1+j] = ''
    for i in range(len(b)):
        if i < len(b)-3 and b[i] == '1' and b[i+1]== '.' and b[i+2]== '0':
            b[i] = ''
            b[i+1] = ''
            b[i+2] = ''
            if b[i+3] == '*':
                b[i+3] = ''
    c =''.join(b)      
    return c








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

 
# uncomment for full user interface kinda thing
# choice = input("Bell state input or basis state input ? (type 'bell' or 'basis')" )       
choice = 'bell'                                     # uncomment to avoid imput: choice = bell states

if choice == 'bell':
    InputBellState = (input("Input bell state (type 'def' for symbols): " ))
    if InputBellState == 'def':
        print('[(00+11) = phiplus, (00-11) = phiminus, (01+10) = psiplus, (10-10) = psiminus]')
    elif InputBellState == 'phiplus':
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
elif choice == 'basis':
    user_input_state = input("input state (enter as 1001 0200 etc.)? ")
    user_input_list = [[int(i) for i in user_input_state]]
    user_input_coeffs = [1]
else: 
    print('unrecognized input!')

# user_input_matrix = int(input("Till which Beam splitter (enter input as 13, 14 etc.) ? "))

 
user_input_matrix = 34                                       # uncomment to avoid imput: matrix  = 34 


 
# user_input_list = [[1,0,0,1]]            # uncomment to avoid inputting state & matrices while debugging, default state = 1001, matrix = 23
# user_input_coeffs = [1]
# user_input_matrix = 23 


# use the second block below instead of the first one for custom user inputs


M12 = MatrixAction('12', user_input_list,user_input_coeffs)                                         # making use of the beam splitter function, looping it over and over
M13 = MatrixAction('13', M12[0], M12[1])
M14 = MatrixAction('14', M13[0], M13[1])
M23 = MatrixAction('23', M14[0], M14[1])
M24 = MatrixAction('24', M23[0], M23[1])
M34 = MatrixAction('34', M24[0], M24[1])


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
else:
    print('Wrong Input!!') 


# print(M14[:2])
# print(M14[2])


# print(f'LATEX Grouped for: ',latex_conversion(output_display))
# print(f'Grouped MATHEMATICA (list of coefficients): ', sym.mathematica_code(output_coefficients))



# for mathematica solving specifically

 
# print('Test: ',removing_nSqrt('0.707106781186547*t12 +1.4142135623731*x + t_12'))


# for i in range(len(output_coefficients)):            # uncomment for printing all ten coefficients in mathematica script
#     print(f'{InputBellState}_Coeffs = {removing_nSqrt(sym.mathematica_code(output_coefficients[i]))} \n') 


MathematicaInputCoeffList = [removing_nSqrt(sym.mathematica_code(i)) for i in output_coefficients]       # gives a mathematica list (with {}) of all ten coeff of the imput state 
inputlist = '{'+ ','.join(MathematicaInputCoeffList)+'}'
print(f'{InputBellState}CoeffList = {inputlist}')         


# text editing part for mathematica calculations


# mathcopy = '-r23 r34^2 t12 t13 t23-r12 r13 r34^2 t13 t23^2-r23^2 r24 r34 t12 t13 t34-2 r12 r13 r23 r24 r34 t13 t23 t34+r24 r34 t12 t13 t23^2 t34-r13 r14 r23 r34 t12 t24 t34-r12 r23 r34 t14 t24 t34-r12 r13^2 r14 r34 t23 t24 t34+r12 r14 r34 t13^2 t23 t24 t34+r13 r34 t12 t14 t23 t24 t34-r12 r13 r23^2 r24^2 t13 t34^2+r23 r24^2 t12 t13 t23 t34^2-r12 r13^2 r14 r23 r24 t24 t34^2+r12 r14 r23 r24 t13^2 t24 t34^2+r13 r23 r24 t12 t14 t24 t34^2+r13 r14 r24 t12 t23 t24 t34^2+r12 r24 t14 t23 t24 t34^2+r12 r13 r14^2 t13 t24^2 t34^2-r14 t12 t13 t14 t24^2 t34^2'
MathCoeffPsiplus = ['(-r14^2 r24 t12 t13-r14 (2 r12 r13 r24 t13 t14+r13 r23 t12 t24+r12 t23 t24)+t14 (r24 t12 t13 t14+r12 r23 (-r13^2+t13^2) t24+r13 t12 t23 t24))/Sqrt[2]' ,'(1/Sqrt[2])(r34 t12 t13 (-r14^2+t14^2) t24+r12 r13^2 t14 (r23 r24 r34-t23 t34)+r12 (-r23 r24 r34 t13^2 t14+r14 r24 r34 t23+r14 r23 t34+t13^2 t14 t23 t34)-r13 (t12 t14 (r24 r34 t23+r23 t34)+r14 (-r23 r24 r34 t12+2 r12 r34 t13 t14 t24+t12 t23 t34)))',' (1/Sqrt[2])(t12 t13 (-r14^2+t14^2) t24 t34+r12 (r13^2-t13^2) t14 (r34 t23+r23 r24 t34)+r13 t12 (r23 r34 t14+r14 r34 t23+r14 r23 r24 t34-r24 t14 t23 t34)+r12 r14 (-r23 r34+r24 t23 t34-2 r13 t13 t14 t24 t34))', 't13 t14 (r14 t12+r12 r13 t14)',' (1/Sqrt[2])(t12 (-t13 t24 (2 r14 r24 r34 t14+2 r23 r24 r34 t23+r23^2 t34-t23^2 t34)+r13 (r14 r34 t23 (r24^2-t24^2)-r24 t14 t23 t34+r23 (r24^2 r34 t14-r34 t14 t24^2+r14 r24 t34)))+r12 (t14 (r24^2 r34 t23-r34 t23 t24^2+r23 r24 t34)+r14 t13^2 (r23 r34 (r24^2-t24^2)-r24 t23 t34)+r13^2 r14 (r23 r34 (-r24^2+t24^2)+r24 t23 t34)+2 r13 t13 t24 (r14^2 r24 r34+r23 (r23 r24 r34-t23 t34))))' ,'(1/Sqrt[2])(t12 t13 t24 (r23^2 r34-r34 t23^2-2 r14 r24 t14 t34-2 r23 r24 t23 t34)-r12 r13^2 r14 (r24 r34 t23+r23 r24^2 t34-r23 t24^2 t34)+r12 (r14 r24 r34 t13^2 t23+t14 t23 (r24^2-t24^2) t34+r23 (-r24 r34 t14+r14 r24^2 t13^2 t34-r14 t13^2 t24^2 t34))+r13 (r23 r24^2 t12 t14 t34+2 r12 r14^2 r24 t13 t24 t34+r24 (r34 t12 t14 t23+2 r12 r23^2 t13 t24 t34)+r23 t24 (2 r12 r34 t13 t23-t12 t14 t24 t34)-r14 t12 (r23 r24 r34+t23 (-r24^2+t24^2) t34)))',' -t12 (r14 r24 (r24 t13 t14+r13 t23 t24)+r23 t24 (r13 r24 t14-t13 t23 t24))+r12 (r13^2 r14 r23 r24 t24-r24 (r14 r23 t13^2+t14 t23) t24+r13 t13 (r14^2 r24^2-r23^2 t24^2))', '(1/Sqrt[2])(2 r34 t13 t23 (r23 t12+r12 r13 t23) t34-2 r34 (-t12 (r23 r24 (r24 t13 t23+r13 t14 t24)+r14 t24 (r13 r24 t23-t13 t14 t24))+r12 (r13^2 r14 r23 r24 t24-r24 (r14 r23 t13^2+t14 t23) t24+r13 t13 (r23^2 r24^2-r14^2 t24^2))) t34-(r23^2 r24 t12 t13+r23 (2 r12 r13 r24 t13 t23+r13 r14 t12 t24+r12 t14 t24)-t23 (r24 t12 t13 t23+r12 r14 (-r13^2+t13^2) t24+r13 t12 t14 t24)) (r34^2-t34^2))', 't12 (r23 r24^2 r34^2 t13 t23+r13 r23 r24 r34^2 t14 t24+r23^2 r24 r34 t13 t34+r13 r34 t23 t24 (r14 r24 r34-t14 t34)+r23 t34 (r13 r14 r34 t24-t13 t23 t34)-r34 t13 (r14 r34 t14 t24^2+r24 t23^2 t34))+r12 (r13^2 r14 r34 t24 (-r23 r24 r34+t23 t34)+r13 t13 (-r23^2 r24^2 r34^2+r14^2 r34^2 t24^2+2 r23 r24 r34 t23 t34-t23^2 t34^2)+r34 t24 (t14 (r24 r34 t23+r23 t34)+r14 t13^2 (r23 r24 r34-t23 t34)))',' -r23^2 r24 t13 t34 (r34 t12+r12 r13 r24 t34)-r23 (r34^2 t12 t13 t23+r34 (2 r12 r13 r24 t13 t23+r13 r14 t12 t24+r12 t14 t24) t34-r24 (r24 t12 t13 t23+r12 r14 (-r13^2+t13^2) t24+r13 t12 t14 t24) t34^2)+t12 t34 (r24 t23 (r34 t13 t23+r13 r14 t24 t34)+t14 t24 (r13 r34 t23-r14 t13 t24 t34))+r12 (-r13^2 r14 r34 t23 t24 t34+t23 t24 t34 (r14 r34 t13^2+r24 t14 t34)+r13 (-r34^2 t13 t23^2+r14^2 t13 t24^2 t34^2))']
MathCoeffPsiplusExpanded = ['-(\\frac{1}{\\sqrt{2}})\\left(r14^2 r24 t12 t13-2 r12 r13 r14 r24 t13 t14+r24 t12 t13 t14^2-r13 r14 r23 t12 t24-r12 r13^2 r23 t14 t24+r12 r23 t13^2 t14 t24-r12 r14 t23 t24+r13 t12 t14 t23 t24\\right)',
'(\\frac{1}{\\sqrt{2}})\\left(r13 r14 r23 r24 r34 t12+r12 r13^2 r23 r24 r34 t14-r12 r23 r24 r34 t13^2 t14+r12 r14 r24 r34 t23-r13 r24 r34 t12 t14 t23-r14^2 r34 t12 t13 t24-2 r12 r13 r14 r34 t13 t14 t24+r34 t12 t13 t14^2 t24+r12 r14 r23 t34-r13 r23 t12 t14 t34-r13 r14 t12 t23 t34-r12 r13^2 t14 t23 t34+r12 t13^2 t14 t23 t34\\right)',
'-(\\frac{1}{\\sqrt{2}})\\left(r12 r14 r23 r34+r13 r23 r34 t12 t14+r13 r14 r34 t12 t23+r12 r13^2 r34 t14 t23-r12 r34 t13^2 t14 t23+r13 r14 r23 r24 t12 t34+r12 r13^2 r23 r24 t14 t34-r12 r23 r24 t13^2 t14 t34+r12 r14 r24 t23 t34-r13 r24 t12 t14 t23 t34-r14^2 t12 t13 t24 t34-2 r12 r13 r14 t13 t14 t24 t34+t12 t13 t14^2 t24 t34\\right)',
'r14 t12 t13 t14+r12 r13 t13 t14^2',
'-(\\frac{1}{\\sqrt{2}})\\left(r12 r13^2 r14 r23 r24^2 r34+r12 r14 r23 r24^2 r34 t13^2+r13 r23 r24^2 r34 t12 t14+r13 r14 r24^2 r34 t12 t23+r12 r24^2 r34 t14 t23+2 r12 r13 r14^2 r24 r34 t13 t24+2 r12 r13 r23^2 r24 r34 t13 t24-2 r14 r24 r34 t12 t13 t14 t24-2 r23 r24 r34 t12 t13 t23 t24+r12 r13^2 r14 r23 r34 t24^2-r12 r14 r23 r34 t13^2 t24^2-r13 r23 r34 t12 t14 t24^2-r13 r14 r34 t12 t23 t24^2-r12 r34 t14 t23 t24^2+r13 r14 r23 r24 t12 t34+r12 r23 r24 t14 t34+r12 r13^2 r14 r24 t23 t34-r12 r14 r24 t13^2 t23 t34-r13 r24 t12 t14 t23 t34-r23^2 t12 t13 t24 t34-2 r12 r13 r23 t13 t23 t24 t34+t12 t13 t23^2 t24 t34\\right)',
'-(\\frac{1}{\\sqrt{2}})\\left(r13 r14 r23 r24 r34 t12-r12 r23 r24 r34 t14-r12 r13^2 r14 r24 r34 t23+r12 r14 r24 r34 t13^2 t23+r13 r24 r34 t12 t14 t23+r23^2 r34 t12 t13 t24+2 r12 r13 r23 r34 t13 t23 t24-r34 t12 t13 t23^2 t24-r12 r13^2 r14 r23 r24^2 t34+r12 r14 r23 r24^2 t13^2 t34+r13 r23 r24^2 t12 t14 t34+r13 r14 r24^2 t12 t23 t34+r12 r24^2 t14 t23 t34+2 r12 r13 r14^2 r24 t13 t24 t34+2 r12 r13 r23^2 r24 t13 t24 t34-2 r14 r24 t12 t13 t14 t24 t34-2 r23 r24 t12 t13 t23 t24 t34+r12 r13^2 r14 r23 t24^2 t34-r12 r14 r23 t13^2 t24^2 t34-r13 r23 t12 t14 t24^2 t34-r13 r14 t12 t23 t24^2 t34-r12 t14 t23 t24^2 t34\\right)',
'r12 r13 r14^2 r24^2 t13-r14 r24^2 t12 t13 t14+r12 r13^2 r14 r23 r24 t24-r12 r14 r23 r24 t13^2 t24-r13 r23 r24 t12 t14 t24-r13 r14 r24 t12 t23 t24-r12 r24 t14 t23 t24-r12 r13 r23^2 t13 t24^2+r23 t12 t13 t23 t24^2',
'-(\\frac{1}{\\sqrt{2}})\\left(r23^2 r24 r34^2 t12 t13-2 r12 r13 r23 r24 r34^2 t13 t23+r24 r34^2 t12 t13 t23^2-r13 r14 r23 r34^2 t12 t24-r12 r23 r34^2 t14 t24-r12 r13^2 r14 r34^2 t23 t24+r12 r14 r34^2 t13^2 t23 t24+r13 r34^2 t12 t14 t23 t24-2 r12 r13 r23^2 r24^2 r34 t13 t34+2 r23 r34 t12 t13 t23 t34+2 r23 r24^2 r34 t12 t13 t23 t34+2 r12 r13 r34 t13 t23^2 t34-2 r12 r13^2 r14 r23 r24 r34 t24 t34+2 r12 r14 r23 r24 r34 t13^2 t24 t34+2 r13 r23 r24 r34 t12 t14 t24 t34+2 r13 r14 r24 r34 t12 t23 t24 t34+2 r12 r24 r34 t14 t23 t24 t34+2 r12 r13 r14^2 r34 t13 t24^2 t34-2 r14 r34 t12 t13 t14 t24^2 t34+r23^2 r24 t12 t13 t34^2+2 r12 r13 r23 r24 t13 t23 t34^2-r24 t12 t13 t23^2 t34^2+r13 r14 r23 t12 t24 t34^2+r12 r23 t14 t24 t34^2+r12 r13^2 r14 t23 t24 t34^2-r12 r14 t13^2 t23 t24 t34^2-r13 t12 t14 t23 t24 t34^2\\right)',
'-r12 r13 r23^2 r24^2 r34^2 t13+r23 r24^2 r34^2 t12 t13 t23-r12 r13^2 r14 r23 r24 r34^2 t24+r12 r14 r23 r24 r34^2 t13^2 t24+r13 r23 r24 r34^2 t12 t14 t24+r13 r14 r24 r34^2 t12 t23 t24+r12 r24 r34^2 t14 t23 t24+r12 r13 r14^2 r34^2 t13 t24^2-r14 r34^2 t12 t13 t14 t24^2+r23^2 r24 r34 t12 t13 t34+2 r12 r13 r23 r24 r34 t13 t23 t34-r24 r34 t12 t13 t23^2 t34+r13 r14 r23 r34 t12 t24 t34+r12 r23 r34 t14 t24 t34+r12 r13^2 r14 r34 t23 t24 t34-r12 r14 r34 t13^2 t23 t24 t34-r13 r34 t12 t14 t23 t24 t34-r23 t12 t13 t23 t34^2-r12 r13 t13 t23^2 t34^2',
'-r23 r34^2 t12 t13 t23-r12 r13 r34^2 t13 t23^2-r23^2 r24 r34 t12 t13 t34-2 r12 r13 r23 r24 r34 t13 t23 t34+r24 r34 t12 t13 t23^2 t34-r13 r14 r23 r34 t12 t24 t34-r12 r23 r34 t14 t24 t34-r12 r13^2 r14 r34 t23 t24 t34+r12 r14 r34 t13^2 t23 t24 t34+r13 r34 t12 t14 t23 t24 t34-r12 r13 r23^2 r24^2 t13 t34^2+r23 r24^2 t12 t13 t23 t34^2-r12 r13^2 r14 r23 r24 t24 t34^2+r12 r14 r23 r24 t13^2 t24 t34^2+r13 r23 r24 t12 t14 t24 t34^2+r13 r14 r24 t12 t23 t24 t34^2+r12 r24 t14 t23 t24 t34^2+r12 r13 r14^2 t13 t24^2 t34^2-r14 t12 t13 t14 t24^2 t34^2',
]




MathCoeffPhiplus = ['','','','','','','','','',''] 


MathCoeffPhiplusExpanded = []
MathCoeffPsiminus = ['(-r14^2 r24 t12 t13+r14 (2 r12 r13 r24 t13 t14-r13 r23 t12 t24-r12 t23 t24)+t14 (r24 t12 t13 t14+r12 r23 (r13^2-t13^2) t24-r13 t12 t23 t24))/Sqrt[2]',
'(1/Sqrt[2])(r34 t12 t13 (-r14^2+t14^2) t24+r13 t12 t14 (r24 r34 t23+r23 t34)+r12 r13^2 t14 (-r23 r24 r34+t23 t34)+r13 r14 (r23 r24 r34 t12+2 r12 r34 t13 t14 t24-t12 t23 t34)+r12 (r23 r24 r34 t13^2 t14+r14 r24 r34 t23+r14 r23 t34-t13^2 t14 t23 t34))',
'(1/Sqrt[2])(t12 t13 (-r14^2+t14^2) t24 t34-r12 (r13^2-t13^2) t14 (r34 t23+r23 r24 t34)+r13 t12 (-r23 r34 t14+r14 r34 t23+r14 r23 r24 t34+r24 t14 t23 t34)+r12 r14 (-r23 r34+r24 t23 t34+2 r13 t13 t14 t24 t34))',
't13 t14 (r14 t12-r12 r13 t14)',
'(1/Sqrt[2])(-2 r14 r24 r34 t13 (r12 r13 r14+t12 t14) t24-2 r23 r24 r34 t13 (r12 r13 r23-t12 t23) t24+r34 (r13 t12 (r23 t14-r14 t23)+r12 (r13^2 r14 r23-r14 r23 t13^2+t14 t23)) (r24^2-t24^2)-r24 (r12 r13^2 r14 t23-r12 (r23 t14+r14 t13^2 t23)+r13 t12 (r14 r23+t14 t23)) t34+t13 (r23^2 t12+2 r12 r13 r23 t23-t12 t23^2) t24 t34)',
'(1/Sqrt[2])(t12 t13 t24 (-r23^2 r34+r34 t23^2-2 r14 r24 t14 t34+2 r23 r24 t23 t34)+r12 r13^2 r14 (r24 r34 t23+r23 r24^2 t34-r23 t24^2 t34)-r12 (r14 r24 r34 t13^2 t23+t14 t23 (-r24^2+t24^2) t34+r23 (r24 r34 t14+r14 r24^2 t13^2 t34-r14 t13^2 t24^2 t34))+r13 (r23 r24^2 t12 t14 t34-2 r12 r14^2 r24 t13 t24 t34+r24 (r34 t12 t14 t23-2 r12 r23^2 t13 t24 t34)-r23 t24 (2 r12 r34 t13 t23+t12 t14 t24 t34)+r14 t12 (r23 r24 r34+t23 (-r24^2+t24^2) t34)))',
'-t12 (r14 r24 (r24 t13 t14-r13 t23 t24)+r23 t24 (r13 r24 t14+t13 t23 t24))-r12 (r13^2 r14 r23 r24 t24+r24 (-r14 r23 t13^2+t14 t23) t24+r13 t13 (r14^2 r24^2-r23^2 t24^2))',
'(1/Sqrt[2])(-2 r34 t13 t23 (r23 t12+r12 r13 t23) t34+2 r34 (-t12 (r23 r24 (r24 t13 t23-r13 t14 t24)+r14 t24 (r13 r24 t23+t13 t14 t24))+r12 (r13^2 r14 r23 r24 t24+r24 (-r14 r23 t13^2+t14 t23) t24+r13 t13 (r23^2 r24^2-r14^2 t24^2))) t34+(r23^2 r24 t12 t13+r23 (2 r12 r13 r24 t13 t23+r13 r14 t12 t24-r12 t14 t24)+t23 (-r24 t12 t13 t23+r12 r14 (r13^2-t13^2) t24+r13 t12 t14 t24)) (r34^2-t34^2))',
'-t12 (r23 r24^2 r34^2 t13 t23-r13 r23 r24 r34^2 t14 t24+r23^2 r24 r34 t13 t34+r13 r34 t23 t24 (r14 r24 r34+t14 t34)+r23 t34 (r13 r14 r34 t24-t13 t23 t34)+r34 t13 (r14 r34 t14 t24^2-r24 t23^2 t34))+r12 (r13^2 r14 r34 t24 (r23 r24 r34-t23 t34)+r13 t13 (r23^2 r24^2 r34^2-r14^2 r34^2 t24^2-2 r23 r24 r34 t23 t34+t23^2 t34^2)+r34 t24 (t14 (r24 r34 t23+r23 t34)+r14 t13^2 (-r23 r24 r34+t23 t34)))',
'r23^2 r24 t13 t34 (r34 t12+r12 r13 r24 t34)+r23 (r34^2 t12 t13 t23+r34 (2 r12 r13 r24 t13 t23+r13 r14 t12 t24-r12 t14 t24) t34+r24 (-r24 t12 t13 t23+r12 r14 (r13^2-t13^2) t24+r13 t12 t14 t24) t34^2)-t12 t34 (r24 t23 (r34 t13 t23+r13 r14 t24 t34)+t14 t24 (-r13 r34 t23+r14 t13 t24 t34))+r12 (r13^2 r14 r34 t23 t24 t34+t23 t24 t34 (-r14 r34 t13^2+r24 t14 t34)+r13 t13 (r34^2 t23^2-r14^2 t24^2 t34^2))',
]

# '(\\frac{1}{\\sqrt{2}})\left(' \right)


MathLatexCoeff = [MathematicaToLatex(i) for i in MathCoeffPsiminus]    # list of latex coeffs converted from input code from mathematica


# print(latex_conversion(str(ten_states_1)))



# print(NewNewlatex_conversion(MathLatexCoeff,output_vectors))



print('------END----------END---------END-----------END--------END-------------END---------END-----------END--')
























