import numpy as np
import math as m
import sympy as sym
import random as rand
import Functions_module_beta as fn
import Data
from Functions_module_beta import MatrixAction, SystemAction




def Bell_like_C(theta = 'theta', state_number = 'all'):          # to generate a list of bell-like coeffs' lists that are functions of the angle (degrees), default theta gives symbolic results, state_number (starts with 1 not 0) is in order to select a particular states' coeffs
    if theta == 'theta':
        theta = sym.symbols('theta')
    phiplus_like_C = [sym.cos(fn.radians(theta)),sym.sin(fn.radians(theta))]              #Bell-like coeffs ie. disturbing C slightly away from the perfect ones in bell states, like theta degrees instead of theta
    phiminus_like_C = [sym.sin(fn.radians(theta)), -sym.cos(fn.radians(theta))]
    psiplus_like_C = [sym.cos(fn.radians(theta)),sym.sin(fn.radians(theta))]
    psiminus_like_C = [sym.sin(fn.radians(theta)), -sym.cos(fn.radians(theta))]
    bell_like_C = [phiplus_like_C,phiminus_like_C,psiplus_like_C,psiminus_like_C]
    if state_number != 'all':
        return bell_like_C[state_number-1]
    return bell_like_C
    #Bell_like_C(45, state_number= 1) >>>  [sqrt(2)/2, sqrt(2)/2] 
    #Bell_like_C()                    >>>  [[cos(pi*theta/180), sin(pi*theta/180)], [sin(pi*theta/180), -cos(pi*theta/180)], [cos(pi*theta/180), sin(pi*theta/180)], [sin(pi*theta/180), -cos(pi*theta/180)]]
    #Bell_like_C(40)                  >>>  [[cos(2*pi/9), sin(2*pi/9)], [sin(2*pi/9), -cos(2*pi/9)], [cos(2*pi/9), sin(2*pi/9)], [sin(2*pi/9), -cos(2*pi/9)]]
    

def Bell_like_V(theta = sym.symbols('theta'), state_number = 'all'):          #to generate list of vectors of each bell like state.angle is obsolete, included jsut for sake of similarity
    phiplus_like_V = [fn.ten_states_2,fn.ten_states_5]                      
    phiminus_like_V = [fn.ten_states_2,fn.ten_states_5]
    psiplus_like_V = [fn.ten_states_3,fn.ten_states_4]
    psiminus_like_V = [fn.ten_states_3,fn.ten_states_4]

    bell_like_V = [phiplus_like_V,phiminus_like_V,psiplus_like_V,psiminus_like_V]
    if state_number != 'all':
        return bell_like_V[state_number-1]
    return bell_like_V
    #Bell_like_V()                    >>> [[[1, 0, 1, 0], [0, 1, 0, 1]], [[1, 0, 1, 0], [0, 1, 0, 1]], [[1, 0, 0, 1], [0, 1, 1, 0]], [[1, 0, 0, 1], [0, 1, 1, 0]]]
    #Bell_like_V(20, state_number= 4) >>>   [[1, 0, 1, 0], [0, 1, 0, 1]]




