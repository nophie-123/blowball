class BlowballStick:
    alpha_phi = -0.05
    alpha_radius = -0.1
    
    def __init__(self, radius, phi, parent, crossSize = 15):
        self.phi0 = phi
        self.radius0 = radius
        
        self.phi = phi
        self.radius = radius + 10
        self.v_phi = 0
        self.v_radius = 0
        
        self.parent = parent
        self.crossSize = crossSize
        
    def getCartesianCoordinates(self):
        centerX = self.parent.centerX + self.radius*cos(self.phi)
        centerY = self.parent.centerY + self.radius*sin(self.phi)
        
        return centerX, centerY    
        
    def drawLine(self):
        strokeWeight(1)
        
        centerX, centerY = self.getCartesianCoordinates()
        line(self.parent.centerX, self.parent.centerY, centerX, centerY)
    
    def drawCrosses(self):
        strokeWeight(3)
        
        centerX, centerY = self.getCartesianCoordinates()
        line(centerX - self.crossSize/2.0, centerY - self.crossSize/2.0, centerX + self.crossSize/2.0, centerY + self.crossSize/2.0)
        line(centerX + self.crossSize/2.0, centerY - self.crossSize/2.0, centerX - self.crossSize/2.0, centerY + self.crossSize/2.0)
        
    def animate(self):
        
        a_radius = self.alpha_radius * (self.radius - self.radius0)
        a_phi = self.alpha_phi * (self.phi - self.phi0)
        
        self.radius = self.v_radius + a_radius/20.0 + self.radius
        self.phi = self.v_phi + a_phi/20.0 + self.phi
        
        self.v_radius = a_radius
        self.v_phi = a_phi
       
        

class Blowball:
    def __init__(self, centerX, centerY, diameter, bottomX = None):
        self.centerX = centerX
        self.centerY = centerY
        self.diameter = diameter
        if bottomX:
            self.bottomX = bottomX
        else:
           self.bottomX = self.centerX - 50
           
        self.crossSize = 15
        
        N = 45
        self.sticks = [BlowballStick(random(self.diameter/2.0 - 10, self.diameter/2.0), 2*PI/N*i + random(- 2*PI/N/5, 2*PI/N/5), self) for i in range(N)]
        self.sticks += [BlowballStick(random(0, self.diameter/2.0 - 10), PI/N*i + random(- PI/N/5, PI/N/5), self) for i in range(2*N)]
        
    def animate(self):
        for stick in self.sticks:
            stick.animate()
        
        
    def draw(self):
        strokeWeight(3)
        curve(self.bottomX, height, self.bottomX - 50, height, self.centerX, self.centerY, self.centerX + 400, 0)
        
        for stick in self.sticks:
            stick.drawLine()

        fill(255)
        ellipse(self.centerX, self.centerY, self.diameter/4.0, self.diameter/4.0)
        
        for stick in self.sticks:
            stick.drawCrosses()


b = Blowball(200, 200, 240)


def setup():
    size(800, 700)
    #frameRate(1)

def draw():
    background(255)
    b.animate()
    b.draw()