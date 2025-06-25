from utils import load_file, save_file

file_name = "tasks.json"

load_file(file_name)

task = [
    {
        "task_id": 1,
        "task_title": "Sample Task",
        "task_description": "This is a sample task description.",
        "task_status": "Pending",
        "task_due_date": None,
        "task_created_date": None,
        "task_status_updated_date": None
    }
]

save_file("tasks.json", task)
print(load_file("tasks.json"))