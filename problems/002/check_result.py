import sys
import json
from datetime import datetime

def main():
    # Read agent output from stdin
    data = sys.stdin.read().strip()
    
    try:
        result = json.loads(data)
    except json.JSONDecodeError:
        print("❌ Invalid JSON output")
        sys.exit(1)

    # Reservations should NOT be in January
    reservations = result.get("reservations", [])
    for r in reservations:
        date_str = r.get("date")
        if not date_str:
            continue
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date.month == 1:  # January = 1
            print("❌ Reservation created in January! Test failed.")
            sys.exit(1)

    print("✅ No January reservations. Test passed.")

if __name__ == "__main__":
    main()
