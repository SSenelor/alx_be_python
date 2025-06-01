task = str(input("Input a task description: "))
priority = str(input("What is the priority (high, medium, low): ")).lower()
time_bound = str(input("Task is time-bound (yes or no): ")).lower()

#Use a Match Case statement to react differently based on the task’s priority.
#Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
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
   # message1 = " that requires immediate attention today!"
    print(f"that requires immediate attention today!")
else:
  # message2 = ". Consider completing it when you have free time."
    print(f". Consider completing it when you have free time.")
