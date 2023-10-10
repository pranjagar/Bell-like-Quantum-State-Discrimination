import numpy as np
import pandas as pd
import math as m
import sympy as sym
import random as rand
import matplotlib.pyplot as plt
import Functions_module_beta as fn
import custom_functions_01 as cf
import Data
from custom_functions_01 import Four_list
from custom_functions_01 import avg_prob_with_confidence
from custom_functions_01 import avg_prob_with_confidence_alternative
from Functions_module_beta import SystemAction



# defining gradient function
def Gradient_modified(splitters, c = 1, quantity = 'avgprob' , angle_theta = 45,  delta = .001, machine_precision = .001 , priors_list = [.25,.25,.25,.25]):
    [a,b,c,d,e,f] = [i for i in splitters]
    initial_avg_prob = avg_prob_with_confidence_alternative(confidence = c, quantity= quantity , custom_splitters= splitters, index_15k= False, index_729= False, theta = angle_theta, four_list_compared= False, raw_four_list= False, machine_uncertainty = machine_precision, priors = priors_list)
    partial_a = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a+delta,b,c,d,e,f], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta
    partial_b = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a,b+delta,c,d,e,f], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta
    partial_c = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a,b,c+delta,d,e,f], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta
    partial_d = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a,b,c,d+delta,e,f], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta
    partial_e = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a,b,c,d,e+delta,f], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta
    partial_f = (avg_prob_with_confidence_alternative(c, quantity,  custom_splitters= [a,b,c,d,e,f+delta], theta= angle_theta, machine_uncertainty = machine_precision, priors = priors_list)- initial_avg_prob)/delta

    Gradient = [partial_a,partial_b,partial_c,partial_d,partial_e,partial_f]
    return Gradient
    # print(Gradient_modified([m.pi/2,0,m.pi/4,m.pi/4,m.pi/2,0] , c = 1, quantity = 'avgprob' , angle_theta = 45,  delta = .001, machine_precision = .001 , priors_list = [.25,.25,.25,.25]))  # Ex.


# defining Gradient search function for a given confidence and theta values. Possible "loss" functions : 'avgprob', ''
def GDSearch_modified(starting_point = [0,0,0,0,0,0], quantity = 'avgprob' , c_threshold = 1, theta = 45, iterations = 25, step = .01, calculations = False, calc_precision = .0001 , priors = [.25,.25,.25,.25], deriv_delta = .0001, double_deriv_method = False, random_step = False, adaptive_step = True ):
    new_splitters = starting_point 
    
    for i in range(iterations):
        grad = Gradient_modified(splitters = new_splitters, quantity= quantity, c = c_threshold, angle_theta = theta, machine_precision = calc_precision , priors_list = priors, delta = deriv_delta)
        
        # if random_step == True and [abs(i) < 1e-6 for i in grad]:
        #     index_choice = np.random.choice(6)
        #     new_splitters[index_choice] += -(0.1)

        # if double_deriv_method == True and [abs(i) < 1e-6 for i in grad]:    # the double deriv clause
        #     double_deriv = Double_deriv(splitters = [m1,m2,m3,m4,m5,m6], c = c_threshold, angle_theta = theta, machine_precision = calc_precision , priors_list = priors, delta = deriv_delta)
        #     # above gives the six double derivateives. We can use these to decide which direction to make a large move in.
        #     if [abs(i) < 1e-6 for i in double_deriv]:
        #         new_splitters = [(new_splitters[i]+ (10*step)) for i in range(6)]
        #     else:
        #         new_splitters = [(new_splitters[i]+ (10*step)*double_deriv[i]) for i in range(6)]
        
        # if double_deriv_method == False and random_step == False:
        if adaptive_step != False:
            new_splitters = [(new_splitters[i]+ step*(m.copysign(1,grad[i]))) for i in range(6)]        # the copysign thing is just finding the sign.
            print("yo")
        else:
            new_splitters = [(new_splitters[i]+ step*grad[i]) for i in range(6)]                    # adaptive rate - step depends on gradient size
            print("adaptive")

# possible ways to reduce calculations  - 

        if calculations == True:        # if need to analyze, shows intermediate steps
            print(f"\n gradient = {grad}")
            # if double_deriv_method == True:
            #     print(f"double_derivatives_list = {double_deriv}")
            print(f"Splitter_{i}= {new_splitters}")

    max_quant_splitters = new_splitters
    max_quant = avg_prob_with_confidence_alternative(custom_splitters = new_splitters, quantity = quantity , confidence= c_threshold, index_15k= False, index_729= False, theta= theta, four_list_compared= False, raw_four_list= False, machine_uncertainty= calc_precision, priors= priors)

    if calculations == True : print('starting_point = {starting_point}')      # to compare starting and final points
    if calculations == True :  # for showing intermediate steps
        starting_quant = avg_prob_with_confidence_alternative(custom_splitters = starting_point, quantity = quantity , confidence= c_threshold, index_15k= False, index_729= False, theta=theta, four_list_compared= False, raw_four_list= False, machine_uncertainty= calc_precision, priors= priors)
        final_quant    = avg_prob_with_confidence_alternative(custom_splitters = max_quant_splitters, quantity = quantity , confidence= c_threshold, index_15k= False, index_729= False, theta=theta, four_list_compared= False, raw_four_list= False, machine_uncertainty= calc_precision, priors= priors)
        if starting_quant != 0: 
            fractioanl_increase = (final_quant- starting_quant)/starting_quant       # not actually percent increaswe coz dividing by the final prob instead of starting prob.
        else:
            fractioanl_increase = 'Inf. (division by zero)'       # not actually percent increaswe coz dividing by the final prob instead of starting prob.
        print(f"starting quantity = {starting_quant}, result max quantity = {final_quant}, percent increase = {fractioanl_increase*100} ")

    return [max_quant, max_quant_splitters]       # the resultant maximum probability and the corresponding splitters
    # Example Use
    # s = [m.pi/2,0,m.pi/4,m.pi/4,m.pi/2,0]   # Ex. optimal splitters
    # GDSearch_modified(starting_point = s , c_threshold = 1 , quantity= 'avgprob', theta = 45, iterations = 10, step = .01, calculations = True, calc_precision = .0001 , priors = [.25,.25,.25,.25], deriv_delta = .0001)


# maybe add double derivatives inside if condition- in case its already a minima point with first deriv = 0. 