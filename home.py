from lib2to3.pytree import convert
import PySimpleGUI as sg

layout = [
    [sg.Input(key="input"),sg.Spin(['Km to miles', 'Kg to pound', 'sec to min'],key="units"), sg.Button('Convert',key='convert')],
    [sg.Text('Output', key="output")]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'convert':
        input_value = values["input"]
        if input_value.isnumeric():
            match values['units']:
                case 'Km to miles':
                    output = float(input_value) * 0.6214
                    output_string = f'{input_value} km is {output} miles.'

                case 'Kg to pound':
                    output = float(input_value) * 2.20462
                    output_string = f'{input_value} kg is {output} pounds.'

                case 'sec to min':
                    output = float(input_value) / 60
                    output_string = f'{input_value} sec is {output} mins.'


            window['output'].update(output_string)

        else:
            window['output'].update('Please enter numeric value.')

window.close()

