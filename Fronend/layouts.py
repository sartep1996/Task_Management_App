from backend import *
from config import *


headers = ['ID', 'Task Name', 'Start Date', 'Finish Date', 'Status']

tasks = session.query(Task).all()

data = [[task.id, task.task_name, task.start_date, task.date_to_finish, task.status] for task in tasks]

table = sg.Table(values=data,headings=headers, num_rows=10, key='-TABLE-' )

main_layout =[
[table],
[sg.Button('Exit')],
[sg.Button('Delete Task')],
[sg.Button('Add Task')]

]
def add_task_window():
    add_task_layout = [
        [sg.Text('Enter your task details')],
        [sg.Text("Enter the name of your task: "), sg.Input(key='task_name')],
        [sg.Text('Enter the beggining date of your task: '), sg.Input(key="start_date")],
        [sg.Text('Enter the finish date of your task:'), sg.Input(key='date_to_finish')],
        [sg.Text('Enter the status of your task', sg.Input(key='status'))],
        [sg.Button('OK', key='OK'), sg.Button('Cancel', key='Cancel')]
    ]
    window = sg.Window('Add Task', add_task_layout())
    
    while True:
        event, values = window.read()
        if event == 'OK':
            task_name = values['task_name']
            start_date = values['start_date']
            date_to_finish = values['date_to_finish']
            status = values['status']

            new_task = Task(task_name=task_name, start_date=start_date, date_to_finish=date_to_finish, status=status)  
            session.add(new_task)
            session.commit
            break

    window.close()