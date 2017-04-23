import imageio as im

import numpy as np
import numpy.random as alea
a=im.imread("paysageCR.png")
print(a)
l=a.shape
b=np.zeros([int((l[0])/2),int((l[1])/2)])
print(b)

    
for i in range(0,int(l[0]/2)):
    for j in range(0,int(l[1]/2)):
        b[i][j]=(a[2*i][2*j]+a[2*i+1][2*j]+a[2*i][2*j+1]+a[2*i+1][2*j+1])/4
print(b)
print(b.shape)

m=b.shape
c=np.zeros([int(m[0])*2,int(m[1])*2])
print(c)
for k in range(0,int((m[0]))):
    for n in range(0,int((m[1]))):
        c[2*k][2*n]=int(b[k][n])
        c[2*k][2*n+1]=int(b[k][n])
        c[2*k+1][2*n]=int(b[k][n])
        c[2*k+1][2*n+1]=int(b[k][n])
print(c,type(c))
im.imsave("paysageCRdec.png",c)
        

        
