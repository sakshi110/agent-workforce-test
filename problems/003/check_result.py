import sys
sys.path.append("src")
import reservation_server

def run_check():
    # Step 1: Create test reservation
    reservation_server.create_reservation("R123", "Alice", "2025-09-15")

    # Step 2: Add services
    reservation_server.add_service_to_reservation("R123", "breakfast")
    reservation_server.add_service_to_reservation("R123", "parking")

    # Step 3: Validate
    reservation = reservation_server.get_reservation("R123")
    services = reservation.get("services", [])

    if "breakfast" in services and "parking" in services:
        print("✅ Services successfully added to reservation R123.")
        return True
    else:
        print("❌ Failed to add services to reservation R123.")
        return False

if __name__ == "__main__":
    run_check()

