from elements import Blowball


b = Blowball(300, 600, 400, -PI/2)


def setup():
    size(800, 700)
    frameRate(20)

def draw():
    background(255)
    
    b.animate()    
    b.draw()