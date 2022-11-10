from lib2to3.pygram import Symbols
from re import A
import sympy as sym
import numpy as np
import math as m

def Output_states_list(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34):
    # f below is a list of four elts, each one is the general output of an input bell state    
    f= [[r24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))+t24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)),r34*(-r24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2)))+t34*(-r23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)+t23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)),-r34*(-r23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14)+t23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12))+t34*(-r24*(r23*((1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14+(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))),r12*r13*t13*t14**2+r14*t12*t13*t14,r34*(np.sqrt(2)*r24*t24*(r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(-r12*r13*r23**2*t13+r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)))+t34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))),-r34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2)))+t34*(np.sqrt(2)*r24*t24*(r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(-r12*r13*r23**2*t13+r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))),r24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14)+np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23),-np.sqrt(2)*r34*t34*(-r12*r13*t13*t23**2-r23*t12*t13*t23)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))+(-r34**2+t34**2)*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))),r34**2*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))+np.sqrt(2)*r34*t34*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(-r12*r13*t13*t23**2-r23*t12*t13*t23),r34**2*(-r12*r13*t13*t23**2-r23*t12*t13*t23)-np.sqrt(2)*r34*t34*(-r24*(-np.sqrt(2)*r12*r13*r23*t13*t23+(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r24**2*(-r12*r13*r23**2*t13+r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14-(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r14**2*t13-r14*t12*t13*t14))],[r24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))+t24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)),r34*(-r24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2)))+t34*(-r23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)),-r34*(-r23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12))+t34*(-r24*(r23*(-(1/np.sqrt(2))*r12*t14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r14-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r14*t13*t14+(1/np.sqrt(2))*t12*t13*(-r14**2+t14**2))),-r12*r13*t13*t14**2+r14*t12*t13*t14,r34*(np.sqrt(2)*r24*t24*(-r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(r12*r13*r23**2*t13-r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)))+t34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))),-r34*(r24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))+t24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2)))+t34*(np.sqrt(2)*r24*t24*(-r12*r13*r14**2*t13-r14*t12*t13*t14)-np.sqrt(2)*r24*t24*(r12*r13*r23**2*t13-r23*t12*t13*t23)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))),r24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14)+np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23),-np.sqrt(2)*r34*t34*(r12*r13*t13*t23**2+r23*t12*t13*t23)+np.sqrt(2)*r34*t34*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))+(-r34**2+t34**2)*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14))),r34**2*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))+np.sqrt(2)*r34*t34*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r12*r13*t13*t23**2+r23*t12*t13*t23),r34**2*(r12*r13*t13*t23**2+r23*t12*t13*t23)-np.sqrt(2)*r34*t34*(-r24*(np.sqrt(2)*r12*r13*r23*t13*t23-(1/np.sqrt(2))*t12*t13*(-r23**2+t23**2))+t24*(-r23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12)+t23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)))+t34**2*(r24**2*(r12*r13*r23**2*t13-r23*t12*t13*t23)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r14*(-r13**2+t13**2)-(1/np.sqrt(2))*r13*t12*t14)+t23*(-(1/np.sqrt(2))*r12*t14+(1/np.sqrt(2))*r13*r14*t12))+t24**2*(-r12*r13*r14**2*t13-r14*t12*t13*t14))],[r24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)+t24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)),r34*(-r24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12))+t24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14))+t34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))),-r34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12)+t23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2)))+t34*(-r24*(r23*(-(1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14+(1/np.sqrt(2))*r14*t12))+t24*((1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)),r34*(np.sqrt(2)*r24*t24*(-r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)))+t34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)),-r34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23))+t34*(np.sqrt(2)*r24*t24*(-r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))),r24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13)+np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13),-np.sqrt(2)*r34*t34*(r12*r23*t13*t23-r13*t12*t13*t23**2)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13))+(-r34**2+t34**2)*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))),r34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13))+np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2),r34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2)-np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14)+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r14*t13*t14+r13*r14**2*t12*t13)),r12*r14*t13*t14+r13*t12*t13*t14**2],[r24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)+t24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)),r34*(-r24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12))+t24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14))+t34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))),-r34*(-r23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12)+t23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2)))+t34*(-r24*(r23*((1/np.sqrt(2))*r12*r13*r14+(1/np.sqrt(2))*t12*t14*(-r13**2+t13**2))+t23*(-(1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12))+t24*(-(1/np.sqrt(2))*r12*t13*(-r14**2+t14**2)-np.sqrt(2)*r13*r14*t12*t13*t14)),r34*(np.sqrt(2)*r24*t24*(r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)))+t34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)),-r34*(r24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))+t24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23))+t34*(np.sqrt(2)*r24*t24*(r12*r14*t13*t14+r13*r14**2*t12*t13)-np.sqrt(2)*r24*t24*(-r12*r23*t13*t23-r13*r23**2*t12*t13)+(-r24**2+t24**2)*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))),r24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13)+np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13),-np.sqrt(2)*r34*t34*(r12*r23*t13*t23-r13*t12*t13*t23**2)+np.sqrt(2)*r34*t34*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13))+(-r34**2+t34**2)*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2)))),r34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13))+np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2),r34**2*(r12*r23*t13*t23-r13*t12*t13*t23**2)-np.sqrt(2)*r34*t34*(-r24*(-(1/np.sqrt(2))*r12*t13*(-r23**2+t23**2)-np.sqrt(2)*r13*r23*t12*t13*t23)+t24*(-r23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14)+t23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))))+t34**2*(r24**2*(-r12*r23*t13*t23-r13*r23**2*t12*t13)-np.sqrt(2)*r24*t24*(r23*((1/np.sqrt(2))*r12*r13*t14-(1/np.sqrt(2))*r14*t12*(-r13**2+t13**2))+t23*((1/np.sqrt(2))*r12*r13*r14-(1/np.sqrt(2))*t12*t14))+t24**2*(r12*r14*t13*t14+r13*r14**2*t12*t13)),-r12*r14*t13*t14+r13*t12*t13*t14**2]]
    return f

