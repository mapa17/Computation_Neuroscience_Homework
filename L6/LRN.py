import numpy as np
from pudb import set_trace as st

W = np.matrix([[0.6, 0.1, 0.1, 0.1, 0.1], \
               [0.1, 0.6, 0.1, 0.1, 0.1],
               [0.1, 0.1, 0.6, 0.1, 0.1],
               [0.1, 0.1, 0.1, 0.6, 0.1],
               [0.1, 0.1, 0.1, 0.1, 0.6]])

M = np.matrix([[-0.5, 0.0, 0.5, 0.5, 0.0], \
               [0.0, -0.5, 0.0, 0.5, 0.5],
               [0.5, 0.0, -0.5, 0.0, 0.5],
               [0.5, 0.5, 0.0, -0.5, 0.0],
               [0.0, 0.5, 0.5, 0.0, -0.5]])

u = np.matrix([0.6, 0.5, 0.6, 0.2, 0.1])
u = u.T

h = W * u

evalues, e = np.linalg.eig(M)

print('Max eigenvalue %2.2f'%max(evalues))

vss_comp = []
for eW, eV in zip(evalues, [e[:, x] for x in range(len(evalues))]):
    vss_comp.append((np.inner(h,eV))/(1.0 - eW) * eV)

vss = sum(vss_comp)
print('Vss = %s' % vss)

#vss_len = np.sqrt(sum([x*x for x in vss_comp]))
#print('Normalized vss = %2.2f' % vss/vss_len)

vss_norm = np.multiply(vss, 1./np.sqrt(np.sum(np.inner(vss, vss).diagonal())))
print('Normalized vss = %s' % vss_norm)