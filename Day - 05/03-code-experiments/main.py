# # Code experiments

# user_prompt = "Type add, show, edit, complete or exit: "

# todos = []

# while True:
#     user_action = input(user_prompt)
#     user_action = user_action.strip()

#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos.append(todo)
#         case 'show':
#             for index, item in enumerate(todos):
#                 row = f"{index + 1}. {item}"
#                 print(row)
#             # print("Length of the todo is: ", index + 1)
#             # print(len(todos))
#         case 'edit':
#             number = int(input("Number of the todo to edit: "))
#             number = number - 1
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))
#             todos.pop(number - 1)
#         case 'exit':
#             break

# print('Bye!')



for i, j in enumerate("Hello"):
    print(i, j)

a = enumerate(["a", "b", "c"])
print(a)

print(list(a))

for i, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(i, item)

b = enumerate("Hello")
print(list(b))