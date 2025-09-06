Todolist=[]
def addtask():
    task=input("Enter the task:")
    Todolist.append({'Task': task, 'Status': "Pending"})
    print("New task added successfully\n")
def viewtask():
    print("your to-do list:\n")
    if len(Todolist)==0:
        print("No pending tasks")
    else:
        for i,task in enumerate(Todolist, 1):
            print(f"{i}:{task['Task']} - {task['Status']}")
def removetask():
    if len(Todolist)==0:
        print("List is Empty!")
    else:
        try:
            searchingindex=int(input("Enter the task number that you want to remove: "))-1
            if 0 <=searchingindex < len(Todolist):
                removed_task = Todolist.pop(searchingindex)
                print(f"Task Removed: {removed_task}")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
def markdone():
    if len(Todolist)==0:
        print("List is Empty!")
    else:
        try:
            searchingindex=int(input("Enter the task number that you want to remove: "))-1
            if 0 <=searchingindex < len(Todolist):
                Todolist[searchingindex]['Status'] = "Completed"
                print(f"Task {Todolist[searchingindex]['Task']} has been marked as done.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
def menu():
    while (True):
        print("Welcome to the To-Do List Application!")
        print("1. Add a new task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. mark a task as done")
        print("5. Exit")

        choice = input("Please enter your choice Number: ")
        if choice == '1':
            addtask()
        elif choice == '2':
            viewtask()
        elif choice == '3':
            removetask()
        elif choice == '4':
            markdone()
        elif choice == '5':
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice, please try again.")    
menu()    
