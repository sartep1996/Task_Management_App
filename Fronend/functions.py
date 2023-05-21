from backend import *
from config import *
from Fronend.layouts import *

def delete_task(values):
    selected_rows = values['-TABLE-']
    if selected_rows:
        selected_row = selected_rows[0]
        if isinstance(selected_row, dict):
            task_id = selected_row[0]
            selected_task = session.query(Task).get(task_id)
            if selected_task:
                session.delete(selected_task)
                session.commit()
                sg.popup('Task is deleted successfully')
            else:
                sg.popup('Task is not found')
    else:
        sg.popup('No task selected')




def add_task(task_values):
    
    task_name = task_values['task_name']
    start_date = task_values['start_date']
    date_to_finish = task_values['date_to_finish']
    status = task_values['status']

    new_task = Task(task_name=task_name, start_date=start_date, date_to_finish=date_to_finish, status=status)

    session.add(new_task)
    session.commit
    
