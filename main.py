import json
from datetime import datetime
import os

DATA_FILE = 'habits.json'
DATE_FORMAT = "%Y-%m-%d"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print(f"Warning: Could not read or decode {DATA_FILE}. Starting with an empty data (habit list).")

def save_data(habits):
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(habits, f, indent=4)
    except IOError:
        print(f"Error: Could not save data to {DATA_FILE}.")




def main():
    print("--- Welcome to the Habit Tracker App ---")
    habits = load_data()

    while True:
        print("\nChoose an action:")
        print("1. Add a new habit")
        print("2. Log completion for a habit")
        print("3. View habit status")
        print("4. Exit and Save")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            log_completion(habits)
        elif choice == '3':
            show_status(habits)
        elif choice == '4':
            save_data(habits)
            print("Habits saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

        save_data(habits)


if __name__ == "__main__":
    main()

