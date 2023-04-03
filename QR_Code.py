import qrcode as qr
import PySimpleGUI as sg 

sg.theme('Purple')
font =('Verdana', 13)

qr_image = [sg.Image('', key = 'QRCODE')]

# the layout
index = 0
color = {0: ("white", "blue"), 1: ("red", "green")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'green', key= 'URL' )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE', size= (7,1))],
    [sg.Column([qr_image], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['URL']
        if url:
            qr_code = qr.QRCode(
                version=1,
                error_correction=qr.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
                )
            qr_code.add_data('Some data')
            qr_code.make(fit=True)
            img = qr_code.make_image(fback_color=(205, 92, 92), fill_color=(240, 128, 128))
            img.save('qr_code'+'.png')
            window['QRCODE'].update('qr_code'+'.png')
window.close()