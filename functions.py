FILEPATH = "todos.txt"                         # this is used when changing filenames only this can be changed and will
                                               # automatically change other strings

def get_todos(filepath=FILEPATH):              # default parameter     #() to filepath for optimise   # avoid repetetive lines in code
    with open(filepath, 'r') as file_local:            # todos to todos_local for differentiating with the code
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):       # order should be SAME in all
    with open(filepath, 'w') as file:
     file.writelines(todos_arg)

# print("GBU MAME")

if __name__ == "__main__":
   print("hello")
   print(get_todos())
