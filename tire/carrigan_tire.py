from tire.tire import Tire


class Carrigan(Tire):
    def __init__(self, wear_sensor_array):
        self.wear_sensor_array = wear_sensor_array
    
    def needs_service(self):
        return any(wear >= 0.9 for wear in self.wear_sensor_array)
        #if should_service:
            #return True
        #return False
        '''for value in self.wear_sensor_array:
            if float(value) >= 0.9:
                return True
            return False'''