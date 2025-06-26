from task import Task
import time
import sys



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
            case 4: 
                new_task.delete_task_Id(file_path)
            case 5:
                new_task.tasks_due_today(file_path)
            case 6:
                new_task.update_task(file_path)
            case 7:
                print("Exiting....Good Bye 😊")
                sys.exit()
                
if __name__ == "__main__":
    main()
