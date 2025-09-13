import sys
import json

data = json.load(sys.stdin)

# Check if there is at least one completed task
has_done = any(task["done"] for task in data["tasks"])

if has_done:
    print("✅ At least one task marked as done. Test passed.")
else:
    print("❌ No completed tasks found. Test failed.")
