import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from celluloid import Camera
import random
import sys
def limit(xadd,xsub,yadd,ysub,xop,yop):
    if yadd>20 and xadd<20:
        xop=1
        yop=-1
    elif xadd>20 and ysub>-20:
        xop=-1
        yop=-1
    elif ysub<-20 and xsub>-20:
        xop=-1
        yop=1
    elif xsub<-20 and yadd<20:
        xop=1
        yop=1
    elif yadd==20 and xadd==20:
        xop=-1
        yop=-1
    elif ysub==-20 and xadd==20:
        xop=-1
        yop=1
    elif ysub==-20 and xsub==-20:
        xop=1
        yop=1
    elif yadd==20 and xsub==-20:
        xop=1
        yop=-1
    return xop,yop;
def infected(c,x,y,j,num):
    for i in range(0,num):
        if c[i]=='r':
            if x[j]<x[i]+0.5 and y[j]<y[i]+0.5 and y[j]>y[i]-0.5 and x[j]>x[i]-0.5:
                return True
    return False

def spread():
    num = 72
    color=[]
    for i in range(0,num):
        color.append('b')
    fig=plt.figure()
    ax=fig.add_subplot(111) # subplot of 1*1 grid
    ax.set_xlim(-20,20)     # setting the x and y axis limit
    ax.set_ylim(-20,20)
    camera = Camera(fig)    #creating the figure using and matplot and also creating a camera for taking saps of it
    x=[]
    y=[]
    pos=[1 for i in range(0,num)]
    xop=[random.choice([-1,1]) for i in range(0,num)] # randomly initialzing the the array by which the values of datapoints will increase along the x and y aixs
    yop=[random.choice([-1,1]) for i in range(0,num)]
    for i in range(0,num):
        x.append(random.randint(-20,20)) # randomly initialzing  the array x and y with the datapoints along the x and y axis
        y.append(random.randint(-20,20))
    color[1]='r' # selecting some people which are infected from the disease which will further infect the disease
    color[20]='r'
    color[10]='r'
    pos[1]=100
    pos[10]=100
    pos[20]=100
    for k in range(10000): # represents the time for which the code will run
        for i in range(0,num): # adding small values to the points in order to make them move
            xadd=x[i]+random.uniform(0,1)
            xsub=x[i]-random.uniform(0,1)
            yadd=y[i]+random.uniform(0,1)
            ysub=y[i]-random.uniform(0,1)
            xop[i],yop[i]=limit(xadd,xsub,yadd,ysub,xop[i],yop[i])
            if color[i]=='r' and (k+1)%pos[i]==0: # if the person is infected and specific time for it has passed so the person will die
                color[i]='k'
                pos[i]=pos[i]+20
            elif color[i]=='k' and (k+1)%pos[i]==0: # if the person is dead and  then after some specific time for it has passed the person will revive
                color[i]='b'
            x[i]=x[i]+xop[i]*random.uniform(0,1)
            y[i]=y[i]+yop[i]*random.uniform(0,1)
            if color[i]!='r':
                if infected(color,x,y,i,num):
                    color[i]='r'
                    pos[i]=k+100
        plt.scatter(x,y, c=color, s=50)
        camera.snap() # it will take repeatdly snaps of all the graphs
    anim = camera.animate(blit=True) # after that all the snaps are animated in such a way that the datapoints will see like moving
    plt.show()
spread()