def Four_list(splitter_comb = [0,0,0,0,0,0], theta = 'theta', roundoff = True, compared = False):     # splitter comb is a six-list of the six splitters, change to 'BL' for bell like, change to True for rounding, compared to True if want in output-by-output comparison format 
    if roundoff == True and theta == 'theta':
        print('Wait a minute!!! You are trying to round off an abstract calculation!!! Give a number to "theta" argument if you want to roundoff, or manually set "roundoff" argument to False!!')
    four_list = [(fn.SystemAction(Bell_like_V(theta, state_number = i), Bell_like_C(theta, state_number = i),splitter_comb, 34, roundoff)[1]) for i in range(1,5)]      # list comprehension, looping from state 1-4. Creates 'raw list' ie. list of four lists of 10 elts, each sublist is output prob-amps of an input state at the ten detectors                                       
    if compared == False:
        return four_list
    else:
        compared_four_list = [[four_list[i][j] for i in range(4)] for j in range(10)]       #creating the compared version ie. list of ten lists of four elts, each sublist is an output detector with prob amps of the four states to make it click
        return compared_four_list
    # Four_list(Data.big_phi_abstract[1405] , theta = 33)    >>>  [[0.0, 0.0, 0.0, 0.14701, 0.0, 0.0, 0.38511, -0.48907, -0.48907, 0.59302], [0.0, 0.0, 0.0, 0.69165, 0.0, 0.0, -0.59302, 0.10395, 0.10395, 0.38511], [-0.10395, 0.10395, -0.69165, 0.0, -0.10395, -0.10395, 0.0, -0.48907, 0.48907, 0.0], [-0.48907, 0.48907, 0.14701, 0.0, -0.48907, -0.48907, 0.0, 0.10395, -0.10395, 0.0]]     # gives bell-like states' outputs when angle is 33 degrees, in raw format
    # Four_list(Data.big_phi_abstract[1405] , theta = 33,compared= True)   >>> [[0.0, 0.0, -0.10395, -0.48907], [0.0, 0.0, 0.10395, 0.48907], [0.0, 0.0, -0.69165, 0.14701], [0.14701, 0.69165, 0.0, 0.0], [0.0, 0.0, -0.10395, -0.48907], [0.0, 0.0, -0.10395, -0.48907], [0.38511, -0.59302, 0.0, 0.0], [-0.48907, 0.10395, -0.48907, 0.10395], [-0.48907, 0.10395, 0.48907, -0.10395], [0.59302, 0.38511, 0.0, 0.0]]       # same but in compared format
    # Four_list(Data.big_phi_abstract[1405] ,compared= True, roundoff = False )  # gives compared list of the output prob amps that are abstract here 




def Confidence(L, port = 1, state_number = 'all' , priors = [.25,.25,.25,.25]):       # L is an output 'compared' list (ie. list of 10 lists of each 4 elts), port is the output number for which confidence is to be calctd: by default 1,priors is a list of 4 the prior prob of the four input states- by default [.25,.25,.25,.25]
    A = L[port-1]         # port starts from 1, not zero
    denominator_prob = sum([priors[j]*(A[j])**2 for j in range(len(A))])
    confidence = [(priors[i]*(A[i])**2 )/denominator_prob for i in range(len(A))]
    if state_number != 'all':
        return confidence[state_number-1]
    return confidence


""" 
def avg_prob_with_confidence(confidence = 1, index_15k = False, index_729 = False ,theta = 45, four_list_compared = False, machine_uncertainty = .001,  priors = [.25,.25,.25,.25]):     
# index_15k is a ith elt of list big_phi_abstract, index_729 for big_phi_abstract_729, machine_uncertainty is to account for error in numerical computations 
    if priors != [.25,.25,.25,.25]:
        if sum(priors) != 1:
            print('YO! Priors dont add to 1!! \n \n ') 
    if index_15k != False:
        splitters = Data.big_phi_abstract[index_15k]
        four_list_compared = Four_list(splitters, compared= True, theta = theta)
    elif index_729 != False:
        splitters = Data.big_phi_abstract_729[index_729]
        four_list_compared = Four_list(splitters, compared= True, theta = theta)
    print(four_list_compared)
    c_threshold = confidence-machine_uncertainty
    avg_prob_at_confidence = 0
    # i index for states - 0,1,2,3, j index for detectors - 0,1,2,...,9
    # detector j click prob = sum_i ( eta_i*a_(ij)^2) .. Ex [.5,0,.5,0] will give .25*.5^2+.25*.5^2
    detector_prob_list = []             # creating list of the ten detector prob - denoted p_i in the theory work
    for j in range(10):
        detector_prob = sum([priors[i]*(four_list_compared[j][i])**2 for i in range(4)])
        if detector_prob == 0:
            detector_prob_list.append(1)
        else:
            detector_prob_list.append(detector_prob)
    for i in range(4):
        sum_cij_pj = 0
        for j in range(10):
            c_ij = (priors[i]*(four_list_compared[j][i])**2/detector_prob_list[j]) 
            if c_ij >= c_threshold:
                sum_cij_pj += c_ij*detector_prob_list[j]
        avg_prob_at_confidence += sum_cij_pj       
    return avg_prob_at_confidence
    # avg_prob_with_confidence(index_15k=1405)      # prob for index 1405 from the big splitter list in Data. Returns the avg prob = .5
    # avg_prob_with_confidence(index_729= 200, theta = 43, confidence = .98)



 """




