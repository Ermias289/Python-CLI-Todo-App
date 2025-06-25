from utils import load_file


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

    #  def create_task(self, new_task, file_path):
    #     """Create a new task with user input."""
    #     try:
    #         # Load existing tasks from the file
    #         tasks = load_json(file_path)
    #     except FileNotFoundError:
    #         print(f"File {file_path} not found. Creating a new task File.")
    #         tasks = []
    #     task_exist = False
    #     # Check if the task ID already exists
    #     for task in tasks:
    #         if int(task['task_id']) == new_task.task_id:
    #             task_exist = True
    #             break
        
    #     if task_exist:
    #         print("Task ID already exists. Please try again.")    
    #     else:
    #         # Generate a new task ID
    #         self.task_id = 1
    #         self.task_title = new_task.task_title 
    #         self.task_description = new_task.task_description
    #         self.task_status = "Pending"
    #         self.task_due_date = new_task.task_due_date
    #         self.task_created_date = None
    #         print("Task created successfully!")

    #     tasks.append(new_task.to_dict())
       
    