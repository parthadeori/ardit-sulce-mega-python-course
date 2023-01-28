# Improving the 'Add' Feature

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + "\n" # list-slicing

        with open(r'todos\todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open(r'todos\todos.txt', 'w') as file:
            file.writelines(todos)
    if 'show' in user_action:
        with open(r'todos\todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos] ### list-comprehension expression

        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"
            print(row)

    if 'edit' in user_action:
        number = int(input("Number of the todo to edit: "))
        number = number - 1

        with open(r'todos\todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open(r'todos\todos.txt', 'w') as file:
            file.writelines(todos)

    if 'complete' in user_action:
        number = int(input("Number of the todo to complete: "))

        with open(r'todos\todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1

        removed_todo = todos[index].strip('\n')
        
        todos.pop(index)

        with open(r'todos\todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo '{removed_todo}' was removed from the list."
        print(message)

    if 'exit' in user_action:
        break

print('Bye!')