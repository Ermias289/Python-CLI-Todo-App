def main(): 
    """Main function to run the CLI Todo app."""

    while True:
        app_menu = '''
            Hello Welcome to the CLI Todo App!

                Please choose an option:    

                1. Add a new task
                2. List all task
                3. Complete Task with ID
                4. Delete task with ID
                5. Tasks due today
                6. Exit
        '''
        print(app_menu)
        choice = input("Enter your choice: ")
    
        match choice:
            case '1':
                # new_task = Task()
                # new_task.task_title = input("Enter task title: ")
                # new_task.task_description = input("Enter task description: ")
                # new_task.task_due_date = input("Enter task due date (YYYY-MM-DD): ")
                # new_task.create_task(new_task, 'tasks.json')
                break


if __name__ == "__main__":
    main()