class DampedVariable:
    def __init__(self, offset, c, D):
        self.offset = offset
        self.c = c
        self.D = D
        
        self._x = 0
        self._previousX = 0
        self._v = 0
        
    def timestep(self):
        x_old = self._x
        v_old = self._v
        a_old = - self.D * x_old - self.c * v_old
       
        self._previousX = x_old
        
        x_new = x_old + v_old + a_old/2.0
        v_new = v_old + a_old
       
        self._x = x_new
        self._v = v_new
        
    def get_value(self):
        return self._x + self.offset
    
    def get_previous_value(self):
        return self._previousX + self.offset
    
    def set_value(self, x):
        self._x = x - self.offset
        
        
class Stick:
    def __init__(self, x0, y0, r_offset, r_c, r_D, phi_offset, phi_c, phi_D):
        self._r = DampedVariable(r_offset, r_c, r_D)    
        self._phi = DampedVariable(phi_offset, phi_c, phi_D)
        
        self._x0 = x0
        self._y0 = y0
   
    def timestep(self):
        self._r.timestep()
        self._phi.timestep() 
    
    @property        
    def r(self):
        return self._r.get_value()
        
    @property        
    def phi(self):
        return self._phi.get_value()
       
    @property        
    def previous_r(self):
        return self._r.get_previous_value()
        
    @property        
    def previous_phi(self):
        return self._phi.get_previous_value()
    
    @property        
    def x(self):
        return self.r * cos(self.phi) + self._x0
        
    @property        
    def y(self):
        return self.r * sin(self.phi) + self._y0
       
    @property        
    def previous_x(self):
        return self.previous_r * cos(self.previous_phi) + self._x0
        
    @property        
    def previous_y(self):
        return self.previous_r * sin(self.previous_phi) + self._y0
        
    
        