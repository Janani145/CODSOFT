class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks found.")

    def update_task(self, task_number, updated_task):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1] = updated_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nWELCOME TO TO-DO LIST MAINTANANCE")
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            updated_task = input("Enter updated task: ")
            todo_list.update_task(task_number, updated_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Thank you for using the To-Do List.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()


#OUTPUT
'''
WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 1
Enter task: Publish a Book
Task added successfully!

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 1
Enter task: Deliver an item
Task added successfully!

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 2
To-Do List:
1. Publish a Book
2. Deliver an item

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 3
Enter task number to update: 2
Enter updated task: Off the stove
Task updated successfully!

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 2
To-Do List:
1. Publish a Book
2. Off the stove

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 4
Enter task number to delete: 2
Task deleted successfully!

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 2
To-Do List:
1. Publish a Book

WELCOME TO TO-DO LIST MAINTANANCE

To-Do List Menu:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Enter your choice: 5
Thank you for using the To-Do List.

'''