"""
# original function, untouched, working. Next, more general one is the next one.
def avg_prob_with_confidence_original(confidence = 1, index_15k = False, index_729 = False ,theta = 45, four_list_compared = False, machine_uncertainty = .001,  priors = [.25,.25,.25,.25]):     
# index_15k is a ith elt of list big_phi_abstract, index_729 for big_phi_abstract_729, machine_uncertainty is to account for error in numerical computations 
    if priors != [.25,.25,.25,.25]:
        if sum(priors) != 1:
            print('YO! Priors dont add to 1!! \n \n ') 
    if index_15k != False:
        splitters = Data.big_phi_abstract[index_15k]
        four_list_compared = Four_list(splitters, compared= True, theta = theta)
    elif index_729 != False:
        splitters = Data.big_phi_abstract_729[index_729]
        four_list_compared = Four_list(splitters, compared= True, theta = theta)
#     print(four_list_compared)
    c_threshold = confidence-machine_uncertainty
    avg_prob_at_confidence = 0
    # i index for states - 0,1,2,3, j index for detectors - 0,1,2,...,9
    # detector j click prob = sum_i ( eta_i*a_(ij)^2) .. Ex [.5,0,.5,0] will give .25*.5^2+.25*.5^2
    detector_prob_list = []             # creating list of the ten detector prob - denoted p_i in the theory work
    for j in range(10):
        detector_prob = sum([priors[i]*(four_list_compared[j][i])**2 for i in range(4)])
        if detector_prob == 0:
            detector_prob_list.append(1)
        else:
            detector_prob_list.append(detector_prob)
    for i in range(4):
        sum_cij_pj = 0
        for j in range(10):
            c_ij = (priors[i]*(four_list_compared[j][i])**2/detector_prob_list[j]) 
            if c_ij >= c_threshold:
                sum_cij_pj += c_ij*detector_prob_list[j]
        avg_prob_at_confidence += sum_cij_pj       
    return avg_prob_at_confidence
    # avg_prob_with_confidence(index_15k=1405)  # chooses 1405th entry from the big_phi_abstract list from 'Data' file, which is a list of six splitters; and computes the average prob with the confidence parameter for the corresponding four_list of that splitter list
    # avg_prob_with_confidence(index_729= 200, theta = 40, confidence = .97)
"""









def avg_prob_with_confidence(confidence = 1, custom_splitters = False, index_15k = False, index_729 = False ,theta = 45, four_list_compared = False, raw_four_list = False ,machine_uncertainty = .001,  priors = [.25,.25,.25,.25]):     
    """
    four_list_compared can have both compared and raw four lists as input, in case latter just set raw_four_list to True.
    
    confidence variable is the threshold, = 1 for unambiguous discrimination
    
    index_15k is a ith elt of list big_phi_abstract, index_729 for big_phi_abstract_729, machine_uncertainty is to account 
    for error in numerical computations 
    """
    if priors != [.25,.25,.25,.25]:
        if sum(priors) != 1:
            print('Error. Priors dont add to 1!! \n \n ') 
    
    if index_15k != False:
        splitters = Data.big_phi_abstract[index_15k]
    elif index_729 != False:
        splitters = Data.big_phi_abstract_729[index_729]
    elif custom_splitters != False:
        splitters = custom_splitters

    if four_list_compared is False:              # if this is given then good, if not we construct the list using the splitter list
        four_list_compared = Four_list(splitters, compared= True, theta = theta)

    if raw_four_list is True:
        four_list_compared = [[i[j] for i in list(four_list_compared)] for j in range(len(four_list_compared[0]))]  # converting compared into raw

    # if index_15k and four_list_compared != False:
    #     print('Error! Give only one of the splitter combination and four list, not both!') 
    # elif index_15k and index_729 != False:    
    #     print('Error! Give only one of the indices 15k/729, not both!') 
    c_threshold = confidence-machine_uncertainty
    avg_prob_at_confidence = 0
    # i index for states - 0,1,2,3, j index for detectors - 0,1,2,...,9
    # detector j click prob = sum_i ( eta_i*a_(ij)^2) .. Ex [.5,0,.5,0] will give .25*.5^2+.25*.5^2
    detector_prob_list = []             # creating list of the ten detector prob - denoted p_i in the theory work
    for j in range(10):
        detector_prob = sum([priors[i]*(four_list_compared[j][i])**2 for i in range(4)])
        if detector_prob == 0:
            detector_prob_list.append(1)
        else:
            detector_prob_list.append(detector_prob)
    for i in range(4):
        sum_cij_pj = 0
        for j in range(10):
            c_ij = (priors[i]*(four_list_compared[j][i])**2/detector_prob_list[j]) 
            if c_ij >= c_threshold:
                sum_cij_pj += c_ij*detector_prob_list[j]
        avg_prob_at_confidence += sum_cij_pj       
    return avg_prob_at_confidence
    # avg_prob_with_confidence(index_15k=1405)  # chooses 1405th entry from the big_phi_abstract list from 'Data' file, which is a list of six splitters; and computes the average prob with the confidence parameter for the corresponding four_list of that splitter list
    # avg_prob_with_confidence(index_729= 200, theta = 40, confidence = .97)

















