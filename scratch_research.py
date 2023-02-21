def avg_prob_with_confidence(confidence = 1, index_15k = False, index_729 = False ,theta = 45,four_list_compared = False, machine_uncertainty = .001,  priors = [.25,.25,.25,.25]):     # index_15k is a ith elt of list big_phi_abstract, index_729 for big_phi_abstract_729, machine_uncertainty is to account for error in numerical computations 
    if index_15k != False:
        splitters = Data.big_phi_abstract[index_15k]
        four_list_compared = cfn.Four_list(splitters, compared= True, theta = theta)
    elif index_729 != False:
        splitters = Data.big_phi_abstract_729[index_729]
        four_list_compared = cfn.Four_list(splitters, compared= True, theta = theta)

    c_threshold = confidence-machine_uncertainty
    avg_prob_at_confidence = 0
    # i index for states - 0,1,2,3
    # j index for detectors - 0,1,2,...,9
    
    # detector j click prob = sum_i ( eta_i*a_(ij)^2) .. Ex [.5,0,.5,0] will give .25*.5^2+.25*.5^2

    detector_prob_list = []             # creating list of the ten detector prob - denoted p_i in the theory work
    for j in range(10):
        for i in range(4):
            detector_prob = sum([priors[k]*(four_list_compared[j][k])**2 for k in range(4)])
            detector_prob_list.append(detector_prob)

    for i in range(4):
        sum_cij_pj = 0
        for j in range(10):
            c_ij = ((four_list_compared[j][i])**2/detector_prob_list[j]) 
            if c_ij >= c_threshold:
                sum_cij_pj += c_ij
        avg_prob_at_confidence += priors[i]*sum_cij_pj       

    return avg_prob_at_confidence

           