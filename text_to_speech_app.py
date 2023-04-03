import PySimpleGUI as sg
import pyttsx3 as pt

# Set a theme for the layout
sg.theme('Purple')
# All the staff inside the window.
index = 1
index_1= 0
color = {0: ("white", "blue"), 1: ("yellow", "purple")}
layout = [
    [sg.Text(''), sg.Input(text_color= 'white', key= 'INPUT' ), sg.Button('Speak', key='LISTENER',  mouseover_colors=color[index], use_ttk_buttons=True, size= (7,1)), sg.Text(), sg.Button('Close', key='close',  mouseover_colors=color[index_1], use_ttk_buttons=True, size= (7,1))],
    [sg.Text('Select voice type:'), sg.Radio("Male", "RADIO", default= True, key='MALE'),sg.Radio('Female', 'RADIO', default = False, key ='FEMALE' )],
    [sg.Text( key= 'RESULT')],
]

# Create the Window
window = sg.Window('Text to Speech App', layout)

# Event loop
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'close':
        break
    elif event == 'LISTENER':
        Text = str(values['INPUT'])
        eng = pt.init() # Initialise the instance
        eng.setProperty('rate', 180)
        eng.setProperty('volume',1.0)
               
        voice = eng.getProperty('voices') # get the available voice 
        Male = values['MALE']
        Female= values['FEMALE']
        if Male:
            eng.setProperty('voice', voice[0].id) # set the voice to index 0 for male voice
        elif Female :
            eng.setProperty('voice', voice[1].id) # set the voice to index 1 for female voice
        
        result = eng.say(Text)    
        eng.runAndWait()
        window['RESULT'].update(result)
window.close()
