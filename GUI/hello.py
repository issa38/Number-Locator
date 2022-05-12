#!/usr/bin/env python
import PySimpleGUI as sg

"""
    Simple test harness to demonstate how to use the CalendarButton and the get date popup
"""
# sg.theme('Dark Red')
layout = [[sg.Text('Calendar', key='-TXT-')],
          [sg.Input(key='-IN-', size=(20, 1)), sg.CalendarButton('Set Start',
                                                                 close_when_date_chosen=True,  target='-IN-', location=(0, 0), no_titlebar=False, )],
          [sg.Input(key='-IN3-', size=(20, 1)), sg.CalendarButton('Choose Date', title='Pick a date any date', no_titlebar=True, close_when_date_chosen=False,  target='-IN3-', begin_at_sunday_plus=1, month_names=(
              'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'Novemeber', 'Decemeber'), day_abbreviations=('Mo', 'Tu', 'We', 'Th', 'F', 'Sa', 'Su'))],
          [sg.Input(key='-IN2-', size=(20, 1)), sg.CalendarButton('Click End Date',  target='-IN2-',
                                                                  default_date_m_d_y=(2, None, 2020), locale='de_DE', begin_at_sunday_plus=1)],
          [sg.Input(key='-IN4-', size=(20, 1)), sg.CalendarButton('Format Test %m-%d Jan 2020',
                                                                  target='-IN4-', format='%m-%d', default_date_m_d_y=(1, None, 2020), )],
          [sg.Button('Read'), sg.Button('Date Popup'), sg.Exit()]]

window = sg.Window('window', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Date Popup':
        sg.popup('You chose:', sg.popup_get_date())
window.close()
