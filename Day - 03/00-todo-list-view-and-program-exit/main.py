# match-case

user_prompt = "Type add, show or exit: "

todos = []

while True:
    user_action = input(user_prompt)

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print('Bye!')