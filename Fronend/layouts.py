from backend import *
from config import *


headers = ['ID', 'Task Name', 'Start Date', 'Finish Date', 'Status']

tasks = session.query(Task).all()

data = [[task.id, task.task_name, task.start_date, task.date_to_finish, task.status] for task in tasks]

table = sg.Table(values=data,headings=headers, num_rows=10, key='-TABLE-' )

main_layout =[
[table],
[sg.Button('Exit')],
[sg.Button('Delete Task')]
]

