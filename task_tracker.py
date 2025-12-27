import json
from pathlib import Path
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
            print(tasks_list)
            print(f"Type of the result: {type(tasks_list)}")
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
            
    
    