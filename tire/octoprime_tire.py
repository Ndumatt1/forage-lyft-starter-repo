from tire.tire import Tire


class Octoprime(Tire):
    def __init__(self, wear_sensor_array):
        self.wear_sensor_array = wear_sensor_array

    def needs_service(self):
        value_sum = sum(self.wear_sensor_array)
        if value_sum >= 3: 
            return True
        return False