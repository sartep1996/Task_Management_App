from backend import Task
from config import sg, session
from Fronend.layouts import main_layout



def delete_task(values):
    selected_rows = values['-TABLE-']
    if selected_rows:
        selected_row = selected_rows[0]
        if isinstance (selected_row, dict):
            task_id = selected_row['id']
            selected_task = session.query(Task).get(task_id)
            if selected_task:
                session.remove(selected_task)
                session.commit()
                sg.popup('Task is deleted successfully')
            else:
                sg.popup('Task is not found')
    else:
        sg.popup('No task selected')