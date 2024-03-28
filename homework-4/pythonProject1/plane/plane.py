from base.vehicle import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    _cargo: int = 0
    _max_cargo: int

    def __init__(self, max_cargo: int):
        super().__init__()
        self._max_cargo = max_cargo

    def load_cargo(self, cargo: int):
        new_cargo = self._cargo + cargo
        if new_cargo > self._max_cargo:
            raise CargoOverload()
        else:
            self._cargo = new_cargo

    def remove_all_cargo(self):
        cargo = self._cargo
        self._cargo = 0
        return cargo
