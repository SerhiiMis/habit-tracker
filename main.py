def main():
    print("--- Welcome to the Habit Tracker App ---")

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


