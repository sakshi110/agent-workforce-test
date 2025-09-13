import json
import os

RESERVATIONS = {}
SERVICES_FILE = os.path.join(os.path.dirname(__file__), "../problems/003/data/services.json")

def create_reservation(reservation_id, guest_name, date):
    RESERVATIONS[reservation_id] = {
        "guest_name": guest_name,
        "date": date,
        "services": []
    }
    return RESERVATIONS[reservation_id]

def get_reservation(reservation_id):
    return RESERVATIONS.get(reservation_id)

# Load available services
def load_services():
    with open(SERVICES_FILE, "r") as f:
        return json.load(f)

# Add service to reservation
def add_service_to_reservation(reservation_id, service_name):
    services = load_services()
    if service_name not in services:
        raise ValueError(f"Service '{service_name}' is not available.")

    reservation = RESERVATIONS.get(reservation_id)
    if not reservation:
        raise ValueError(f"Reservation {reservation_id} not found.")

    if service_name not in reservation["services"]:
        reservation["services"].append(service_name)

    return reservation
