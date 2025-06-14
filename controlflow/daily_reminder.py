def get_task_details():
    """Prompt user for task details and return them."""
    task = input("Enter your task: ").strip()
    
    while True:
        priority = input("Priority (high/medium/low): ").lower().strip()
        if priority in ('high', 'medium', 'low'):
            break
        print("Invalid priority. Please enter high, medium, or low.")
    
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
        if time_bound in ('yes', 'no'):
            break
        print("Please answer yes or no.")
    
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    """Generate and print a customized reminder message."""
    match priority:
        case 'high':
            urgency = "high priority"
        case 'medium':
            urgency = "medium priority"
        case 'low':
            urgency = "low priority"
    
    if time_bound == 'yes':
        message = f"Reminder: '{task}' is a {urgency} task that requires immediate attention today!"
    else:
        message = f"Note: '{task}' is a {urgency} task. Consider completing it when you have free time."
    
    print(f"\n{message}")

def main():
    """Main function to run the daily reminder program."""
    print("Daily Task Reminder\n" + "="*20)
    task, priority, time_bound = get_task_details()
    generate_reminder(task, priority, time_bound)
    
    # Celebration message
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()