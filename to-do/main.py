import json
from tasks import TaskHandler
import re
def main():
    task_handler = TaskHandler()

    while True:
        print("\nTodo App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Done")
        print("6. View Filtered Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_handler.add_task()
        elif choice == "2":
            task_handler.view_tasks()
        elif choice == "3":
            index = int(input("Enter task index to update: "))
            try:
                task_handler.update_task(index)
            except ValueError:
                print("Invalid index")
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            try:
                task_handler.delete_task(index)
            except ValueError:
                print("Invalid index")
        elif choice == "5":
            index = int(input("Enter task index to mark as done: "))
            try:
                task_handler.mark_task_done(index)
            except ValueError:
                print("Invalid index")
        elif choice == "6":
            priority = input("Enter priority (High/Medium/Low): ").lower()
            valid_priorities = ["high", "medium", "low"]
            while priority not in valid_priorities:
                   print("Invalid priority. Please enter High, Medium, or Low.")
                   priority = input("Enter priority (High/Medium/Low): ").lower()
                   
            due_date_regex = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
            due_date = input("Enter due date (YYYY-MM-DD): ").lower()
            while not re.match(due_date_regex, due_date):
                 print("Invalid due date format. Please enter in YYYY-MM-DD format.")
                 due_date = input("Enter due date (YYYY-MM-DD): ").lower()
            print(due_date)
            task_handler.view_tasks(priority=priority, due_date=due_date)
        elif choice == "7":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()