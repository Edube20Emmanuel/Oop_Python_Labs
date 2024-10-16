from my_Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, winter_tires = False):
        super().__init__(color)
        self.winter_tires = winter_tires

    def __str__(self):
        return 'This vehicle is %s \nHas winter tires: %s\
            ' %(self.get_color,self.winter_tires)

#car2 = Car('white',True)
#print(car2)