noOfTdo = int(input("How many items you want to add? "))
user_prompt = 'Enter a todo:'


todos = []
x=0
while x <= noOfTdo:
    todo = input(user_prompt)
    todos.append(todo)
    x = x+1

print(todos)
print(type(todos))