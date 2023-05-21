from backend import Task
from config import session, sg
from Fronend.layouts import main_layout
from Fronend.functions import *

window = sg.Window('Tasks', main_layout)


while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break
    elif event == 'Delete Task':
        delete_task(values)
        session.commit()


session.close()
window.close()