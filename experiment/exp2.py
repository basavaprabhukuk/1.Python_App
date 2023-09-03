todos = ["1.todo", "2.report","3.presentation"]


todos=[item.replace('.','-')+".txt" for item in todos]

print(todos)
 
