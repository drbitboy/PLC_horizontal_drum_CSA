import os
import sys
import math
import matplotlib.pyplot as plt

if "__main__" == __name__:
  L = L0 = float(('0.0'.split() +sys.argv[1:2]).pop())
  R = float(('1.0'.split() +sys.argv[2:3]).pop())
  cumarea = 0.0
  n = 1.0
  nfracareas = list()
  for i in range(20):
    #deltaarea = n * math.sqrt(((R-L)**3) * (R+L))
    deltaarea = n * (R-L) * math.sqrt((R*R) - (L*L))
    cumarea += deltaarea
    nfracareas.append((n,deltaarea/cumarea,))
    L = math.sqrt(R*(R + L)/2.0)
    n *= 2.0
    print((n,L,deltaarea,cumarea,))

  plt.plot(*zip(*[(nn,fracarea,) for nn,fracarea in nfracareas if fracarea>0.0]),'o')
  plt.yscale('log')
  #plt.xscale('log')
  plt.xlabel('2**N')
  plt.ylabel('fractional area of step N')
  plt.title('R={2}; L0={0}  Segment area~{1}~$\pi$'.format(L0,cumarea,R) + '\nFractional convergence $\Delta{CumulArea}/CumulArea$')
  plt.show()
