# Editing and Completing Todo Items

user_prompt = "Type add, show, edit, complete or exit: "

# todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open(r'Day - 8\02-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos] ### list-comprehension expression

            for index, item in enumerate(new_todos):
                row = f"{index + 1}. {item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1

            removed_todo = todos[index].strip('\n')
            
            todos.pop(index)

            with open(r'Day - 8\02-with-context-manager\todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo '{removed_todo}' was removed from the list."
            print(message)

        case 'exit':
            break

print('Bye!')