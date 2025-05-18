# Task Tracker CLI

A command-line task management tool to help you organize your tasks.

## Features

* Add new tasks.
* Update existing tasks.
* Delete tasks.
* Mark tasks as in progress or done.
* List all tasks.
* List tasks by status (todo, in progress, done).

## Usage

1.  Clone the repository:

    ```
    git clone <repository_url>
    ```
    (Replace `<repository_url>` with your repository URL.)
2.  Navigate to the project directory:

    ```
    cd TaskTrackerCLI
    ```
3.  Run the program:

    ```
    python task_tracker.py <command> [arguments]
    ```

## Commands

* **Add a task:** `python task_tracker.py add "Task description"`
* **Update a task:** `python task_tracker.py update <task_id> "New description"`
* **Delete a task:** `python task_tracker.py delete <task_id>`
* **Mark a task as in progress:** `python task_tracker.py mark-in-progress <task_id>`
* **Mark a task as done:** `python task_tracker.py mark-done <task_id>`
* **List all tasks:** `python task_tracker.py list`
* **List done tasks:** `python task_tracker.py list done`
* **List todo tasks:** `python task_tracker.py list todo`
* **List in-progress tasks:** `python task_tracker.py list in-progress`

## Task Properties

Each task has the following properties:

* `id`: A unique identifier for the task
* `description`: A short description of the task
* `status`: The status of the task (todo, in-progress, done)
* `createdAt`: The date and time when the task was created
* `updatedAt`: The date and time when the task was last updated

## Example


python task_tracker.py add "Buy groceries"
python task_tracker.py list
python task_tracker.py mark-done 1
python task_tracker.py list done

## Project Page URL

[Project Page](https://github.com/Ollamidee/TaskTrackerCLI)

