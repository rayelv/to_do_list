to_do_list = []
def add_task():
    task = input("Enter your task ✍️:\n").title()
    to_do_list.append(task)
    print("Task has been added.")
    
def remove_task():
    no_task = input("Enter the name of task you would like to remove: \n").title()
    if no_task in to_do_list:
        to_do_list.remove(no_task)
        print("Task has been removed 🗑️.")
    else:
        print("👁️👁️ task not found.")
        
def view_list():
    print("Here are your current tasks: \n")
    for task in to_do_list:
        print(task.title())
        print("\n")
def main():
    to_do_list = []
    
while True:
    print("Let's get you started: \n1)Add task\n2)Remove task\n3)View To Do List\n4)Exit\n")
    choice = input("Make your selection (1-4)\n")
    if choice == '1':
            add_task()
    elif choice == '2':
            remove_task()
    elif choice == '3':
            view_list()
    elif choice == '4':
            print("You have no more tasks to enter. Goodbye✌️✌️")
            break
    else: 
            print("Invalid entry Try again.")
            
main()