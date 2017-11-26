from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt
import sys


# input current
#I = 1 # nA
#I = 0.32 # nA
I = float(sys.argv[2]) # nA

# capacitance and leak resistance
C = 1 # nF
R = 40 # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method

V = 0
tstop = 200
abs_ref = 5 # absolute refractory period 
ref = 0 # absolute refractory period counter
V_trace = []  # voltage trace for plotting
V_th = 10 # spike threshold

nSpikes = 0
for t in range(tstop):

    # Question 1:
    # What is the largest current that will fail to cause the neuron to spike?
    # Give your answer in pA and round down to the nearest 10 pA. Do not include units in your answer.
    # You should vary the input current gradually from very low to high values
    # to find this value and then validate your answer with an analytical solution.
    #I *= 0.991
    print('t=%f, I=%f' % (t, I))

    if not ref:
        V = V - (V/(R*C)) + (I/C)
    else:
        ref -= 1
        V = 0.2 * V_th # reset voltage
   
    if V > V_th:
        V = 50 # emit spike
        ref = abs_ref # set refractory counter
        nSpikes+=1

    V_trace += [V]

print('Had %d spikes in %f ms = %f sp/sec' % (nSpikes, tstop, (nSpikes/tstop)*1000))
plt.plot(V_trace)
plt.savefig(sys.argv[1], dpi=200)
plt.show()