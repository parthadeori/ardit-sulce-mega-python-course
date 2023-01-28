# Add a "Date" Feature

from functions import get_todos, write_todos
import time

date_today = time.strftime("%b %d, %Y")
time_today = time.strftime("%H:%M:%S")
print("It is", date_today)
print(time_today)
user_prompt = "Type add, show, edit, complete or exit: "


while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        
        todos = get_todos() # todos/todos.txt is the argument value

        todos.append(todo + '\n')

        write_todos(todos) # filepath is default, so no need to pass filepath

    elif user_action.startswith("show"):
        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos) # filepath is default, so no need to pass filepath
        except ValueError:
            print("Your command is not valid. Try again.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1

            removed_todo = todos[index].strip('\n')
            
            todos.pop(index)

            write_todos(todos) # filepath is default, so no need to pass filepath

            message = f"Todo '{removed_todo}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number. Try again")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print('Bye!')