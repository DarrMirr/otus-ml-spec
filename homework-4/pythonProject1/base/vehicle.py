from exceptions import LowFuelError
from exceptions import NotEnoughFuel


class Vehicle:
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self._weight = weight
        self._started = started
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    def start(self):
        if not self._started:
            if self._fuel > 0:
                self._started = True
            else:
                raise LowFuelError()

    def move(self, distance: int):
        if not self._started:
            return
        if not self._is_fuel_enough(distance):
            raise NotEnoughFuel()

    def _is_fuel_enough(self, distance: int) -> bool:
        fuel_diff = self._fuel - (distance / 100 * self._fuel_consumption)
        return fuel_diff > 0
