import matplotlib as plt
import math as m
import numpy as n
import scipy as s
import sympy as sym

print('------BEGIN----------BEGIN---------BEGIN-----------BEGIN--------BEGIN-------------BEGIN---------BEGIN-----------BEGIN--')

# Side functions stored here


# LATEX function: to convert our output display state into latex code that can be directly copied and result can be seen easily
def latex_conversion(A,n=1):                                    # 'A' is a the output (a list of strings) that you wanna convert into latex code

    AA = [(i+'') for i in A]                               #adding the  + at the end of each term for display purpose    
    B = ''.join(AA)                                        # making a huge string by adding all the elements of the list
    C = [i for i in B]                                         # making a huge list composed of The letters of the huge string above
    # C.pop()

    counter = 0                                                    # Dummy variable forkeeping track of even and odd,for adding slashes appropriately
    for i in range(len(C)):                                      # loop that converts symbols into their corresponding latex format
        if C[i] == '*':
            if i <= len(C)-1 and C[i+1] == '*':
                C[i] = '^{'
                C[i+2] += '}'
            else:
                C[i] = '' 
        elif i <= len(C)-1 and C[i] == '_' and C[i+1] != '{' :                        # added the 'and' part on 10/18 10 AM
            C[i] = '_{'
            C[i+2] += '}'
        elif i < len(C)-2 and C[i] == '['and C[i+2] != ']':
            C[i] = '|'
        elif i > 2 and C[i] == ']' and C[i-2] != '[':
            counter += 1
            if counter%n ==0:                                 # change '1' to '2' or whatever for making new line (adding \\) after 2 terms
                C[i] = '\\rangle \\\\ & '
            else:
                C[i] = '\\rangle'
        elif C[i] == '+' and C[i+1] == '-':
            C[i] = ''

    C.insert(0,'\\begin{align*} & ')                        # adding begin align command for latex type setting, and adding also at the end
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
    out = ''.join(c)

    C.append(' \\end{align*}')                         
    out = ''.join(C)                                                             # recombining into a final string for display 
    return out


# fn from mathematica to latex

def MathematicaToLatex(A):    # A is the input string
    C = [i for i in A]
    for i in range(len(C)):
        if C[i] == 'r' or C[i] == 't':
            if i < len(C)-2 and C[i+1] == '1' or C[i+1] == '2' or C[i+1] == '3':
                if C[i+2]== '1' or C[i+2]== '2' or C[i+2]== '3' or C[i+2]== '4':
                    # print(c[i:i+3])
                    C[i+1] = '_{'+ C[i+1]
                    C[i+2] = C[i+2] + '}'
    # c.insert(0,'\\begin{align*} & ')
    # c.append(' \\end{align*}')  
    out = ''.join(C)
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


#fn for removing '_' and '1.4142' n 1.0* etc for mathematica and latex (uncomment) from input strings 
def removing_nSqrt(A,M= 'M'):      # M = 'M' or 'L' for matheematica or latex
    b = [i for i in A]
    for i in range(len(b)):
        if b[i] == '_':
            if M == 'M':
                b[i] = ''
    if len(b) > 15:
        for i in range(len(b)):            # removing the 1.4142 
            if b[i] == '1' and b[i+1] == '.' and b[i+2] == '4' and b[i+3] == '1' and b[i+4] == '4':
                b[i] = 'Sqrt[2]'
                if M == 'L':
                    b[i] = '\\sqrt{2}'              # uncomment for latex output without 1.4142
                for j in range(14):
                    b[i+1+j] = ''
    if len(b) > 17:        
        for i in range(len(b)):            # removing the 0.7071
            if b[i] == '0' and b[i+1] == '.' and b[i+2] == '7' and b[i+3] == '0' and b[i+4] == '7':
                b[i] = '(1/Sqrt[2])'                  
                if M == 'L':
                    b[i] = '\\frac{1}{\\sqrt{2}}'                  # uncomment for latex output without 1.4142
                for j in range(16):
                    b[i+1+j] = ''
    for i in range(len(b)):
        if i < len(b)-3 and b[i] == '1' and b[i+1]== '.' and b[i+2]== '0':
            b[i] = ''
            b[i+1] = ''
            b[i+2] = ''
            if b[i+3] == '*':
                b[i+3] = ''
    for i in range(len(b)):
        if i < (len(b)-7) and b[i] == 'S' and b[i+1] == 'q' and b[i+2] == 'r' and b[i+3] == 't' and b[i+4] == '[' and b[i+6] == ']':
                for j in range(8):
                    if j != 5:
                        b[i+j] = '' 
                if M == 'L':
                    b[i+5] = '\\sqrt{'+b[i+5]+'}'

    c =''.join(b)   
       
    return c