def Dummy(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34):
    # f below is a trial
    f= t12+r12+t13+r13+t14+r14+t23+r23+t24+r24+t34+r34
    return f


possible_values = [0, 1/(np.sqrt(2)), -1/(np.sqrt(2)),-1,1]

# possible_values = [0, -1, 1, sym.symbols('x'), sym.symbols('y')]

# realized_values = [1, 0, sym.symbols('x_'), sym.symbols('y_')]
# def Test():
#     for i in range(len(possible_values)):
#         t12 = possible_values[i]
#         r12 = realized_values[i]
#         for j in range(len(possible_values)):
#             t13 = possible_values[j]
#             r13 = realized_values[j]
#             for k in range(len(possible_values)):
#                 t14 = possible_values[k]
#                 r14 = realized_values[k]
#                 for l in range(len(possible_values)):
#                     t23 = possible_values[l]
#                     r23 = realized_values[l]
#                     for m in range(len(possible_values)):
#                         t24 = possible_values[m]
#                         r24 = realized_values[m]
#                         for n in range(len(possible_values)):
#                             t34 = possible_values[n]
#                             r34 = realized_values[n]
#                             print(Output_states_list(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34).subs([(x, 1/np.sqrt(2)), (y, -1/np.sqrt(2))]))
                           
                            
                        
# Test()
# t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34 = sym.symbols("t12, r12, t13, r13, t14, r14, t23, r23, t24, r24, t34, r34")



#k = len(possible_values)
# for i in range(len(possible_values)):
#     t12 = possible_values[i]
#     r12 = np.sqrt(1-possible_values[i]**2)
#     for j in range(len(possible_values)):
#         t13 = possible_values[j]
#         r13 = np.sqrt(1-possible_values[j]**2)
#         for k in range(len(possible_values)):
#             t14 = possible_values[k]
#             r14 = np.sqrt(1-possible_values[k]**2)
#             for l in range(len(possible_values)):
#                 t23 = possible_values[l]
#                 r23 = np.sqrt(1-possible_values[l]**2)
#                 for m in range(len(possible_values)):
#                     t24 = possible_values[m]
#                     r24 = np.sqrt(1-possible_values[m]**2)
#                     for n in range(len(possible_values)):
#                         t34 = possible_values[n]
#                         r34 = np.sqrt(1-possible_values[n]**2)
#                         Huge_List = Output_states_list(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34)
#                         for o in range(len(Huge_List)):
#                             for p in range(len(Huge_List[o])):                           
#                                 if Huge_List[o][p] < 1e-10 and Huge_List[o][p] > -1e-10:
#                                     Huge_List[o][p] = 0   
#                                 elif Huge_List[o][p] > 0.48 and Huge_List[o][p] < 0.55:
#                                     Huge_List[o][p] = .5                                   
#                                 elif Huge_List[o][p] < -0.48 and Huge_List[o][p] > -0.55:
#                                     Huge_List[o][p] = -.5
#                                 elif Huge_List[o][p] >.24 and Huge_List[o][p] < .25:
#                                     Huge_List[o][p] = .25
#                                 elif Huge_List[o][p] < -.24 and Huge_List[o][p] > -.25:
#                                     Huge_List[o][p] = -.25
                                    
#                         print(Huge_List)
                        
def equalszero(num):
    if num < 1e-10 and num > -1e-10:              #approximates 0; can be changed accordingly if need be
        return True
    return False
