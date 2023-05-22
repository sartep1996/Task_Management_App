from backend import *
from config import *


headers = ['ID', 'Task Name', 'Start Date', 'Finish Date', 'Status']

tasks = session.query(Task).all()

data = [[task.id, task.task_name, task.start_date, task.date_to_finish, task.status] for task in tasks]

table = sg.Table(values=data,headings=headers, num_rows=10, key='-TABLE-' )

main_layout =[
[table],
[sg.Button('Exit')], [sg.Button('Delete Task')],
[sg.Button('Add Task')], [sg.Button('Edit Task')]

]
def add_task_window():
    add_task_layout = [
        [sg.Text('Enter your task details')],
        [sg.Text("Enter the name of your task: "), sg.Input(key='task_name')],
        [sg.Text('Enter the beggining date of your task: '), sg.Input(key="start_date")],
        [sg.Text('Enter the finish date of your task:'), sg.Input(key='date_to_finish')],
        [sg.Text('Enter the status of your task'), sg.Input(key='status')],
        [sg.Button('OK', key='OK'), sg.Button('Cancel', key='Cancel')]
    ]
    window = sg.Window('Add Task', add_task_layout)
    
    while True:
        event, values = window.read()
        if event == 'OK':
            task_name = values['task_name']
            start_date = values['start_date']
            date_to_finish = values['date_to_finish']
            status = values['status']

            new_task = Task(task_name=task_name, start_date=start_date, date_to_finish=date_to_finish, status=status)  
            session.add(new_task)
            session.commit()
            break

    window.close()
    return add_task_layout

def edit_task_layout(task):
    edit_layout = [[sg.Text('Edit Task')],
                        [sg.Text('New Task Name'), sg.InputText(key= 'task_name', default_text=task.task_name)],
                        [sg.Text('New Task Start Date'), sg.InputText(key= 'start_date', default_text=task.start_date)],
                        [sg.Text('New Task Finish Date'), sg.InputText(key= 'date_to_finish', default_text=task.date_to_finish)],
                        [sg.Text('New Status'), sg.InputText(key= 'status', default_text=task.status)],
                        [sg.Button('Save', key='Save')],
                        [sg.Button('Close', key = 'Close')]
                        ]

    # task = session.query(Task).get(task.id)

    window = sg.Window('Edit Book', edit_layout)

    while True:
        event, values = window.read()
        if event == 'Close' or event == sg.WINDOW_CLOSED:
            break
        elif event == 'Save':
            task.task_name = values['task_name']
            task.start_date = values['start_date']
            task.date_to_finish = values['date_to_finish']
            task.status = values['status']

            session.commit()
            break
    
    session.close()
    window.close()
