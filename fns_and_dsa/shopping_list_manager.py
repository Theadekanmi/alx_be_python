def display_menu():
    """Display the main menu options."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Add item to the shopping list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Invalid input. Item cannot be empty.")
        
        elif choice == '2':
            # Remove item from the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
                continue
                
            print("Current shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
            try:
                item_num = int(input("Enter the number of the item to remove: "))
                if 1 <= item_num <= len(shopping_list):
                    removed_item = shopping_list.pop(item_num - 1)
                    print(f"'{removed_item}' has been removed from your shopping list.")
                else:
                    print("Invalid item number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            # View the current shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
        
        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()