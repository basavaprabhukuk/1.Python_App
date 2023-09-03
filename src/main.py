todos = []
 
to_do_file ="../data/todos.txt"
while True:
    user_input= input("Type add[1], edit[2], show[3] , complete[4], exit[x]:")
    user_input =user_input.strip()

    if user_input=="1":
        file1 = open(to_do_file, 'r')
        todos = file1.readlines() 
        file1.close()
        
        new_item = input("Enter a to-do:") + '\n'
        
        file_w = open(to_do_file, 'w')
        todos.append(new_item)
        file_w.writelines(todos)
        file_w.close()
    elif user_input =="2":
        item = int(input("Enter a place to replace the todo(Int):"))
        item = item-1
        with open(to_do_file, 'a+' ) as fp_edit:
            fp_edit.seek(0,0)
            todos = fp_edit.readlines()
        new_to_do = input("Enter a new to-do:") + '\n'
        todos[item] = new_to_do
        with open(to_do_file, 'w' ) as fp_edit:
            fp_edit.writelines(todos)
    
    elif user_input =="3":
        with open(to_do_file, 'r') as fp_r:
           display=fp_r.readlines()
        
        new_to_do = [item.strip('\n') for item in display]
        
        for index, to_do_item in enumerate(new_to_do):
            print (f'{index+1}-->{to_do_item}')
    
    elif user_input =="4":
        complete = int(input("Enter which item to be completed!:"))
        complete = complete-1
        
        with open(to_do_file, 'r') as fp_c:
            todos =fp_c.readlines()

        to_do_to_remove =  todos[complete].strip('\n')   
        todos.pop(complete)
            
        with open(to_do_file, 'w') as fp_w:
            fp_w.writelines(todos)

        print(f"The to-do item removed was : '{to_do_to_remove}'")

    elif user_input =="x":
        break

print("Bye!!!!!!")
