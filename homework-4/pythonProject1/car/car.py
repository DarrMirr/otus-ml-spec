from base.vehicle import Vehicle
from engine.engine import Engine


class Car(Vehicle):
    _engine: Engine

    def set_engine(self, engine: Engine):
        self._engine = engine
