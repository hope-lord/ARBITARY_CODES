#This is a simulation to appraoch pi from the concept of collision of boxes
#This takes lots of time to find the result.

from math import exp
#by the 3blue1brown simulation

class Box:
    def __init__(self,mass,velocity):
        self.mass=mass
        self.velocity=-velocity
        self.position=mass*1.0

#This function finds the velocities after the collision
def coll_velocity(b1,b2):
    momentum=b1.mass*b1.velocity+b2.mass*b2.velocity
    vel=b1.velocity-b2.velocity

    delta=b1.mass+b2.mass
    b2.velocity=(momentum+b1.mass*vel)/delta
    b1.velocity=(momentum-b2.mass*vel)/delta
    #print(b1.velocity)
   # print(b2.velocity)

#This function where the next collision is going to happen
def next_collision(b1,b2,click):
    time_b1_wall=0.0
    time_b1_b2=0.0
    if b1.velocity!=0:
        time_b1_wall = -(b1.position) / b1.velocity
    if b1.velocity!=b2.velocity:
        time_b1_b2 = (b1.position - b2.position) / (b2.velocity - b1.velocity)
        #print("It happens")
    if click==1:
            if time_b1_wall>0:
                b1.position=0.0
                b2.position+=b2.velocity*time_b1_wall
            else:
                b1.position=-1
    elif click==0 and time_b1_b2>0:
        b1.position+=b1.velocity*time_b1_b2
        b2.position=b1.position
    else:
        ''''print("founder")
        print(click)

        print(time_b1_b2)
        return'''''


#this function counts the collisions by recursion
def collision(b1,b2):
    
    if b1.position>b2.position or b1.position<0:
        return 0
    elif b1.velocity<b2.velocity and b1.velocity>0:
        return 0
    elif b1.position == b2.position==0:
        coll_velocity(b1, b2)
        b1.velocity = -b1.velocity
        b2.velocity = -b2.velocity
        print("ok")
        next_collision(b1, b2, -1)
        return collision(b1,b2)+2
    elif b1.position==b2.position:
        #collision happens
        coll_velocity(b1,b2)
        #if b1.velocity!=0 and b1.velocity!=b2.velocity:
        next_collision(b1,b2,1)
        return collision(b1,b2)+1
    elif b1.position==0:
        b1.velocity=-b1.velocity
        next_collision(b1,b2,0)
        return collision(b1,b2)+1
    
#same as collision but by loop
def coll(b1,b2):
    i=0
    while(b1.velocity<0 or b1.velocity>=b2.velocity):
        if b1.position==0:
            b1.velocity = -b1.velocity
            next_collision(b1, b2, 0)
            i+=1
        elif b1.position == b2.position:
            coll_velocity(b1, b2)
            if i==0:
                print("Velocity of b1=",b1.velocity)
                print("Velocity of b2=", b2.velocity)
            next_collision(b1, b2, 1)
            if i==0:
                print("pos of b1=", b1.position)
                print("pos of b2=", b2.position)
            i+=1
        else:
            print("why")
        #print("Velocity of b1=",b1.velocity)
        #print("comparison of b1-b2=",b1.velocity-b2.velocity,'\n \n')
    return i
def f(x):
    return 2.05761085*10**(-5)*exp(x*2.22517214) +10**(x/8)
i=int(input("Give the integer"))#int(input("Give the no. of digits you want"))
from time import perf_counter,time,localtime
t=time()+f(i)
print("wait", f(i), "secs")
#print("Wait till ",localtime(t).tm_wday,'Days',localtime(t).tm_hour,'hours',localtime(t).tm_min,'mins' ,localtime(t).tm_sec,'secs')


n=i*2
b1=Box(1,0.0)
b2=Box(10**n,10.0)
b1.position=10**n *1.0
t1=perf_counter()
#print("Initially")
#print("Velocity of b1=",b1.velocity)
#print("Velocity of b2=",b2.velocity,"\n")
col=coll(b1,b2)
print("pi approximation=",col/10**i)
print(perf_counter()-t1)


        
    
            
        
