import PySimpleGUI as sg

"""
    Demo_Close_Attempted_Event

    Detecta se o usuário tentou fechar uma janela (clique em "X") e confirma com um pop-up.
    Requer PySimpleGUI 4.33.0 e posterior

    Copyright 2021 PySimpleGUI Inc.
"""

layout = [[sg.Text('Close confirmation demo')],
          [sg.Text('Try closing window with the "X"')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, enable_close_attempted_event=True, finalize=True)

while True:
    win, event, values = sg.read_all_windows()   #event return none
    print(event, values)
    if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
        if sg.popup_yes_no('Do yuou really want to exit?') == 'Yes':
            break
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()