todos = []

while True:
    user_action = (input("type add, show, edit or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':     # Bitwise operator
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            edit_item_no = int(input("Please enter the item number that you want to edit"))
            new_todo = input("Please enter your new value: ")
            todos[edit_item_no] = new_todo
        case 'exit':
            break
        case _:
            print("Invalid Input. Please type valid choice: ")

print('Done')