good_lists = []
coeff_list = []
point_threshold = 6                      # The threshold for how many outputs satisfy the condition that 1 non-zero, and 3 zeros
for i in range(len(possible_values)):                   
    t12 = possible_values[i]
    r12 = np.sqrt(1-possible_values[i]**2)
    for j in range(len(possible_values)):
        t13 = possible_values[j]
        r13 = np.sqrt(1-possible_values[j]**2)
        for k in range(len(possible_values)):
            t14 = possible_values[k]
            r14 = np.sqrt(1-possible_values[k]**2)
            for l in range(len(possible_values)):
                t23 = possible_values[l]
                r23 = np.sqrt(1-possible_values[l]**2)
                for m in range(len(possible_values)):
                    t24 = possible_values[m]
                    r24 = np.sqrt(1-possible_values[m]**2)
                    for n in range(len(possible_values)):
                        t34 = possible_values[n]
                        r34 = np.sqrt(1-possible_values[n]**2)
                        Huge_List = Output_states_list(t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34)
                        points = 0
                        for i in range(10):                                                         
                            if not equalszero(Huge_List[0][i]) and equalszero(Huge_List[1][i]) and equalszero(Huge_List[2][i]) and equalszero(Huge_List[3][i]):
                                points = points + 1
                            elif equalszero(Huge_List[0][i]) and not equalszero(Huge_List[1][i]) and equalszero(Huge_List[2][i]) and equalszero(Huge_List[3][i]):
                                points = points + 1
                            elif equalszero(Huge_List[0][i]) and equalszero(Huge_List[1][i]) and not equalszero(Huge_List[2][i]) and equalszero(Huge_List[3][i]):
                                points = points + 1
                            elif equalszero(Huge_List[0][i]) and equalszero(Huge_List[1][i]) and equalszero(Huge_List[2][i]) and not equalszero(Huge_List[3][i]):
                                points = points + 1
                        if points >= point_threshold:
                            # good_lists.append(([t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34], Huge_List)) 
                            good_lists.append(Huge_List)
                            # coeff_list.append([t12,r12,t13,r13,t14,r14,t23,r23,t24,r24,t34,r34])       #If one would want to see the list of coefficients corresponding to the good_lists
                
# print(good_lists[1][0])
# print(good_lists[1][1])
# print(good_lists[1][2])
# print(good_lists[1][3])

for i in range(len(good_lists)):
    Huge_List = good_lists[i]
    for o in range(len(Huge_List)):
        for p in range(len(Huge_List[o])):                           
            if Huge_List[o][p] < 1e-10 and Huge_List[o][p] > -1e-10:
                Huge_List[o][p] = 0   
            elif Huge_List[o][p] > 0.48 and Huge_List[o][p] < 0.55:
                Huge_List[o][p] = .5                                   
            elif Huge_List[o][p] < -0.48 and Huge_List[o][p] > -0.55:
                Huge_List[o][p] = -.5
            elif Huge_List[o][p] >.24 and Huge_List[o][p] < .25:
                Huge_List[o][p] = .25
            elif Huge_List[o][p] < -.24 and Huge_List[o][p] > -.25:
                Huge_List[o][p] = -.25
# print(len(good_lists))  
# print(good_lists)


def Discrimination(L, out = 'dis'):                         # L is a list (of lists of lists), set out to 'modes' for fn to return which choices and output modes are perfectly discriminating 
    listofdiscrimnations = []
    instances = []
    # print(f'L :{len(L)}')
    for i in range(len(L)):
        counterlist = []                                # counter for each output component for each possibility : increases by 1 for each non-zero output for a given output component
        discrimination_list = []
        # print(f'len(L[i][0] : {len(L[i][0])}')
        for k in range(len(L[i][0])):                         # tells to go over each output component
            counter = 0
            discrimination_position = 0                         # will add to this value for the ones that are non-zero. for the unambigous this value will coninceide with the state that is discriminated
            for j in range(len(L[i])):                  # it is saying we should go over all the output states, which is jsut the four output bell states
                if L[i][j][k] != 0:
                    counter = counter+1
                    discrimination_position=+ j             # (can add j+1 instead if we want starting from 1 instead of from 0 )
            counterlist.append(counter)
            discrimination_list.append(discrimination_position)
        # print(f'conterlist : {counterlist}')
        # listofcounterlists.append(counterlist)
        # listofdiscrimnationpositions.append(discrimination_list)
        discriminated_ones = []
        for s in range(len(counterlist)):
            if counterlist[s] == 1:
                instances.append(f'Choice # {i}, output # {s}, discriminates #{discrimination_list[s]+1}')            # remember starts from zero, not one. # also +1 in discrimination part is for starting at 1. 'Bell state 1' refers to psi+, 2 to psi-, 3 to phi+, 4 to phi-.
                discriminated_ones.append(discrimination_list[s]+1)
        if discriminated_ones != []:
            # if 1 in discriminated_ones and 2 in discriminated_ones and 3 in discriminated_ones and 4 in discriminated_ones:
            listofdiscrimnations.append(f' choice # {i}, discriminated : {(discriminated_ones)}')
    if out == 'dis':
        return listofdiscrimnations
    elif out == 'modes':
        return instances




# print(f'ListofCounterLists: {Discrimination(good_lists)}')
ListofCounterLists = Discrimination(good_lists)

# print(len(ListofCounterLists))

for i in range(len(ListofCounterLists)):
    counter = 0
    