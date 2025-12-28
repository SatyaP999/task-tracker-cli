import json
import subprocess
import os

PYTHON_CMD = "python3"
ENTRY_FILE = "main.py"
DATA_FILE = "tasks.json"

def run_command(args):
    result = subprocess.run(
        [PYTHON_CMD, ENTRY_FILE] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def clear_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
        
def run_tests():
    print("Starting integration testing for main.py...\n")
    clear_data()
    
    # --- TEST 1: Add a task ---
    print("Testing ADD..\n")
    response = run_command(["add", "Buy Milk"])
    # print(f"𝌮 {response}\n")
    assert "Task added successfully" in response
    print("✅ Pass: Task added.")
    
    # --- TEST 2: Update validation (Non-numeric ID) ---
    print("Testing 'update' with invalid ID...")
    response = run_command(["update", "abc", "New Name"])
    assert "numeric" in response.lower()
    print("✅ Pass: Caught non-numeric ID.")
    
    # --- TEST 3: Update validation (Empty description) ---
    print("Testing 'update' with empty description...")
    # Passing an empty string as an argument
    response = run_command(["update", "1", ""])
    assert "valid task description" in response.lower()
    print("✅ Pass: Caught empty description.")

    # --- TEST 4: Delete logic ---
    print("Testing 'delete'...")
    response = run_command(["delete", "1"])
    assert "deleted" in response.lower()
    print("✅ Pass: Task deleted.")

    # --- TEST 5: List empty state ---
    print("Testing 'list' when empty...")
    response = run_command(["list"])
    assert "no tasks" in response.lower()
    print("✅ Pass: Correct empty list message.")

    print("\n🎉 All Integration Tests Passed!")

if __name__ == "__main__":
    run_tests()