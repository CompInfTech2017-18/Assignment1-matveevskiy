import numpy as np
import matplotlib.pyplot as plt

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
    def __init__(self,m,vx,vy, mg,R,Q,Ex,Ey,theta,w,color,plotter):
        telo.__init__(self,m,vx,vy, mg,color,plotter)
        self.radius = R
        self.charge = Q
        self.field_x = Ex
        self.field_y = Ey
        self.ang = theta
        self.asp = w
        
    def getX(self, time):
        return self.ispeed_x * time
    
    def getY(self, time):
        return self.ispeed_y * time - self.gforce/(2.0*self.mass)*time*time
    
    def getXX(self,time):
        return self.radius * np.cos(self.ang + time * self.asp )
    def getYY(self,time):
        return self.radius * np.sin(self.ang + time * self.asp )
    def position1(self):
        time=np.arange(0., 10.0, 0.1)
        xp = self.getX(time) + self.getXX(time)
        yp = self.getY(time) + self.getYY(time)
        plotter.plot(xp, yp, self.color)
        xp = self.getX(time) - self.getXX(time)
        yp = self.getY(time) - self.getYY(time)
        plotter.plot(xp, yp, self.color)
        
plotter = pplotter()
'telo1 = telo(1.0,1.0,3.0,1.0,'r',plotter)'

telo2 = gantel(1.0,1.0,0.0,1.0,0.7,1.0,0.2,0.2,0.5,2.0,'g',plotter)
telo2.position()
telo2.position1()