# Spearating lines from the big list containing outputs of the four bell states

def separating_Big_list_fromMathem(A):             # A is string, containing mathem output list like {{4,5},{d},{''}}. This fn breaks it into different lines and adds parenthes to each part
    counter = 0                                     
    B = [i for i in A]
    for i in range(len(B)):
        if B[i] == '{':
            counter += 1
            if counter == 2:
                k = 0
                while k < 1:
                    B[i] = '\\\\ & \\Bigl('
                    k = k+1
        if B[i] == '}':
            counter -= 1
            if counter == 1:
                k = 0
                while k < 1:
                    B[i] = '\\Bigl)'
                    k = k+1
    B.insert(0,'\\begin{align*} & ')
    B.append(' \\end{align*}')
    c =''.join(B)   
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

 
""" 
# uncomment for full user interface kinda thing
# choice = input("Bell state input or basis state input ? (type 'bell' or 'basis')" )       
choice = 'bell'                                     # uncomment to avoid imput: choice = bell states

if choice == 'bell':
    # InputBellState = 'phiplus'                    # avoiding input
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

 """





def BellOutput(InputBellState, V_or_C_or_Out = 'Out'):              #input one one of the four bell states as string, second input is what is needed : list of coeffs or list of vectors or full output as a string 
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

    if V_or_C_or_Out == 'V':
        return output_vectors
    elif V_or_C_or_Out == 'C':
        return output_coefficients
    elif V_or_C_or_Out == 'Out':
        return output_display





# list of vector outputs for bell states
# print(latex_conversion(str(BellOutput('psiplus', 'V')), 10))
# print(latex_conversion(str(BellOutput('psiminus', 'V')), 10))
# print(latex_conversion(str(BellOutput('phiplus', 'V')), 10))
# print(latex_conversion(str(BellOutput('phiminus', 'V')), 10))                           # 10 says that put '\\ &' after 10 \rangles in the latex 


# To create a list of lists (in mathematica language), each sublist being a list of all ten coefficients of output of one of the bell states 
big_outlist = []

MathematicaInputCoeffList_psiplus = [removing_nSqrt(sym.mathematica_code(i),'M') for i in BellOutput('psiplus','C')]       # gives a mathematica list (with {}) of all ten coeff of the imput state 
inputlist_psiplus = '{'+ ','.join(MathematicaInputCoeffList_psiplus)+'}'
big_outlist.append(inputlist_psiplus)    

MathematicaInputCoeffList_psiminus = [removing_nSqrt(sym.mathematica_code(i),'M') for i in BellOutput('psiminus','C')]       # gives a mathematica list (with {}) of all ten coeff of the imput state 
inputlist_psiminus = '{'+ ','.join(MathematicaInputCoeffList_psiminus)+'}'
big_outlist.append(inputlist_psiminus)    

MathematicaInputCoeffList_phiplus = [removing_nSqrt(sym.mathematica_code(i),'M') for i in BellOutput('phiplus','C')]       # gives a mathematica list (with {}) of all ten coeff of the imput state 
inputlist_phiplus = '{'+ ','.join(MathematicaInputCoeffList_phiplus)+'}'
big_outlist.append(inputlist_phiplus)    

