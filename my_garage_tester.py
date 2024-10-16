from my_garage import Garage
from my_truck import *
class Garage_Tester:
    @staticmethod
    def get_example():
        truck = Truck("black", True)
        garage = Garage()
        garage.set_Vehicle(truck)
        return garage
    

## Main program
#garage = Garage_Tester.get_example()
#print(garage)