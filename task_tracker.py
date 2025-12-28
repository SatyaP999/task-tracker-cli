import json
from pathlib import Path
from datetime import datetime
from task import Task

TASKS_FILE = Path("tasks.json")
task_id = 1

def _init_storage():
    """
    Ensures the tasks.json file exists and is initialized with an empty list.
    """
    # 1. Check if the file already exists
    # 2. If it doesn't exist:
        # a. Open the file in write mode ('w')
        # b. Use json.dump to write [] into it
        # c. (Optional) Print a message like "Storage initialized"
        
    if TASKS_FILE.exists():
        print("JSON file already exists..")
    else:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        print("Storage initialized")
    
def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks_list = json.load(file)
        if isinstance(tasks_list, list):
            print("Successfully read the JSON file into a Python list:")
            # print(tasks_list)
            # print(f"Type of the result: {type(tasks_list)}")
            return tasks_list
        else:
            print(f"Error: The JSON file did not contain a list (it was a {type(tasks_list).__name__}).")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except IOError as e:
        print(f"Error reading file: {e}")


def add_task(task_description):
    try:
        _init_storage()
        new_id = 1
        tasks_lst = load_tasks()
        if len(tasks_lst) == 0:
            t = Task(new_id, task_description)
            t = t.to_dict()
            tasks_lst.append(t)
            with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump(tasks_lst, f, indent=2)
        else:
            last_task_id = tasks_lst[-1]["id"]
            new_id = last_task_id+1
            t = Task(new_id, task_description)
            t = t.to_dict()
            tasks_lst.append(t)
            with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump(tasks_lst, f, indent=2)
        
        print(f"Task added successfully: (ID: {new_id})")
    except Exception as e:
        print(f"Error adding task - {task_description: {e}}")
        
def update_task(task_id, task_description):
    try:
        _init_storage()
        tasks_lst = load_tasks()
        num_of_tasks = len(tasks_lst)
        task_found = False
        if num_of_tasks == 0:
            print("There are no tasks to be updated. Please add a task")
            return
        
        if not(task_id.isnumeric()):
            print("Please enter a valid task id to update. Task id should be numeric")
            return
        
        if len(task_description) == 0:
            print("Task description should not be empty. Please enter a valid task description to update.")
            return
        
        for i in range(num_of_tasks):
            if task_id == str(tasks_lst[i]["id"]):
                tasks_lst[i]["description"] = task_description
                tasks_lst[i]["updatedAt"] = datetime.now().isoformat()
                task_found = True
                break
        if not(task_found):
            print(f"Task with ID: {task_id} is not found. Please enter a valida task id for updation.")
        else:
            with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump(tasks_lst, f, indent=2)
        
            print(f"\n Task (ID: {task_id}) updated to {task_description}")
    except Exception as e:
        print(f"Error updating task (ID: {task_id}): {e}")
            

def delete_task(task_id):
    try:
        _init_storage()
        tasks_lst = load_tasks()
        num_of_tasks = len(tasks_lst)
        task_found = False
        if num_of_tasks == 0:
            print("There are no tasks to delete.")
            return
        
        if not(task_id.isnumeric()):
            print("Please enter a valid task id to delete. Task id should be numeric")
            return
            
        for task in tasks_lst:
            if task_id == str(task["id"]):
                tasks_lst.remove(task)
                task_found = True
                break
        
        if not(task_found):
            print(f"Task with ID: {task_id} is not found. Please enter a valida task id for deletion.")
        else:
            with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump(tasks_lst, f, indent=2)
            print(f"\n Task (ID: {task_id}) deleted.")
    except Exception as e:
        print(f"Error deleting task (ID: {task_id}): {e}")
    
    
def update_progress(task_id, raw_status):
    try:
        _init_storage()
        tasks_lst = load_tasks()
        num_of_tasks = len(tasks_lst)
        task_found = False
        if num_of_tasks == 0:
            print("There are no tasks to update the progress.")
            return
        
        if not(task_id.isnumeric()):
            print("Please enter a valid task id to update the progress. Task id should be numeric")
            return
            
        if len(raw_status) == 0:
            print("Status should not be empty. Please enter a valid status.")
            return
        
        status_lst = raw_status.split("-")
        status = ""
        if len(status_lst) == 3:
            status += status_lst[-2] + "-" + status_lst[-1]
        elif len(status_lst) == 2:
            status += status_lst[-1]
        
        for task in tasks_lst:
            if task_id == str(task["id"]):
                task["status"] = status
                task["updatedAt"] = datetime.now().isoformat()
                task_found = True
                break
        
        if not(task_found):
            print(f"Task with ID: {task_id} is not found. Please enter a valida task id for updation of progress.")
        else:
            with open(TASKS_FILE, 'w', encoding='utf-8') as f:
                json.dump(tasks_lst, f, indent=2)
            print(f"\n Task (ID: {task_id}) progress has been updated.")
    except Exception as e:
        print(f"Error updating the progress of task (ID: {task_id}): {e}")


def get_tasks():
    try:
        _init_storage()
        tasks_lst = load_tasks()
        num_of_tasks = len(tasks_lst)
        
        if num_of_tasks == 0:
            print("There are no tasks to be displayed.")
            return
        print("\n", "="*80)
        for task in tasks_lst:
            print(f"[{task['id']}] {task['description']}")
            print(f"Status: {task['status'].upper()} | Created: {task['createdAt'][:10]}")
            print("-" * 40)
        print("\n", "="*80)
    except Exception as e:
        print(f"Error listing out all the tasks: {e}")
            
def get_tasks_by_ststus(status):
    try:
        _init_storage()
        tasks_lst = load_tasks()
        num_of_tasks = len(tasks_lst)

        if num_of_tasks == 0:
            print("There are no tasks to be displayed.")
            return
        
        if status not in ["todo", "in-progress", "done"]:
            print("Please enter a valid status. Status must be one of these (todo, in-progress, done).")
            return
        
        cnt = 0
        print("\n", "="*80)
        for task in tasks_lst:
            if task["status"].lower() == status.lower(): 
                print(f"[{task['id']}] {task['description']}")
                print(f"Status: {task['status'].upper()} | Created: {task['createdAt'][:10]}")
                print("-" * 40)
                cnt += 1
        
        if cnt == 0:
            print(f"There are no tasks with the status: {status}")
        print("\n", "="*80)
    except Exception as e:
        print(f"Error listing out all the tasks by status: {e}")
        