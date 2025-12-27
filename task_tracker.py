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
    


def add_task(task_description):
    """
    - checks if a json file exists
        - if, yes then create a task and adds to json fie
        - else, creates a file and adds the task to that file.
    """
    global task_id
    try:
        _init_storage()
        t = Task(task_id, task_description)
        print(t)
        t = t.to_dict()
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            json.dump(t, f, ensure_ascii=False, indent=2)
        print(f"Task added successfully (ID: {t.id})")
        task_id += 1
    except Exception as e:
        print(f"Error occured adding a task: {e}")
    