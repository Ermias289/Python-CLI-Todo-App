from task import Task
import time
def main():
    """Main Menu Of To do List App"""
    new_task = Task()
    file_path = "tasks.json"
    while True:
        menu = new_task.app_menu()
        match menu :
            case 1:
                new_task.task_title = input("Enter the title of your new task: ")
                new_task.task_description = input("Enter the description of the task: ")
                new_task.task_due_date = input("Enter the due date of your task: ")
                new_task.create_task(new_task, file_path)
                print('''
                        *********************************
                        *                               * 
                        * ✔ Task Created Successfully   *    
                        *                               *
                        *                               *
                        *********************************
                    ''')
                time.sleep(2)
            case 2:
                new_task.view_all(file_path)
                time.sleep(2)
            case 3:
                new_task.mark_complete(file_path)
                time.sleep(2)
# 1. Add a new task
#                 2. View all tasks
#                 3. Mark a task as complete
#                 4. Delete a task
#                 5. View tasks due today
#                 6. Update Task Data
#                 7. Exit

if __name__ == "__main__":
    main()
