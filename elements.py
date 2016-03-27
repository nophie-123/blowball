from numerics import Stick

class Blowball(Stick):

    def __init__(self, x0, y0, radius, phi):
        Stick.__init__(self, x0, y0, radius, 0.1, 0.1, phi, 0.1, 0.1)
        
        self.diameter = 240
        
        N = 45
        self.sticks = [BlowballStick(self, random(self.diameter/2.0 - 10, self.diameter/2.0), 2*PI/N*i + random(- 2*PI/N/5, 2*PI/N/5)) for i in range(N)]
        self.sticks += [BlowballStick(self, random(0, self.diameter/2.0 - 10), PI/N*i + random(- PI/N/5, PI/N/5)) for i in range(2*N)]

        self._phi._x = 0.9

    def draw(self):
        noFill()

        strokeWeight(6)
        stroke(200)
        curve(self._x0, self._y0, self._x0 - 50, self._y0, self.x, self.y, self.x + 400, 0)

        strokeWeight(2)
        stroke(0)
        curve(self._x0, self._y0, self._x0 - 50, self._y0, self.x, self.y, self.x + 400, 0)
        
        for stick in self.sticks:
            stick.drawLine()

        strokeWeight(1)
        stroke(0)
        fill(255)
        ellipse(self.x, self.y, self.diameter/4.0, self.diameter/4.0)
        
        for stick in self.sticks:
            stick.drawCrosses()
        
    def animate(self):
        
        #if random(0, 1) < 0.1:
        #    self._r._v += random(-0.5, 0.5)
        #if random(0, 1) < 0.1:
        #    self._phi._v += random(-0.001, 0.001)
                        
        self.timestep()
        
        for stick in self.sticks:
            stick.animate()
        
            
            
class BlowballStick(Stick):
    
    def __init__(self, parent, radius, phi):
        self._parent = parent
        self._crossSize = 15
        Stick.__init__(self, parent.x, parent.y, radius, 0.1, 0.05, phi, 0, 0)
               
    def drawLine(self):
        strokeWeight(1)
        line(self._parent.x, self._parent.y, self.x, self.y)
    
    def drawCrosses(self):
        strokeWeight(3)
        
        line(self.x - self._crossSize/2.0, self.y - self._crossSize/2.0, self.x + self._crossSize/2.0, self.y + self._crossSize/2.0)
        line(self.x + self._crossSize/2.0, self.y - self._crossSize/2.0, self.x - self._crossSize/2.0, self.y + self._crossSize/2.0)

    def animate(self): 
        old_x = self.x
        old_y = self.y
        
        parent_x = self._parent.x
        parent_y = self._parent.y
        
        x_diff = old_x - parent_x
        y_diff = old_y - parent_y
        
        new_r = sqrt(x_diff**2 + y_diff**2)
        
        self._r.set_value(new_r)
        # We do not set the phi correctly here, as we do not want a movement in this direction!
                                                    
        self.timestep()
        
        self._x0 = self._parent.x
        self._y0 = self._parent.y