MathematicaInputCoeffList_phiminus = [removing_nSqrt(sym.mathematica_code(i),'M') for i in BellOutput('phiminus','C')]       # gives a mathematica list (with {}) of all ten coeff of the imput state 
inputlist_phiminus = '{'+ ','.join(MathematicaInputCoeffList_phiminus)+'}'
big_outlist.append(inputlist_phiminus)    

all_bell_outputs_mathem =  '{'+ ','.join(big_outlist)+'}'
# print('BigList = ',all_bell_outputs_mathem)                  # uncomment to print the outputs of the four bell states



# replace the big list output from mathematica in 'a' below and run
a = '{{(r23 t24)/Sqrt[2],-((r23 r24 r34)/Sqrt[2])+(t23 t34)/Sqrt[2],-((r34 t23)/Sqrt[2])-(r23 r24 t34)/Sqrt[2],(r34 t23 (-r24^2+t24^2))/Sqrt[2]-(r23 r24 t34)/Sqrt[2],(r23 r24 r34)/Sqrt[2]+(t23 (-r24^2+t24^2) t34)/Sqrt[2],r24 t23 t24,-Sqrt[2] r24 r34 t23 t24 t34-(r23 t24 (-r34^2+t34^2))/Sqrt[2],-r24 r34^2 t23 t24-r23 r34 t24 t34,r23 r34 t24 t34-r24 t23 t24 t34^2,0},{(r23 t24)/Sqrt[2],-((r23 r24 r34)/Sqrt[2])+(t23 t34)/Sqrt[2],-((r34 t23)/Sqrt[2])-(r23 r24 t34)/Sqrt[2],(r34 t23 (-r24^2+t24^2))/Sqrt[2]-(r23 r24 t34)/Sqrt[2],(r23 r24 r34)/Sqrt[2]+(t23 (-r24^2+t24^2) t34)/Sqrt[2],r24 t23 t24,-Sqrt[2] r24 r34 t23 t24 t34-(r23 t24 (-r34^2+t34^2))/Sqrt[2],-r24 r34^2 t23 t24-r23 r34 t24 t34,r23 r34 t24 t34-r24 t23 t24 t34^2,0},{(r23 t24)/Sqrt[2],-((r23 r24 r34)/Sqrt[2])+(t23 t34)/Sqrt[2],-((r34 t23)/Sqrt[2])-(r23 r24 t34)/Sqrt[2],(r34 t23 (-r24^2+t24^2))/Sqrt[2]-(r23 r24 t34)/Sqrt[2],(r23 r24 r34)/Sqrt[2]+(t23 (-r24^2+t24^2) t34)/Sqrt[2],r24 t23 t24,-Sqrt[2] r24 r34 t23 t24 t34-(r23 t24 (-r34^2+t34^2))/Sqrt[2],-r24 r34^2 t23 t24-r23 r34 t24 t34,r23 r34 t24 t34-r24 t23 t24 t34^2,0},{(r23 t24)/Sqrt[2],-((r23 r24 r34)/Sqrt[2])+(t23 t34)/Sqrt[2],-((r34 t23)/Sqrt[2])-(r23 r24 t34)/Sqrt[2],(r34 t23 (-r24^2+t24^2))/Sqrt[2]-(r23 r24 t34)/Sqrt[2],(r23 r24 r34)/Sqrt[2]+(t23 (-r24^2+t24^2) t34)/Sqrt[2],r24 t23 t24,-Sqrt[2] r24 r34 t23 t24 t34-(r23 t24 (-r34^2+t34^2))/Sqrt[2],-r24 r34^2 t23 t24-r23 r34 t24 t34,r23 r34 t24 t34-r24 t23 t24 t34^2,0}}'


print(removing_nSqrt(MathematicaToLatex(separating_Big_list_fromMathem(a)),'L'))    # uncomment to print latex form of the solved big output list form mathematica













print('------END----------END---------END-----------END--------END-------------END---------END-----------END--')
























