
#!/usr/bin/env python3
import sys
from task_tracker import add_task
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
    else:
        print("\n User asks for other actions...")
        

if __name__ == "__main__":
    main()