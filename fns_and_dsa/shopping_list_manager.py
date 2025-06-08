def main():
    shopping_list = []

    while True:
        print("Shopping List Manager")  # <-- Required exact print
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
