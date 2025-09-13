import json

# Example: pretend we are generating a list of tasks
tasks = {
    "tasks": [
        {"id": "T1", "title": "Finish project", "done": False},
        {"id": "T2", "title": "Review code", "done": True}
    ]
}

print(json.dumps(tasks))
