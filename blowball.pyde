class BlowballStick:
    def __init__(self, radius, phi, parent, crossSize = 15):
        
        self.centerX = parent.centerX + radius*cos(phi)
        self.centerY = parent.centerY + radius*sin(phi)
        
        self.parent = parent
        self.crossSize = crossSize
        
    def drawLine(self):
        strokeWeight(1)
        line(self.parent.centerX, self.parent.centerY, self.centerX, self.centerY)
    
    def drawCrosses(self):
        strokeWeight(3)
        line(self.centerX - self.crossSize/2.0, self.centerY - self.crossSize/2.0, self.centerX + self.crossSize/2.0, self.centerY + self.crossSize/2.0)
        line(self.centerX + self.crossSize/2.0, self.centerY - self.crossSize/2.0, self.centerX - self.crossSize/2.0, self.centerY + self.crossSize/2.0)
        

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
    frameRate(1)

def draw():
    background(255)
    
    b.draw()