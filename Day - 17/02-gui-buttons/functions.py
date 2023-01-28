def get_todos(filepath=r"todos\todos.txt"): # filepath is parameter
    """
    Read a text file and return the list of todo items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()    
    return todos_local

def write_todos(todos_arg, filepath=r"todos\todos.txt"):
    """
    Write the todo items in a text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)