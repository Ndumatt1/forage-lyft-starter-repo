from battery_basemodel import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        service_threshold_date = self.__last_service_date.replace(year=self.__last_service_date.year + 4)
        current_date = self.__current_date
        if service_threshold_date < current_date:
            return True
        else:
            return False

