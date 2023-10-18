import unittest
from datetime import datetime
from engine.engine_basemodel import Engine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.battery_basemodel import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestCapuletEngine(unittest.TestCase):
    def test_capulet_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_capulet_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_should_be_serviced(self):
        warning_light_is_on = True
        sternman = SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())

    def test_sternman_should_not_be_serviced(self):
        warning_light_is_on = False
        sternman = SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_willoughby_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())


class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin = NubbinBattery(last_service_date, today)
        self.assertTrue(nubbin.needs_service())

    def test_nubbin_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        nubbin = NubbinBattery(last_service_date, today)
        self.assertFalse(nubbin.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        spindler = SpindlerBattery(last_service_date, today)
        self.assertTrue(spindler.needs_service())

    def test_spindler_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spindler = SpindlerBattery(last_service_date, today)
        self.assertFalse(spindler.needs_service())


if __name__ == '__main__':
    unittest.main()