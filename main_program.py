## Import modules in the main program
from my_Vehicle import *
from Car import *
from my_truck import *
from my_garage import *
from my_garage_tester import *


## Running the main program
car1 = Vehicle('blue')
print(car1)
print('_'*50,'\n')
car2 = Car('white',True)
print(car2)
print('_'*50,'\n')
truck = Truck('red')
print(truck)