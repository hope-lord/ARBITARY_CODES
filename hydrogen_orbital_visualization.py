import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp

# hydrogen atom orbital
def orbital(n,l,m):
    def pdf(x,y,z):
        r = (x**2+y**2+z**2)**0.5 #distance
        t = np.arccos(z/r) # theta
        angular = sp.sph_harm(m,l,0,t).real**2

        r = r/n
        radial = r**(2*l)*sp.assoc_laguerre(2*r,n-l-1,2*l+1)**2 * np.exp(-2*r)
        return radial*angular

    return pdf




#coordinates
r0 = 10 #max distance
N=70
x=np.linspace(-r0,r0,N)
y=np.linspace(-r0,r0,N)
z=np.linspace(-r0,r0,N)
elements = []
p = []

n = 2   #principal quantum number
l = 1   #angular quantum number
m = 0   #magnetic quantum number

pdf = orbital(n,l,m)


for ix in x:
    for iy in y:
        for iz in z:
            #Serialize into 1D object
            elements.append(str((ix,iy,iz)))
            p.append(pdf(ix,iy,iz))
            
p = np.array(p)/sum(p)   #normalizing the discete probability
#Getting electron coordinates based on probabiliy
coord = np.random.choice(elements, size=100000, replace=True, p=p)

elem_mat = [i.split(',') for i in coord]
elem_mat = np.array(elem_mat)
x_coords = [float(i[1:]) for i in elem_mat[:,0]] 
y_coords = [float(i) for i in elem_mat[:,1]] 
z_coords = [float(i[0:-1]) for i in elem_mat[:,2]]
#Plotting
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_coords, y_coords, z_coords, alpha=0.25, s=3,color='red')
ax.set_title("$|\psi_{%d,%d,%d}|^2$ of Hydrogen atom"%(n,l,m))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
l = np.linspace(-1.1*r0,1.1*r0)
zero = np.zeros_like(l)
ax.plot3D(l,zero,zero,color='black',linewidth = 2)
ax.plot3D(zero,l,zero,color='black',linewidth = 2)
ax.plot3D(zero,zero,l,color='black',linewidth = 2)
ax.view_init(7,145)
plt.show()
