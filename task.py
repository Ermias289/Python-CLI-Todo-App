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
    
    def update_task(self, task_id, tasks, file_path):
        """Update an existing task with new data."""
        print(
            '''
                  What Would You Like to Update?
                    1. Task Title
                    2. Task Description
                    3. Task Status
                    4. Task Due Date
                    5. All
                    6. Exit
        '''
        )
        tasks = load_file(file_path)
        choice = input("Enter your choice (1-6): ")
        for task in tasks:
            if task['task_id'] == task_id:
                task.update(tasks)
                task['task_status_updated_date'] = format_date()
                save_file(file_path, tasks)
                print(f"Task with ID {task_id} updated successfully.")
                return
        print(f"Task with ID {task_id} not found.") 
        match choice:
            case '1':
                tasks['task_title'] = input("Enter new task title: ")
            case '2':
                tasks['task_description'] = input("Enter new task description: ")
            case '3':
                update_task_status(task_id)
            case '4':
                tasks['task_due_date'] = input("Enter new task due date (YYYY-MM-DD): ")
            case '5':
                tasks['task_title'] = input("Enter new task title: ")
                tasks['task_description'] = input("Enter new task description: ")
                tasks['task_status'] = input("Enter new task status: ")
                tasks['task_due_date'] = input("Enter new task due date (YYYY-MM-DD): ")
            case '6':
                print("Exiting update process.")
                return
            case _:
                print("Invalid choice. Please try again.")
                return
    
    
       
        