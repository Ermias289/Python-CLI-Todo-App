import json
import os
import datetime


def load_tasks(file_path):
    """Load tasks from a JSON file."""
    if not os.path.exists(file_path):
        print(f"⚠️ File {file_path} is missing or empty. Returning empty dict.")
        return {}

    if os.path.getsize(file_path) == 0:
        print(f"⚠️ File {file_path} is empty. Returning empty dict.")
        return {}

    try:
        with open(file_path, 'r') as file:
            tasks = json.load(file)
            if isinstance(tasks, dict):
                return tasks
            else:
                print("⚠️ File content is not a dictionary. Returning empty dict.")
                return {}
    except json.JSONDecodeError:
        print("⚠️ Error decoding JSON. Returning empty dict.")
        return {}
