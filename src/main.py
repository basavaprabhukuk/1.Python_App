todos = []

while True:
    user_input= input("Type add[1], edit[2], show[3], exit[x]:")
    user_input =user_input.strip()

    if user_input=="1":
        new_item = input("Enter a to-do:")
        todos.append(new_item)
    elif user_input =="2":
        item = int(input("Enter a place to replace the todo(Int):"))
        item = item-1
        new_to_do = input("Enter a new to-do:")
        todos[item] = new_to_do
    elif user_input =="3":
        print(todos)
    elif user_input =="x":
        break

print("Bye!!!!!!")
