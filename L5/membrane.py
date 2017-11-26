"""
Created on Wed Apr 22 15:53:00 2015

Charging and discharging curves for passive membrane patch
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt

# input current
I = 10 # nA

# capacitance and leak resistance

# Questions 2:
# Change the values for the membrane's resistance and capacitance (R and C),
# and find out how this influences the response of the membrane. Does it reach
# a stable value more quickly or more slowly after multiplying R by 5?
#R = 100 * 5 # M ohms

# Original
R = 100 # M ohms

# Question 3:
# Does it reach a stable value more quickly or more slowly after dividing C by 10?
C = 0.1 / 10.# nF

# Original
#C = 0.1 # nF

# Question 4:
# Does it reach a stable value more quickly or more slowly after multiplying R
# by 10 AND dividing C by 10?
C = 0.1 / 10.
R = 100 * 10.

tau = R*C # = 0.1*100 nF-Mohms = 100*100 pF Mohms = 10 ms
print('C = %.3f nF' % C)
print('R = %.3f M ohms' % R)
print('tau = %.3f ms' % tau)
print('(Theoretical)')

# membrane potential equation dV/dt = - V/RC + I/C

# QUESTIONS:
# What if the current were not turned off? What would the steady state voltage
# of the membrane be?
# Use the values given in the script to compute your answer (C = 0.1 nF,
# R = 100 MΩ, I = 10 nA). You should give your answer in mV. Do not include
# units in your answer.
#tstop = 15000 # ms

# Original
tstop = 150 # ms

V_inf = I*R # peak V (in mV)
tau = 0 # experimental (ms)

h = 0.2 # ms (step size)

V = 0 # mV
V_trace = [V] # mV

for t in np.arange(h, tstop, h):

   # Euler method: V(t+h) = V(t) + h*dV/dt
   V = V +h*(- (V/(R*C)) + (I/C))

   # Verify membrane time constant
   if (not tau and (V > 0.6321*V_inf)):
     tau = t
     print('tau = %.3f ms' % tau)
     print('(Experimental)')

   
   # Stop current injection 
   if t >= 0.6*tstop:
     I = 0

   V_trace += [V]

# Why draw this every 10th time?
#if t % 10 == 0:
plt.plot(np.arange(0,t+h, h), V_trace, color='r')
plt.xlim(0, tstop)
plt.ylim(0, V_inf)
plt.xlabel('Time[ms]')
plt.ylabel('Voltage[mV]')
plt.draw()

plt.show()