############################################################################################
####################################################################################
############################################################################################
####################################################################################
############################################################################################
####################################################################################
############################################################################################
####################################################################################

""" 




bell_V = [fn.phiplus_V,fn.phiminus_V,fn.psiplus_V,fn.psiminus_V]
bell_C = [fn.phiplus_C,fn.phiminus_C,fn.psiplus_C,fn.psiminus_C]


mirror_list = [12,13,14,23,24,34]


#Chekcs out:  phiplus



def radians(degrees):           # degrees  to radians
    rad = (sym.pi/180)*degrees
    return rad 


#######_Definitions_######

theta = sym.symbols('theta')
theta = 45                                          # theta in degrees, default 45 gives Bell states

phiplus_like_V = [fn.ten_states_2,fn.ten_states_5]                      #Bell-like vectors
phiminus_like_V = [fn.ten_states_2,fn.ten_states_5]
psiplus_like_V = [fn.ten_states_3,fn.ten_states_4]
psiminus_like_V = [fn.ten_states_3,fn.ten_states_4]

phiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]              #Bell-like coeffs ie. disturbing C slightly away from the perfect ones in bell states, like theta degrees instead of theta
phiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]
psiplus_like_C = [sym.cos(radians(theta)),sym.sin(radians(theta))]
psiminus_like_C = [sym.sin(radians(theta)), -sym.cos(radians(theta))]

bell_like_V = [phiplus_like_V,phiminus_like_V,psiplus_like_V,psiminus_like_V]           # making lists of bell-like vectos (and coeffs) so easier to change them as arguments later
bell_like_C = [phiplus_like_C,phiminus_like_C,psiplus_like_C,psiminus_like_C]





zz = fn.SystemAction(bell_V[0],bell_C[0], [0,sym.pi/2,sym.pi/4,0,0,0], 34, True)[1]

mirr = Data.big_phi_abstract[100]

def four_list(splitter_comb, Bell_or_BellLike = 'B', rounding = False, compared = False):     # splitter comb is a six-list of the six splitters, change to 'BL' for bell like, change to True for rounding, compared to True if want in output-by-output comparison format 
    if Bell_or_BellLike == 'B':
        Bell_V = bell_V
        Bell_C = bell_C
    else:
        Bell_V = bell_like_V
        Bell_C = bell_like_C
    four_list = []
    for i in range(4):
        bell_out_C = fn.SystemAction(Bell_V[i],Bell_C[i], splitter_comb, 34, rounding)[1]
        four_list.append(bell_out_C)
    compared_four_list = [[four_list[i][j] for i in range(4)] for j in range(10)]
    if compared == False:
        return four_list
    else:
        return compared_four_list


# dd = fn.SystemAction(bell_V[0],bell_C[0], mirr, 34, True)[1]
# print(dd)
# print(four_list(mirr))
# print(fn.AvgProbability(four_list(mirr)))


good_avg_prob_choices = []
best_avg_prob_choices = []
for i in range(2978,len(Data.big_phi_abstract)):
    mirr = Data.big_phi_abstract[i]
    avg = fn.rounding([fn.AvgProbability(four_list(mirr))])[0]
    if avg >= .24:
        good_avg_prob_choices.append([avg,i])
        if avg > .49:
            best_avg_prob_choices.append([avg,i])
            
print(f'Best avg prob choices = {best_avg_prob_choices}')                      # works. gives list of pairs [avg_prob,i] where avg is the avg prob of the four list corresp to the ith splitter comb of the splitter comb list in Data.py 

# choice = 2230
# print(f'choice {choice} : {four_list(Data.big_phi_abstract[choice], rounding = True)}')
# print(f'choice {choice} compared : {four_list(Data.big_phi_abstract[choice], rounding = True, compared = True)}')


# about first one third of the best choices, each with avg_prb 0.5 = [886,888,896,898,930,932,934,940,942,944,980,982,984,990,992,994,1136,1138,1146,1148,1180,1182,[ 1667], 1669,1670,1671,1672,1673,1674,1676,1678,1700,1702,1704,1705,1707,1709,1710,1711,1712,1713,1714,1715,1717,1719,1720,1721,1722,1723,1724,1726,1728,2136,
# 2138,2146,2148,2180,2182,2184,2190,2192,2194,2230,2232,2234,2240,2242,2244,2386,2388,2396,2398,2430,2432,2434,2440,2442,2444,2480,2482,2484,2490,2492,2494,2626,2628,2650,2652,2654,2655,2657,2659,2660,2661,2662,2663,2664,2665,2667,2669,2670,2671,2672,2673,2674,2676,2678,2700,2702,2704,2705,2707,2709,2710,2711,2712,2713,2714,
# 2715,2717,2719,2720,2721,2722,2723,2724,2726,2728,2876,2878,2900,2902,2904,2905,2907,2909,2910,2911,2912,2913,2914,2915,2917,2919,2920,2921,2922,2923,2924,2926,2928,2950,2952,2954,2955,2957,2959,2960,2961,2962,2963,2964,2965,2967,2969,2970,2971,2972,2973,2974,2976,2978]



#[1405,1407,1409,1411,1413,1415,1417,1419,1421,1423,1455,1457,1459,1461,1463,1465,1467,1469,1471,1473,1655,1657,1659,1661,1663,1665,1667,1669,1671,1673,1705,1707,1709,1711,1713,1715,1717,1719,1721,1723,2655,2657,2659,2661,2663,2665,2667,2669,2671,2673,2705,2707,2709,2711,2713,2715,2717,2719,2721,2723,2905,2907,2909,2911,2913,2915,2917,2919,2921,2923,2955,2957,2959,2961,2963,2965,2967,2969,2971,2973,7655,7657,7659,7661,7663,7665,7667,7669,7671,7673,7705,7707,7709,7711,7713,7715,7717,7719,7721,7723,7905,7907,7909,7911,7913,7915,7917,7919,7921,7923,7955,7957,7959,7961,7963,7965,7967,7969,7971,7973,8905,8907,8909,8911,8913,8915,8917,8919,8921,8923,8955,8957,8959,8961,8963,8965,8967,8969,8971,8973,9155,9157,9159,9161,9163,9165,9167,9169,9171,9173,9205,9207,9209,9211,9213,9215,9217,9219,9221,9223,13905,13907,13909,13911,13913,13915,13917,13919,13921,13923,13955,13957,13959,13961,13963,13965,13967,13969,13971,13973,14155,14157,14159,14161,14163,14165,14167,14169,14171,14173,14205,14207,14209,14211,14213,14215,14217,14219,14221,14223,15155,15157,15159,15161,15163,15165,15167,15169,15171,15173,15205,15207,15209,15211,15213,15215,15217,15219,15221,15223,15405,15407,15409,15411,15413,15415,15417,15419,15421,15423,15455,15457,15459,15461,15463,15465,15467,15469,15471,15473]







 """



















