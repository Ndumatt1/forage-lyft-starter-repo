from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery
        
    def needs_service(self):
        pass
