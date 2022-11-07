# Research_Hunter
PLEASE SEE THE 'MAIN' BRANCH FOR CURRENT VERSION OF CODE.

Research related to quantum information carried out at Hunter College, City University of New York.

The code solves the following problem and handles the related output data:

Problem: Given four different light paths (ex. optical fibres) and arbitrary beam splitters intertwining these paths, what will be the general ouput of
an arbitrary two photon quantum state? There are ten different possibilities of inputting two photons through the four input paths (not 16, due to the
indistinguishability of photons) and the output state will be unknown superpositions of these ten possibilites. A program that gives us this output for
corresponding input states is same as a 10 by 10 unitary operator in the above basis. Thus, we can also find the results for input Bell states and use
it to loop over some physically chosen suitable values of beam splitters such that we find outputs where three Bell states are discriminated unambiguously
rather than just two. 

The python files above execute the above, and also convert input and output data to Mathematica from Python and vice versa. Our code involves use of 
libraries numpy, sympy and mostly relies on string and list manipulations.
