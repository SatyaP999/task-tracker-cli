
#!/usr/bin/env python3
import sys
from task_tracker import *
def main():
    # print(sys.argv)
    # print(f"\n {type(sys.argv)}")
    if len(sys.argv) < 2:
        welcome_msg = """
        Welcome to Task Tracker.
        Use:
            1. task-cli add 'Buy Groceries'
            2. task-cli update 1 "Buy groceries and cook dinner"...
        """
        print(welcome_msg)
        print("Usage: task-cli [command] [arguments]")
        return
    
    if "add" in sys.argv:
        try:
            if len(sys.argv) < 3:
                print("Error: Please provide a task description.")
            else:
                task_desc = sys.argv[-1]
                print(f"\n User asks for adding a task {task_desc}..")
                add_task(task_description=task_desc)
        except Exception as e:
            print(f"Error while calling the add_task method: {e}")
    elif "update" in sys.argv:
        try:
            if len(sys.argv) < 4:
                print("Error: Please provide task id and/or task description.")
            else:
                task_desc = sys.argv[-1]
                task_id = sys.argv[-2]
                print(f"\n User asks for updating a task {task_desc}..")
                update_task(task_id=task_id, task_description=task_desc)
        except Exception as e:
            print(f"Error while calling the update_task method: {e}")
    elif "delete" in sys.argv:
        try:
            if len(sys.argv) < 3:
                print("Error: Please provide task id and/or task id.")
            else:
                task_id = sys.argv[-1]
                print(f"\n User asks for deleting task {task_id}..")
                delete_task(task_id=task_id)
        except Exception as e:
            print(f"Error while calling the delete_task method: {e}")
    elif len(sys.argv) == 3 and "mark" in sys.argv[1]:
        try:
            status = sys.argv[1]
            task_id = sys.argv[-1]
            print(f"\n User asks for updating the progress of task {task_id}..")
            update_progress(task_id=task_id, raw_status=status)
        except Exception as e:
            print(f"Error while calling the update_progress  method: {e}")
    elif len(sys.argv) == 2 and sys.argv[-1] == "list":
        try:
            print(f"\n User asks for displaying all the tasks..")
            get_tasks()
        except Exception as e:
            print(f"Error while calling the method get_tasks: {e}")
            
    else:
        print("\n User asks for other actions...")
        

if __name__ == "__main__":
    main()