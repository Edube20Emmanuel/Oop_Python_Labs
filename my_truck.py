from my_Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, color, has_trailer = False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def __str__(self):
        return 'This vehicle is %s \nHas trailer: %s\
            ' %(self.get_color,self.has_trailer)
    
## Main program 
#truck = Truck('red')
#print(truck)