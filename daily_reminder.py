# Prompt for user inputs
task = input("Enter your task description: ")
priority = input("Enter the task priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Process the task using match-case
match priority:
    case "high":
        reminder = f"Reminder: HIGH priority task - '{task}'."
    case "medium":
        reminder = f"Reminder: MEDIUM priority task - '{task}'."
    case "low":
        reminder = f"Reminder: LOW priority task - '{task}'."
    case _:
        reminder = f"Reminder: Task '{task}' with UNKNOWN priority."

# Add time-bound warning if applicable
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Display the customized reminder
print(reminder)
