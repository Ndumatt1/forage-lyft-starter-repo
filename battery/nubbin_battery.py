from battery_basemodel import Battery
from datetime import datetime


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        current_date = self.current_date
        if service_threshold_date < current_date:
            return True
        return False