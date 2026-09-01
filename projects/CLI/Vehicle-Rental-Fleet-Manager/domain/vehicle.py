from abc import ABC, abstractmethod

from domain.rental import Rental


class Vehicle(ABC):
    _next_id = 100

    def __init__(self, cost, late_rate):
        self._id = Vehicle._next_id
        Vehicle._next_id += 1
        self._cost = cost
        self._late_rate = late_rate
        self._history = []
        self._is_rented = False

    @property
    def id(self):
        return self._id

    @property
    def cost(self):
        return self._cost

    @property
    def late_rate(self):
        return self._late_rate

    @property
    def history(self):
        return list(self._history)

    @property
    def is_rented(self):
        return self._is_rented

    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @property
    @abstractmethod
    def _can_rent(self) -> bool:
        pass

    @abstractmethod
    def late_fee(self, days_late, baseCost) -> float:
        pass

    def to_dict(self) -> dict:
        return {
            "vehicle_type": self.vehicle_type,
            "id": self._id,
            "cost": self._cost,
            "late_rate": self._late_rate,
            "is_rented": self._is_rented,
            "history": [r.to_dict() for r in self._history],
        }

    def __str__(self) -> str:
        status = "rented" if self._is_rented else "available"
        return f"#{self.id} | {self.vehicle_type:<10} | ${self.cost:.2f}/day | {status}"


class Car(Vehicle):
    def __init__(self, cost=40, late_rate=1.2):
        super().__init__(cost, cost * late_rate)

    @property
    def vehicle_type(self):
        return "Car"

    @property
    def _can_rent(self):
        return not self._is_rented

    def late_fee(self, days_late, baseCost):
        return days_late * self._late_rate if days_late > 0 else 0


class Motorcycle(Vehicle):
    def __init__(self, cost=25, late_rate=0.15):
        super().__init__(cost, late_rate)

    @property
    def vehicle_type(self):
        return "Motorcycle"

    @property
    def _can_rent(self):
        return not self._is_rented

    def late_fee(self, days_late, baseCost):
        return baseCost * self._late_rate if days_late > 0 else 0


class Truck(Vehicle):
    def __init__(self, cost=65, late_rate=100):
        super().__init__(cost, late_rate)

    @property
    def vehicle_type(self):
        return "Truck"

    @property
    def _can_rent(self):
        return not self._is_rented

    def late_fee(self, days_late, baseCost):
        return self._late_rate if days_late > 0 else 0


def vehicle_from_dict(data):
    kind = data["vehicle_type"]
    if kind == "Car":
        vehicle = Car()
    elif kind == "Motorcycle":
        vehicle = Motorcycle()
    elif kind == "Truck":
        vehicle = Truck()
    else:
        raise ValueError(f"Unknown vehicle type: {kind}")

    vehicle._id = data["id"]
    vehicle._cost = data["cost"]
    vehicle._late_rate = data["late_rate"]
    vehicle._is_rented = data["is_rented"]
    vehicle._history = [Rental.from_dict(r) for r in data["history"]]
    return vehicle
