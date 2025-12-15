tasks=[]
while True:
    print("....TO-DO-LIST....")
    print("1.veiw tasks")
    print("2.add tasks")
    print("3.delete tasks")
    print("4.exit")

    choice=input("enter the choice: " )

    if choice=="1":
        if not tasks:
            print("NO TASK FOUND")
        else:
            for i, task in enumerate(tasks,1):
                print(i,task)    
    elif choice=="2":
        task=input("enter the task: ")
        tasks.append(task) 
        print("TASK ADDED")   
    elif choice=="3":
        if not tasks:
            print("NO TASK FOUND")
        else:
            for i,task in enumerate(tasks,1):
                print(i,task)
            num=int(input("ENTER THE TASK NO TO BE DELETED: "))
            if 1<=num<=len(task):
                removed=tasks.pop(num-1)
                print(f"DELETED: {removed}")
            else:
                print("INVALID NUMBER")        
    elif choice=="4":
        print("exiting...")
        break
    else:
        print("INVALID CHOICE")
