from backend import *
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


session.close()
window.close()

