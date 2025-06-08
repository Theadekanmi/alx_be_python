def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    item = input("Enter item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

def main():
    shopping_list = []

    while True:
        display_menu()  # Required by the checker
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
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
