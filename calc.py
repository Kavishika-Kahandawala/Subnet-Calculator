import PySimpleGUI as sg
import math

sg.theme('DarkAmber')   # Add a touch of color

#arrays
sb_32 = list(range(32,-1,-1))
sb_a = list(range(32,7,-1))
sb_b = list(range(32,15,-1))
sb_c = list(range(32,23,-1))
sb_d = list(range(23,13,-1))


#methods
def sb_load():
    window.Element('textbox').Update(value='Host IP Range:\t '+'125.210.12.45'+' - '+'255.211.412.12'+'\n'+
    'Subnet Mask:\t'+'255.255.255.255'+'\n'+
    'Binary Subnet Mask: \t'+toBinarySubnet(int(values['sbmsk']))+'\n'+
    'Subnet Mask: \t'+'354.353.425.242'+'\n'+
    'Network Address:\t '+'244.242.3535.353'+'\n'+
    'Braodcast Addresss:\t '+'645.5435.353.535'+'\n'+
    'Wildcard Mask:\t '+'0.21.212.452'+'\n'
    'CIDR Notation:\t '+'\\ '+str(values['sbmsk'])+'\n'
    )

def toBinarySubnet (num):
    ones=''
    for j in range(0, num):
        ones+='1'
    rem_0s=32-num
    zeros=''
    for i in range(0, rem_0s):
        zeros+='0'
    return (ones+zeros)

def splitIP(num):
    return num.split('.')

def decimalToBinary(n):
    return format(n, '08b')
    
def getBinaryIP(num):   #get split value  from splitIP
    bin_IP=''
    for x in splitIP(num):
        binVal=decimalToBinary(int(x))
        print('bin '+str(binVal))
        bin_IP+=str(binVal)
    return bin_IP


# All the stuff inside your window.
classless = [   [sg.Text('Subnet Mask')],
                [sg.Combo(['32','31','30'],default_value='32',key='sbmsk1')]   ]

classfull = [   [sg.Text('Network Class')],
                [sg.Radio('Any', default=False, group_id='1', key='any', enable_events=True)],
                [sg.Radio('A', default=False, group_id='1', key='a', enable_events=True)],
                [sg.Radio('B', default=False, group_id='1', key='b', enable_events=True)],
                [sg.Radio('C', default=False, group_id='1', key='c', enable_events=True)]   ]

layout = [  [sg.Text('IP Address'), sg.InputText()],
            [sg.Radio('Fixed-Length', "RADIO1", enable_events=True, key='fl',default=False),sg.Radio('Variable-Length', "RADIO1", enable_events=True, key='vl', default=False)],
            [sg.Frame('Select A Class', classfull, title_color='White'),
            sg.Frame('Select Subnet Mask', classless, title_color='White')],
            [sg.Text('Network Address'), sg.InputText(key='ntaddr')],
            [sg.Text('Subnet Mask')],
            [sg.Combo(['\t\t\t'],key='sbmsk',readonly=True ,enable_events=True)],
            [sg.Text('No. of Hosts')],
            [sg.Combo(['\t\t\t'],key='no_hosts',readonly=True ,enable_events=True)],
            [sg.Text(' No. of Subnets')],
            [sg.Combo(['\t\t\t'],key='no_sbnts',readonly=True ,enable_events=True)],
            [sg.Text('\n')],
            [sg.Text('Results')],
            [sg.Multiline('',size=(55, 10), key='textbox')],
            [sg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet','Blanket', 'Neck Rest','fgf','fgfgfg','dfgdfg','weqrwer','reterter','rete'], select_mode='extended', key='fac', size=(30, 6))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Subnet Calculator', layout)

new_values = ['Bill', 'Jeff']
key_list_class = 'any', 'a', 'b', 'c'
sb_msk_list = 'any', 'a', 'b', 'c'

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    #classless selected
    if event == 'vl':
        # window['ntaddr'].Widget.configure(state = 'normal')
        for key in key_list_class:
            window[key].update(disabled=True)
        window.Element('sbmsk').Update(values=sb_32)

    #classful selected
    if event == 'fl':
        for key in key_list_class:
            window[key].update(disabled=False)

    #change sbnet by class    
    if event == 'a':
        window.Element('sbmsk').Update(values=sb_a)

    if event == 'b':
        window.Element('sbmsk').Update(values=sb_b)

    if event == 'c':
        window.Element('sbmsk').Update(values=sb_c)

    if event == 'any':
        window.Element('sbmsk').Update(values=sb_32)
    
    if event == 'sbmsk':
        selected_sbmsk=values['sbmsk']
        print(selected_sbmsk)
        user_ip=(values[0])
        split_IP=splitIP(user_ip)
        print(split_IP)
        
        mn=getBinaryIP(user_ip)
        print(mn)

        sb_load()

    #I run when clicked
    # sb_load()
    
    
    # print('You entered ', values[0])

window.close()