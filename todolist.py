print("My Todo-List")
while True:
    choice = input("you wanna add, show, edit,exit or mark complete  a todo")
    choice=choice.strip()

    if choice.startswith("add"):


        todo = choice[4:] + '\n'
        file=open('todos.txt','r')
        todos=file.readlines()
        todos.append(todo)
        file.close()

        file=open('todos.txt','w')
        file.writelines(todos)
        file.close()

    elif choice.startswith("show"):

        #file=open('todos.txt','r')
        #todos=file.readlines()
        #file.close()
        with open('todos.txt','r') as file:
            todos=file.readlines()

        for index, item in enumerate(todos,start=1):
            item=item.title()
            item=item.strip()
            print(f"{index}-{item}")
            #print(f"{index + 1}-{item}") #if the start=1 is not declared in the enumerate function"""
    elif choice.startswith("edit"):

        num=int(choice[5:])

        num= num-1

        with open('todos.txt','r') as file:
            todos=file.readlines()
        print('the number is:',todos[num])

        new_todo=input("enter the new todo:")
        todos[num]=new_todo+'\n'
        print("new todo is ",new_todo)
        with open('todos.txt','w') as file:
            file.writelines(todos)


    elif choice.startswith("complete"):
        num =(int(choice[9:]))
        num=num-1
        with open('todos.txt','r') as file:
            todos=file.readlines()
        x=todos.pop(num)
        with open('todos.txt','w') as file:
            x=file.writelines(todos)

    elif choice.startswith("exit"):

        break
    else:
        print("wrong input")
print("done")