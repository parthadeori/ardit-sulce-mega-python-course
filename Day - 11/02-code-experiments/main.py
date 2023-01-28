# Local and Global Scope

def greet():
    message = "hello"
    new_message = message.capitalize()
    print("Hey hey")
    return new_message


greeting = greet()
# print(greet())
print(greeting)

# print(new_message)
# print(message)