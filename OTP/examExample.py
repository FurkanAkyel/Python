import math
class Nokta:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def pozisyon(self):
        return self.x, self.y
    def hareket(self,x,y):
        self.x += x
        self.y += y
    def mesafe(self,pt):
        dx = pt.x -self.x
        dy = pt.y -self.y
        return math.sqrt(dx**2 + dy**2)
p1 = Nokta(2,3)
p2 = Nokta(3,3)
print(p1.pozisyon())
print(p2.pozisyon())
p1.hareket(10,-10)
print(p1.pozisyon())
print(p2.pozisyon())
print(p1.mesafe(p2))