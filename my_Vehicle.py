class Vehicle:
    def __init__(self, color):
        self.color = color

    @property
    def get_color(self):
        return self.color.title()
    
    def __str__(self):
        return 'This vehicle is %s' %(self.get_color)
    
#car1 = Vehicle('blue')
#print(car1)