task = str(input("Input a task description: "))
priority = str(input("What is the priority (high, medium, low): ")).lower()
time_bound = str(input("Task is time-bound (yes or no): ")).lower()

print("Reminder: ", end = "")
match priority :
    case "high":
        print(f"{task} is a high priority task", end = "") 
    case "medium":
        print(f"{task} is a medium priority task",  end = "")
    case "low":
        print(f"{task} is a low priority task",  end = "")
    case _:
        print (f"{task}' has an unknown priority. Please double-check your input.")

if time_bound == "yes":

    print(f"that requires immediate attention today!")
else:

    print(f". Consider completing it when you have free time.")
