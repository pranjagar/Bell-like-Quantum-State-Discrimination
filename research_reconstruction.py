import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand
import Functions_module_beta as fn
import Data

from Functions_module_beta import MatrixAction, SystemAction


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

def four_list(splitter_comb, Bell_or_BellLike = 'B', rounding = False):     # splitter comb is a six-list of the six splitters, change to 'BL' for bell like, change to True for rounding 
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
    return four_list



# dd = fn.SystemAction(bell_V[0],bell_C[0], mirr, 34, True)[1]
# print(dd)
# print(four_list(mirr))
# print(fn.AvgProbability(four_list(mirr)))


good_avg_prob_choices = []
best_avg_prob_choices = []
for i in range(len(Data.big_phi_abstract)):
    mirr = Data.big_phi_abstract[i]
    avg = fn.rounding([fn.AvgProbability(four_list(mirr))])[0]
    if avg >= .24:
        good_avg_prob_choices.append([avg,i])
        if avg > .49:
            best_avg_prob_choices.append([avg,i])
            
# print(best_avg_prob_choices)                      # works. gives list of pairs [avg,i] where avg is the avg prob of the four list corresp to the ith splitter comb of the splitter comb list in Data.py 








































