class Garage:
    def __init__(self,):
        self.vehicle_parked = None

    def set_Vehicle(self,parked):
        self.vehicle_parked = parked

    def __str__(self):
        if self.vehicle_parked:
            return 'Description of parked vehicle:\n%s'\
                %(self.vehicle_parked)
        else:
            return 'There is no car parked in the garage'