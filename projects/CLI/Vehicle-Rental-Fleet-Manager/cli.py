"""The only file allowed to print() and input(). No rental rules live here."""

from domain.exceptions import VehicleError
from storage.persistence import load_fleet, save_fleet

DATA_PATH = "data/vehicles.json"


def print_menu():
    print(
        """
=========================================
     FLEETTRACK - Main Menu
=========================================
  1. Register vehicle
  2. Rent out a vehicle
  3. Return a vehicle
  4. View vehicle details
  5. View rental history
  6. List all vehicles
  7. Remove a vehicle
  8. Save & quit
========================================="""
    )


def main():
    fleet = load_fleet(DATA_PATH)

    while True:
        print_menu()
        choice = input("> ").strip()

        try:
            if choice == "1":
                kind = input("Vehicle type (car/motorcycle/truck): ")
                vehicle = fleet.register_vehicle(kind)
                print(f"[OK] Registered #{vehicle.id} ({vehicle.vehicle_type})")

            elif choice == "2":
                vehicle_id = int(input("Vehicle ID: "))
                name = input("Customer name: ").strip()
                days = int(input("Days booked: "))
                if not name:
                    print("[!] Customer name can't be empty.")
                else:
                    fleet.rent_vehicle(vehicle_id, name, days)
                    print(
                        f"[OK] Vehicle #{vehicle_id} rented to {name} for {days} day(s)."
                    )

            elif choice == "3":
                vehicle_id = int(input("Vehicle ID: "))
                record = fleet.return_vehicle(vehicle_id)
                print(
                    f"[OK] Vehicle #{vehicle_id} returned. {record.days} day(s) used."
                    f" Total cost: ${record.cost:.2f}"
                )

            elif choice == "4":
                vehicle_id = int(input("Vehicle ID: "))
                vehicle = fleet.get_vehicle(vehicle_id)
                print(vehicle)

            elif choice == "5":
                vehicle_id = int(input("Vehicle ID: "))
                vehicle = fleet.get_vehicle(vehicle_id)
                print(f"\nHistory for #{vehicle.id} ({vehicle.vehicle_type}):")
                if not vehicle.history:
                    print("  (no rentals yet)")
                for record in vehicle.history:
                    print(f"  {record}")

            elif choice == "6":
                if not fleet.all_vehicles():
                    print("[!] No vehicles registered yet.")
                for vehicle in fleet.all_vehicles():
                    print(vehicle)

            elif choice == "7":
                vehicle_id = int(input("Vehicle ID: "))
                fleet.remove_vehicle(vehicle_id)
                print(f"[OK] Vehicle #{vehicle_id} removed.")

            elif choice == "8":
                save_fleet(fleet, DATA_PATH)
                print("[OK] Saved. Goodbye.")
                break

            else:
                print("[!] Unknown option.")

        except VehicleError as e:
            print(f"[!] {e}")
        except ValueError as e:
            print(f"[!] {e}")


if __name__ == "__main__":
    main()
