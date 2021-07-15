todo = []
todo_backup = []


def add_todo(task):
    todo.append(task)


def list_todo():
    return todo


def undo():
    last_task = todo[-1]
    todo_backup.append(last_task)
    todo.pop()


def redo():
    todo.append(todo_backup.pop())


add_todo("Aprender programação")
add_todo("Limpar a casa")
add_todo("Organizar quarto")
print(list_todo())
undo()
print(list_todo())
undo()
print(list_todo())
redo()
print(list_todo())
