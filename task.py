from utils import format_date, task_id_generator, notify_user_overdue, delete_task, update_task_status, load_file, save_file

class Task:
    def __init__(self):
        """Initialize a new task with default values."""
        self.task_id = None
        self.task_title = None
        self.task_description = None
        self.task_status = None
        self.task_due_date = None
        self.task_created_date = None
        self.task_status_updated_date = None

    def create_task(self, new_task, file_path):
        """Create a new task with user input."""
        # Load existing tasks from the file
        tasks = load_file(file_path)
        task_exist = False
        # Check if the task ID already exists
        for task in tasks:
            if int(task['task_id']) == new_task.task_id:
                task_exist = True
                break
        if task_exist:
            print("Task ID already exists. Please try again.")    
        else:
            self.task_id = task_id_generator(tasks)
            self.task_title = new_task.task_title
            self.task_description = new_task.task_description
            self.task_due_date = new_task.task_due_date
            self.task_status = "Pending"
            self.task_created_date = format_date()
            self.task_status_updated_date = None

        tasks.append(self.to_dict())
        # Save the updated tasks back to the file
        save_file(file_path, tasks)

    def to_dict(self):
        """Convert task object to a dictionary for JSON saving."""
        return {
            "task_id": self.task_id,
            "task_title": self.task_title,
            "task_description": self.task_description,
            "task_status": self.task_status,
            "task_due_date": self.task_due_date,
            "task_created_date": self.task_created_date,
            "task_status_updated_date": self.task_status_updated_date
        }
    
    def __str__(self):
        """String representation of the task."""
        return (f"Task ID: {self.task_id}, Title: {self.task_title}, "
                f"Description: {self.task_description}, Status: {self.task_status}, "
                f"Due Date: {self.task_due_date}, Created Date: {self.task_created_date}, "
                f"Status Updated Date: {self.task_status_updated_date}")
    
    
       
        