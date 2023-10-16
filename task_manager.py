#Import library
import datetime
#use while loop for username and question until false and create error message if username does not match
switch = True
while switch:
    user_name = input("Please can you insert a username:")
    user_pass= input("Please can you insert a password:")
    user_file = open("user.txt","r+")
    user_list = user_file.readlines()
    for user in user_list:
        split_user = user.strip().split(", ")
        if split_user[0] == user_name and split_user[1] == user_pass:
            print("Thank you correct credentials")
            switch = False
            break
        else:
            pass
    if split_user[0] != user_name and split_user[1] != user_pass:
        print("Invalid username or password entered, please try again.")
#Create function to register user, create error message if username exists
def reg_user():
    user_file = open("user.txt","a+")
    new_user = input("Please enter new user name :")
    new_pass = input("Please enter new user password :")
    user_file = open("user.txt","r+")
    user_list = user_file.readlines()
    for user in user_list:
        split_user = user.strip().split(", ")
        while split_user[0] == new_user:
            new_user = input("Please can you retry, username already exists: ")
            if split_user[0] != new_user:
                print("Thank you the username has been added.")
                user_file.write(f"\n{new_user}, {new_pass}")
#Create function
#Use read lines and split iteration by comma, print index from text file.
def view_all():
    user_file = open("tasks.txt", "r+")
    user_file = user_file.readlines()
    for split_user in user_file:
        split_user = split_user.split(",")
        print(f"\nAssigned to:	{split_user[0]}, \nTask:	 {split_user[1]}, \nDescription :	 {split_user[2]}, \nDue Date:     {split_user[3]}, \nCurrent Date:    {split_user[4]}, \nCompleted? {split_user[5]},")
#Create function
#Use read lines and split iteration by comma, print index from text file and display only user entry with username
#Create count function to number the lines.
#Print out results with the sub-titles
#Request specific task from user.
#Ask if this has been marked complete
#If complete no will turn to yes
# Edit will change the due date to updated one 
def view_mine():
    count = 0
    user_file = open("tasks.txt", "r+")
    user_file1 = user_file.readlines()
    for split_user in user_file1:
        split_user = split_user.split(",")
        if split_user[0] == user_name:
            count+=1
            print(f"\n{int(count)}.Assigned to:	{split_user[0]}, \nTask:	 {split_user[1]}, \nDescription :	 {split_user[2]}, \nDue Date:     {split_user[3]}, \nCurrent Date:    {split_user[4]}, \nCompleted {split_user[5]},")
    id_task = int(input("Please select a specific task tasks will be numbered accordingly : "))
    linecount = user_file1[id_task - 1]
    ed_task = input("Please advise if you would like to mark complete or edit the task : type 'mc' to mark complete or 'e' to edit the text : ")
    if ed_task == "mc":
        user_file.write(f"\n{linecount.replace('No','Yes')}")
        print("Task has been marked complete")
    if ed_task == "e":
        if split_user[5] == " No":
            new_date_due = input("Please enter a new date for task to be due : ") 
            split_pos = 3
            temp = list(split_user)
            temp[split_pos] = new_date_due
            new_txt = ",".join(temp)
            user_file.write(f"\n{new_txt}")       
        else:
            split_user[5] == " Yes"
            print("task has been completed already !")
            pass
#Created user file variable to open user text and used a+ to append
#Used input to get nessacary information
#Used write function to get the input variables written
#Used f format to have it written in order add in headers
def add_task():
    user_file = open("tasks.txt","a+")
    user_assign = input("Please insert username for task assigned too :")
    new_task_title = input("Please enter the title of the task :")
    new_task_descript = input("Please insert a descriprtion of the task :")
    new_task_due = input("Please insert the due date in format : yyyy-month-day : ")
    new_task_comp = input("Has this task been completed : Yes or no : ")
    new_task_curr = datetime.date.today()
    user_file.write(f"\n{user_assign}, {new_task_title}, {new_task_descript}, {new_task_due}, {new_task_curr}, {new_task_comp} ")    
#Create generate report function
#Use the count variables
#Create 2 txt files to update information too.
def generate_report():
    count = 0
    count_incom = 0
    count_comp = 0
    task_file = open("tasks.txt", "r+")
    task_readlines = task_file.readlines()
    for task in task_readlines:
        split_task = task.split(",")
        t_count = split_task.count(task)
        count += 1
        split_task[5] == " No"
        count_incom += 1
        split_task[5] == "Yes"
        count_comp += 1
    new_file = open("task_overview.txt","w+")
    new_file.write(f"The amount of incomplete tasks left is : {count_incom}")
    new_file.write(f"\nThe amount of completed tasks : {count_comp}")

    new_file = open("user_overview.txt","w+")
    if split_user[0] == user_name:
        new_file.write(f"The amount of incomplete tasks left is : {count_incom}")
        new_file.write(f"\nThe amount of completed tasks : {count_comp}")
#Created display stats variable and created readlines
#Calculated the length of each line in the txt files    
def disp_stat():
    task_file = open("tasks.txt", "r+")
    task_list = task_file.readlines()
    total_task = len(task_list)
    print(f"The total number of tasks is : {total_task}")
    user_file = open("user.txt", "r+")
    user_list = user_file.readlines()
    total_user = len(user_list)
    print(f"The total number of users is : {total_user}")
while True:
    if user_name != "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
#Add the generate report function
    if user_name == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - Generate a report
ds - Display stats
e - Exit
: ''').lower()
#Call the functions below from menu
    if menu == 'r':
        while user_name != "admin":
            user_name = input("Invalid permission not granted, please restart program")
        reg_user()    
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'gr':
        generate_report()
    elif menu == 'ds':
        disp_stat()