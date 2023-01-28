user_prompt = "Enter a todo: " # 1. remove the last double-quote and run it
# 2. exchange double quotes to single quotes
todo1 = input(user_prompt) # 3. remove the last parenthesis and try to run it
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]
print(todos)

print(type(user_prompt))
print(type(todo1))
print(type(todos))