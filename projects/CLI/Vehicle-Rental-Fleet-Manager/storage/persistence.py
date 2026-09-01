import json
import os

from domain.vehicle import Vehicle, vehicle_from_dict
from services.fleet import Fleet


def save_fleet(fleet, path):
    data = {
        "next_id": Vehicle._next_id,
        "vehicles": [v.to_dict() for v in fleet.all_vehicles()],
    }

    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def load_fleet(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return Fleet()

    with open(path) as f:
        data = json.load(f)

    fleet = Fleet()
    for item in data["vehicles"]:
        fleet.add_vehicle(vehicle_from_dict(item))

    # Restored after rebuilding, not before — every constructor call inside
    # vehicle_from_dict bumps Vehicle._next_id, so setting the saved value
    # first would just get pushed right back up as the vehicles rebuild.
    Vehicle._next_id = data["next_id"]

    return fleet
