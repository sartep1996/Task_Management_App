from backend import Task
from config import *
from Fronend.layouts import *
from Fronend.functions import *

window = sg.Window('Tasks', main_layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Delete Task':
        delete_task(values)
        session.commit()
    elif event == 'Add Task':
        add_task_window()
        session.commit()
    elif event == 'Edit Task':
        selected_task = values['-TABLE-'][0]
        task = session.query(Task).filter_by(task_name = selected_task).first()
        if task:
            edit_task_layout(task)
            session.commit()
        else:
            sg.popup("Task is not found")
    
session.close()
window.close()

