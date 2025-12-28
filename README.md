# 📝 Task Tracker CLI

A robust, lightweight Command Line Interface (CLI) application built with Python to manage your tasks. This tool serves as a persistent digital planner, using a local JSON-based database to store, retrieve, and track your daily activities.



---

## 🚀 Key Features

- **Full CRUD Support**: Effortlessly Create, Read, Update, and Delete tasks.
- **Dynamic Status Management**: Categorize your workflow into `todo`, `in-progress`, and `done`.
- **Intelligent Filtering**: Quickly view specific task groups by status.
- **Data Persistence**: All information is stored in a structured `tasks.json` file.
- **Professional Error Handling**: Built-in validation for:
    - Non-numeric IDs.
    - Empty task descriptions.
    - Invalid status updates.
    - Missing or corrupted database files.
- **Audit Logging**: Automatically tracks both `createdAt` and `updatedAt` timestamps using ISO-8601 formatting.

---

## 🏗️ Technical Architecture

This project was built with a focus on **Defensive Programming** and **Data Integrity**:

- **ID Immutability**: IDs are unique and fixed. Deleting a task does not shift remaining IDs, preventing "referential integrity" issues.
- **Guard Clauses**: The application validates all user input at the "edge" before performing any file operations.
- **Dry Principle**: Optimized file I/O operations with reusable helper functions for loading and saving data.
- **Zero Dependencies**: Built entirely using the Python Standard Library (`json`, `sys`, `datetime`, `os`).



---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SatyaP999/task-tracker-cli.git
cd task-tracker-cli
```

### 2. (Optional) Create an alias
```bash
alias task-cli='python3 /absolute/path/to/task_tracker.py'
```

## Usage Guide

### 1. Add a new task
```bash
task-cli add "Finish the Python project"
# Output: Task added successfully (ID: 1)
```

### 2. Update a task
```bash
task-cli update 1 "Finish the Python project and write README"
```

### 3. Delete a task
```bash
task-cli delete 1
```

### 4. List all tasks
```bash
task-cli list
```

### 5. Filter task by ststus
```bash
task-cli list todo
task-cli list in-progress
task-cli list done
```


### Project URL : https://roadmap.sh/projects/task-tracker
