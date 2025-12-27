if __name__ == "__main__":
    import sys
    # print(sys.argv)
    # print(f"\n {type(sys.argv)}")
    if len(sys.argv) < 3:
        welcome_msg = """
        Welcome to Task Tracker.
        Use:
            1. task-cli add 'Buy Groceries'
            2. task-cli update 1 "Buy groceries and cook dinner"...
        """
        print(welcome_msg)
    else:
        if "add" in sys.argv:
            print("\n User asks for adding a task..")
        else:
            print("\n User asks for other actions...")