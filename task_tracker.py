import json
import os
import sys
from datetime import datetime

file_name = "todo.json" #storing JSON file in the variable





def add_task(tasks, description): #function for adding new task
    new_task = {
        "id" : len(tasks) + 1,
        "description" : description,
        "status" : "todo",
        "createdAt" : datetime.now().isoformat(),
        "updatedAt" : datetime.now().isoformat(),

    }


    tasks.append(new_task)
    print("Task added successfully!")

def update_task(tasks, task_id, new_description): # function for updating existing task
    task_id =  int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            print("Task updated successfully!")

def delete_task(tasks, task_id): #function for deleting task
    for task in tasks:
        if task["id"] == task_id:
            del tasks[task["id"] - 1]
            print(f"Task {task_id} deleted successfully!")

def mark_in_progress(tasks, task_id): #function for marking task in progress
    task_id =  int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            print("Successfully marked in-progress!")

def mark_done(tasks, task_id): # function for marking task done
    task_id =  int(task_id)
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            print("Successfully marked done!")

def list_tasks(tasks): #function for listing all the existing task
    if tasks == []:
        print("There is no available task")
    else:
        print("These are all available task:")

        for index, task in enumerate(tasks, 1):
            print("\n" + str(task["id"]) + "." + task["description"]+"("+task["status"]+")")

def list_done(tasks): #functionfor listing all the completed task
    print("These are all the completed task:")
    for index, task in enumerate(tasks, 1):
        if task["status"] == "done":
            print("\n" + str(task["id"]) + "." + task["description"])

def list_todo(tasks): # function for listing all the todo task
    print("These are all the todo task:")
    for index, task in enumerate(tasks, 1):
        if task["status"] == "todo":
            print("\n" + str(task["id"]) + "." + task["description"])

def list_in_progress(tasks): #function for listing all the task in progress
    print("These are all the task that are in progress:")
    for index, task in enumerate(tasks, 1):
        if task["status"] == "in-progress":
            print("\n" + str(task["id"]) + "." + task["description"])



def print_usage(): # function for printing Prints the usage instructions for the CLI

    print("Program name: Task tracker\n"
          "Use the following commands to interact with the program:\n"
          "  add    : to add task\n"
          "  update : to update task\n"
          "  delete : to delete task\n"
          "  list   : list all tasks\n"
          "  list-done   : list all tasks that are done\n"
          "  list-todo   : list all tasks that are todo\n"
          "  list-in-progress : list all tasks that are in progress\n"
          "  mark-in-progress : to mark a task in-progress\n"
          "  mark-done : to mark a task done")

def load_tasks(): #funtion to Load tasks from the JSON file

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                tasks = json.load(f)
                return tasks
        except json.JSONDecodeError:
            print("Error: todo.json was corrupted.  Resetting to empty list.")
            return []
    else:
        return []

def save_tasks(tasks): #function Saves tasks to the JSON file

    try:
        with open(file_name, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():

        tasks = load_tasks()

        if len(sys.argv) < 2: #checks if there are less tha 2 arguments in the CLI
            print_usage()
            return
        command = sys.argv[1]

    #checks what choice the user picked using if-elif-else statement
        if command == 'add':
            description = " ".join(sys.argv[2:])
            add_task(tasks, description)

        elif command == 'delete':
            task_id = int(sys.argv[2])
            delete_task(tasks, task_id)

        elif command == 'update':
            task_id = sys.argv[2]
            new_description = " ".join(sys.argv[3:])
            update_task(tasks, task_id, new_description)

        elif command == 'mark-in-progress':
            task_id = sys.argv[2]
            mark_in_progress(tasks, task_id)

        elif command == 'mark-done':
            task_id = sys.argv[2]
            mark_done(tasks, task_id)

        elif command == 'list':
            list_tasks(tasks)

        elif command == 'list-done':
            list_done(tasks)

        elif command == 'list-todo':
            list_todo(tasks)

        elif command == 'list-in-progress':
            list_in_progress(tasks)


        else:
            print("Invalid Argument\n"
                  "Use the following commands to interact with the program:\n"
                  "  add    : to add task\n"
                  "  update : to update task\n"
                  "  delete : to delete task\n"
                  "  list   : list all tasks\n"
                  "  list-done   : list all tasks that are done\n"
                  "  list-todo   : list all tasks that are todo\n"
                  "  list-in-progress : list all tasks that are in progress\n"
                  "  mark-in-progress : to mark a task in-progress\n"
                  "  mark-done : to mark a task done")


        save_tasks(tasks)



#call the main function
if __name__ == "__main__":
    main()