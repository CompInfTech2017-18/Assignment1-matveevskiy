import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def systema(y,t):
    theta,omega = y
    dydt = [omega, 2.0 * np.sin(theta)]
    return dydt


class pplotter:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)      
    
        

    def plot(self, x, y, color):
        return self.ax.plot(x, y, color)
    
    def show(self):
        plt.show()

class telo:
    def __init__(self,m,vx,vy, mg,color,plotter):
        self.mass = m
        self.ispeed_x = vx
        self.ispeed_y = vy
        self.gforce = mg
        self.plotter = plotter
        self.color = color
        
    def getX(self, time):
        return self.ispeed_x * time
    
    def getY(self, time):
        return self.ispeed_y * time - self.gforce/(2.0*self.mass)*time*time
    
    def position(self):
        time=np.arange(0., 10.0, 0.1)
        xp = self.getX(time)
        yp = self.getY(time)
        plotter.plot(xp, yp, 'r')
        
class gantel(telo):
    def __init__(self,m,vx,vy, mg,R,Q,E,fi,theta,w,color,plotter):
        telo.__init__(self,m,vx,vy, mg,color,plotter)
        self.radius = R
        self.charge = Q
        self.field = E
        self.fa = fi
        self.ang = theta
        self.asp = w
        
    def an(self,time):
        y0 = [self.ang,  self.asp]
        b = self.charge * 2.0 * self.field / (self.radius * self.radius * self.mass)
        b = 1.0
        return odeint(systema,y0,time)[:,0]
        
    def getX(self, time):
        return self.ispeed_x * time + self.gforce/(2.0*self.mass)*time*time * np.sin(self.fa)
    
    def getY(self, time):
        return self.ispeed_y * time - self.gforce/(2.0*self.mass)*time*time * np.cos(self.fa)
    
    def getXX(self,time):
        return self.radius * np.cos(self.an(time))
    def getYY(self,time):
        return self.radius * np.sin(self.an(time))
    def position1(self):
        time=np.arange(0., 10.0, 0.1)
        xp =  self.getX(time)+self.getXX(time)
        yp =  self.getY(time)+self.getYY(time)
        plotter.plot(xp, yp, self.color)
        xp =  self.getX(time)-self.getXX(time)
        yp =  self.getY(time)+-self.getYY(time)
        plotter.plot(xp, yp, self.color)
        
plotter = pplotter()
'telo1 = telo(1.0,1.0,3.0,1.0,'r',plotter)'

telo2 = gantel(1.0,0.1,0.5,1.0,0.7,1.0,0.1,0.0,np.pi-0.5,0.5,'g',plotter)
telo2.position()
telo2.position1()