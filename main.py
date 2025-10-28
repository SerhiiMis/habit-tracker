import json
from datetime import datetime
import os


DATA_FILE = 'habits.json'
DATE_FORMAT = '%Y-%m-%d'



def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print(f"Warning: Could not read or decode {DATA_FILE}. Starting with empty habits.")
        return {}

def save_data(habits):
    try: 
        with open(DATA_FILE, 'w') as f:
            json.dump(habits, f, indent=4)
    except IOError:
        print(f"Error: Could not save data to {DATA_FILE}.")

def add_habit(habits):
    name = input("Enter the name of the new habit: ").strip()
    if not name:
        print("Habit name cannot be empty.")
        return
    
    if name in habits:
        print(f"Habit '{name}' already exists.")
        return
    
    today = datetime.now().strftime(DATE_FORMAT)
    habits[name] = {
        'created': today, 
        'log_dates': [],
        'last_completed': 'Never'
    }
    print(f"Habit '{name}' created on {today}.")

def log_completion(habits):
    if not habits:
        print("No habits to log. Please add a new habit first.")
        return
    
    print("Available habits:")
    habit_names = list(habits.keys())
    for i, name in enumerate(habit_names):
        print(f" {i + 1}. {name}")

    try:
        choice = input("Enter the number of the habit to log: ").strip()
        index = int(choice) - 1
        habit_name = habit_names[index]
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number")
        return
    
    today = datetime.now().strftime(DATE_FORMAT)
    habit = habits[habit_name]
    log_dates = habit.get('log_date', [])

    if today in log_dates:
        print(f"Habit '{habit_name}' already logged for today ({today}).")
        return
    
    log_dates.append(today)
    habit['log_dates'] = log_dates
    habit['last_completed'] = today
    print(f"Successfully logged completion for '{habit_name}' on {today}.")

def delete_habit(habits):
    if not habits:
        print("No habits to delete.")
        return

    print("\nAvailable Habits to Delete:")
    habit_names = list(habits.keys())
    for i, name in enumerate(habit_names):
        print(f" {i + 1}. {name}")

    try: 
        choice = input("Enter the number of the habit to DELETE: ").strip()
        index = int(choice) - 1
        habit_name = habit_names[index]
    except (ValueError, IndexError):
        print("Invalid selection. Please enter a valid number.")
        return
    
    confirmation = input(f"Are you sure you want to permanently delete '{habit_name}'? (y/n): ").strip().lower()

    if confirmation == 'y':
        del habits[habit_name]
        print(f"Habit '{habit_name}' has been permanently deleted.")
    else:
        print(f"Deletion of '{habit_name} cancelled.")
    
def show_status(habits):
    if not habits:
        print("\n--- Habits Status ---")
        print("You haven't added any habits yet!")
        return
    
    print("\n--- Habits Status ---")
    print(f"{'Habit':<25} | {'Created':<10} | {'Logs':<5} | {'Last Completed':<15}")
    print("-" * 60)

    for name, data in habits.items():
        logs = len(data.get('log_dates', []))
        created = data.get('created', 'N/A')
        last_completed = data.get('last_completed', 'Never')
        print(f"{name:<25} | {created:<10} | {logs:<5} | {last_completed:<15}")
    print("-" * 60)

def main():
    print("---Welcome to the Habit Tracker---")
    habits = load_data()

    while True:
        print("\nChoose an action:")
        print("1. Add a new habit")
        print("2. Log completion for a habit")
        print("3. View habits")
        print("4. Delete a habit")
        print("5. Exit and Save")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            log_completion(habits)
        elif choice == '3':
            show_status(habits)
        elif choice == '4':
            delete_habit(habits)
        elif choice == '5':
            save_data(habits)
            print("Habits saved. Goodbye!")
            break
        else:
            print("Invslid choice. Please enter 1, 2, 3, 4, or 5.")

        save_data(habits)

if __name__ == "__main__":
    main()


        
        
        


