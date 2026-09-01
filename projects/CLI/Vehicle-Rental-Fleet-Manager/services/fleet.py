from datetime import datetime

from domain.exceptions import (
    ActionFailure,
    InvalidInput,
    VehicleNotFound,
    VehicleUnavailable,
)
from domain.rental import Rental
from domain.vehicle import Car, Motorcycle, Truck


class Fleet:
    def __init__(self):
        self._vehicles = {}

    def get_vehicle(self, vehicle_id):
        if vehicle_id not in self._vehicles:
            raise VehicleNotFound(f"Vehicle number #{vehicle_id} not found")
        return self._vehicles[vehicle_id]

    def add_vehicle(self, vehicle):
        self._vehicles[vehicle.id] = vehicle

    def all_vehicles(self):
        return list(self._vehicles.values())

    def register_vehicle(self, kind):
        kind = kind.strip().lower()
        if kind == "car":
            vehicle = Car()
        elif kind == "motorcycle":
            vehicle = Motorcycle()
        elif kind == "truck":
            vehicle = Truck()
        else:
            raise InvalidInput(f"Unknown type: {kind}")

        self.add_vehicle(vehicle)
        return vehicle

    def rent_vehicle(self, vehicle_id, customer_name, days):
        vehicle = self.get_vehicle(vehicle_id)
        if days <= 0:
            raise InvalidInput(f"Days must be positive, got {days}")
        if not vehicle._can_rent:
            raise VehicleUnavailable(f"Vehicle number #{vehicle_id} is not available")

        vehicle._is_rented = True
        record = Rental("rent", vehicle_id, customer_name, days)
        vehicle._history.append(record)
        return record

    def return_vehicle(self, vehicle_id):
        vehicle = self.get_vehicle(vehicle_id)
        if not vehicle.is_rented:
            raise ActionFailure(
                f"Vehicle number #{vehicle_id} is not currently rented"
            )

        rent_record = vehicle.history[-1]
        actual_days = (datetime.now() - rent_record.timestamp).days
        days_late = max(0, actual_days - rent_record.days)

        base_cost = actual_days * vehicle.cost
        fee = vehicle.late_fee(days_late, base_cost)
        total_cost = base_cost + fee

        vehicle._is_rented = False
        record = Rental(
            "return", vehicle_id, rent_record.name, actual_days, cost=total_cost
        )
        vehicle._history.append(record)
        return record

    def remove_vehicle(self, vehicle_id):
        vehicle = self.get_vehicle(vehicle_id)
        if vehicle.is_rented:
            raise ActionFailure(f"Can't Remove, Vehicle number #{vehicle_id} is rented")

        del self._vehicles[vehicle_id]
        return vehicle
