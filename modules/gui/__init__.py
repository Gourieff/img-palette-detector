import sys
import PySimpleGUI as sg

def get_file():
    # layout = [[sg.Text('My Window')],
    #        [sg.InputText(size=(50, 1), key='-FILENAME-'), sg.FileBrowse()],
    #        [sg.Button('Go'), sg.Button('Exit')]]
    # event1, values1 = sg.Window('Normal Filename', layout).read(close=True)
    file = sg.popup_get_file('Type the path or the filename here or navigate to the destination', 'Select any image (png, jpg, bmp)', grab_anywhere=True)
    if file is None: file = '' # by default
    return file

def set_method():
    radio_keys = ['1', '2', '3']
    selected_color = ('red', 'white')
    active_radio_button = None
    btn_selected = '1'

    layout = [  [sg.Text('Choose 1, 2 or 3\n1 - OpenCV based method\n2 - ColorThief based method\n3 - Both')],
                [sg.Text("-1- is default if nothing's chosen")],
                [sg.Button(name) for name in radio_keys],
                [sg.Button('Ok'), sg.Button('Cancel')]  ]

    window = sg.Window('How to build the Palette?', layout, use_default_focus=False, element_justification='c', size=(380,200), grab_anywhere=True)

    while True: # Event Loop            
        event, values = window.read()
        if event in (None, 'Cancel'):
            sys.exit('Canceled')
        if event in radio_keys:
            for k in radio_keys:
                window[k].update(button_color=sg.theme_button_color())
            window[event].update(button_color=selected_color)
            active_radio_button = event
        if event == 'Ok':
            btn_selected = active_radio_button
            break
    window.close()
    return btn_selected

def colors_num():
    num = sg.popup_get_text("2 - is minimum, don't type too much, 3-7 is optimal\n-5- is default if nothing's chosen", 'How much colors on the Palette must be?', grab_anywhere=True)
    if num != '' and num is not None:
        if int(num) < 2: num = 2
        elif int(num) > 24:
            print("Don't be crazy! This's too much! Lowering to 24")
            num = 24
    elif num is None:
        sys.exit('Canceled')
    else:
        num = '5'
    return int(num)