import datetime
import json

def load_file(file_name):
    """Load a JSON file and return its content."""
    try:
        with open(file_name, 'r') as f:
            task = json.load(f)
    except FileNotFoundError:
        print(f"File {file_name} not found. Creating a new task file.")
        task = []
    except json.JSONDecodeError as e:
        print(f"❌ JSON decode error in '{file_name}': {e}")
        task = []
    return task
    