from backend import *
from config import *
from Fronend.layouts import *

def delete_task(values):
    selected_rows = values['-TABLE-']
    if selected_rows:
        selected_row = selected_rows[0]
        if isinstance(selected_row, dict):
            task_id = selected_row['ID']
            selected_task = session.query(Task).get(task_id)
            if selected_task:
                print(f"Deleting task with ID: {task_id}")
                session.delete(selected_task)
                session.commit()
                sg.popup('Task is deleted successfully')
            else:
                sg.popup('Task is not found')
        else:
            sg.popup('Invalid task format')
    else:
        sg.popup('No task selected')