from backend import *
from config import *
from Fronend.layouts import *

# def delete_task(values):
#     selected_rows = values['-TABLE-']
#     if selected_rows:
#         selected_row_index = selected_rows[0]
#         task_id = selected_row_index + 1  # Adjust the indexing by adding 1
#         selected_task = session.query(Task).get(task_id)
#         if selected_task:
#             session.delete(selected_task)
#             session.commit()
#             sg.popup('Task is deleted successfully')
#         else:
#             sg.popup('Task is not found')
#     else:
#         sg.popup('No task selected')


def delete_task(values):
    selected_rows = values['-TABLE-'][0]
    if selected_rows:
        selected_row = selected_rows 
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


# def delete_task(values):
#     selected_rows = values['-TABLE-']
#     if selected_rows:
#         selected_row_index = selected_rows[0]
#         print("Selected Row Index:", selected_row_index)  # Debug statement
#         table_data = values['-TABLE-']
#         if 0 <= selected_row_index < len(table_data):
#             selected_row_data = table_data[selected_row_index]
#             print("Selected Row Data:", selected_row_data)  # Debug statement
#             task_id = selected_row_data['ID'] if selected_row_data else None
#             print("Task ID:", task_id)  # Debug statement
#             selected_task = session.query(Task).get(task_id)
#             print("Selected Task:", selected_task)  # Debug statement
#             if selected_task:
#                 session.delete(selected_task)
#                 session.commit()
#                 sg.popup('Task is deleted successfully')
#             else:
#                 sg.popup('Task is not found')
#         else:
#             sg.popup('Invalid selected row index')
#     else:
#         sg.popup('No task selected')


# def delete_task(values):
#     selected_task_id  = int(values['-TABLE-'][0])
#     selected_task = session.query(Task).get(selected_task_id)
#     if selected_task:
#         session.delete(selected_task)
#         session.commit()




def add_task(task_values):
    
    task_name = task_values['task_name']
    start_date = task_values['start_date']
    date_to_finish = task_values['date_to_finish']
    status = task_values['status']

    new_task = task(task_name=task_name, start_date=start_date, date_to_finish=date_to_finish, status=status)

    session.add(new_task)
    session.commit
    
