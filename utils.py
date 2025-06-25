from datetime import date
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

def save_file(file_name, task):
    """Save a JSON file with the given content."""
    try:
        with open(file_name, 'w') as f:
            json.dump(task, f, indent=4)
    except IOError as e:
        print(f"❌ Error saving file '{file_name}': {e}")
    

def task_id_generator(tasks): 
    """Generate a unique task ID based on existing tasks."""
    try:
        if not tasks:
            return 1
        else:
            return max(task['task_id'] for task in tasks) + 1
    except Exception as e:
        print(f"❌ Error in task_id_generator: {e}")
        
def format_date():
    try:
        return date.today().strftime('%Y-%m-%d')
    except Exception as e:
        print(f"❌ Error in format_date: {e}")

def notify_user_overdue(task_due_date):
    """Notify the user if a task is overdue."""
    try:
        today = date.today().strftime('%Y-%m-%d')
        if task_due_date < today:
            print(f"Task due date {task_due_date} is overdue!")
    except Exception as e:
        print(f"❌ Error in notify_user_overdue: {e}")

def delete_task(task_id):
    """Delete a task by its ID."""
    try:
        tasks = load_file("tasks.json")
        for task in tasks:
            if task['task_id'] == task_id:
                index_task = tasks.index(task)
                del tasks[index_task] 
                print(f"Task with ID {task_id} deleted successfully.")
                save_file("tasks.json", tasks)
            else: print(f"Task with ID {task_id} not found.")
    except Exception as e:
        print(f"❌ Error in delete_task: {e}")

def update_task_status(task_id, new_status):
    """Update the status of a task by its Id."""
    try:
        tasks = load_file("tasks.json")
        for task in tasks:
            if task[task_id] == task_id:
                task['task_status'] = new_status
                task['task_status_updated_date'] = format_date()
                print(f"Task with {task['task_status']} status updated to {new_status}.")
                save_file("tasks.json", tasks)
                return tasks
            else:
                print(f"Task with ID {task_id} not found.")
    except Exception as e:
        print(f"❌ Error in update_task_status: {e}")









