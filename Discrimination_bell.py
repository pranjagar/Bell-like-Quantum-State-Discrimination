# just to iterate over all possible output states and find unambiguous discrimination
# we'll paste huge outputs, modify into mathematica lists into python ones and iterate

import numpy as n
import matplotlib.pyplot as plt
import math as m
import sympy as sym
import scipy.constants as const




Biglist = [[[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]], [[1,2,3,4],[1,0,3,4],[1,0,3,4],[1,0,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]]
# second statelist contains three zeroes with one non-zero elt at position #2

def Discrimination(L):                         # L is a list (of lists of lists)
    listofcounterlists = []
    # print(f'L :{len(L)}')
    for i in range(len(L)):
        counterlist = []                                # counter for each output component for each possibility : increases by 1 for each non-zero output for a given output component
        # print(f'len(L[i][0] : {len(L[i][0])}')
        for k in range(len(L[i][0])):                         # tells to go over each output component
            counter = 0
            for j in range(len(L[i])):                  # it is saying we should go over all the output states, which is jsut the four output bell states
                if L[i][j][k] != 0:
                    counter = counter+1
            counterlist.append(counter)
        # print(f'conterlist : {counterlist}')
        listofcounterlists.append(counterlist)
    return listofcounterlists

Biglist = [[[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]], [[1,2,3,4],[1,0,3,4],[1,0,3,4],[1,0,3,4]],[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]]
print(f'ListofCounterLists: {Discrimination(Biglist)}')





print('_______________END________________BEGIN_________BEGIN________________BEGIN___________--')

































print('_______________END________________END_________END________________END___________--')


























































