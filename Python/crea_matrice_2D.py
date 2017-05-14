import numpy.random as rd
import numpy as np
def creamat2D(L,C):
    a=rd.random_integers(0,255,L*C)
    M=[]
    for k in range(0,L*C):
        m=(a[k])
        M.append(m)
    #print(len(M))
    M=np.asarray(M)
    #print(len(M))
    M=np.reshape(M,(L,C))
    return M
        