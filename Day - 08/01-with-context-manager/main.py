# Optimising the Code

user_prompt = "Type add, show, edit, complete or exit: "

# todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open(r'Day - 8\01-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open(r'Day - 8\01-with-context-manager\todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open(r'Day - 8\01-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos] ### list-comprehension expression

            for index, item in enumerate(new_todos):
                row = f"{index + 1}. {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break

print('Bye!')