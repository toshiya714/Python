import math

class Cicle:
    def __init__(self, r):
        self.radius = r
        self.pi = math.pi
        print("Created")
        
    def cicle_area(self):
        return self.radius * self.radius * self.pi
    
cic1 = Cicle(10)
print(cic1.cicle_area())