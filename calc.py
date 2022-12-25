import PySimpleGUI as sg
import math

sg.theme('DarkAmber')   # Add a touch of color

# arrays
sb_32 = list(range(32, -1, -1))
sb_a = list(range(32, 7, -1))
sb_b = list(range(32, 15, -1))
sb_c = list(range(32, 23, -1))
sb_d = list(range(23, 13, -1))


# methods

def sb_load():
    window.Element('resultbox').Update(value='Host IP Range:\t '+'125.210.12.45'+' - '+'255.211.412.12'+'\n' +
                                       'Subnet Mask:\t'+'255.255.255.255'+'\n' +
                                       'Binary Subnet Mask: \t'+toBinarySubnet(int(values['sbmsk']))+'\n' +
                                       'Network Address:\t '+'244.242.3535.353'+'\n' +
                                       'Braodcast Addresss:\t '+'645.5435.353.535'+'\n' +
                                       'Wildcard Mask:\t '+'0.21.212.452'+'\n'
                                       'CIDR Notation:\t '+'\\ ' +
                                       str(values['sbmsk'])+'\n'
                                       )


def host_load():
    window.Element('resultbox').Update(value='Host IP Range:\t '+'125.210.12.45'+' - '+'255.211.412.12'+'\n' +
                                       'Subnet Mask:\t'+'255.255.255.255'+'\n' +
                                       'Binary Subnet Mask: \t'+toBinarySubnet(int(values['sbmsk']))+'\n' +
                                       'Network Address:\t '+'244.242.3535.353'+'\n' +
                                       'Braodcast Addresss:\t '+'645.5435.353.535'+'\n' +
                                       'Wildcard Mask:\t '+'0.21.212.452'+'\n'
                                       'CIDR Notation:\t '+'\\ ' +
                                       str(values['sbmsk'])+'\n'
                                       )


def toBinarySubnet(num):
    ones = ''
    for j in range(0, num):
        ones += '1'
    rem_0s = 32-num
    zeros = ''
    for i in range(0, rem_0s):
        zeros += '0'
    return (ones+zeros)

def splitIP(num):
    return num.split('.')

def splitIP_2(num):
    return num.split(' . ')


def decimalToBinary(n):
    return format(n, '08b')

def binaryToDecimal(n):
    return int(n,2)

def getBinaryIP(num):  # get split value  from splitIP
    bin_IP = ''
    for x in splitIP(num):
        binVal = decimalToBinary(int(x))
        bin_IP += str(binVal)
    return bin_IP

def getSubnetDecimal(num):  # get split value  from splitIP
    dec_IP = ''
    list_len=len(splitIP_2(num))-1
    c=0
    for x in splitIP_2(num):
        decVal = binaryToDecimal(str(x))
        dec_IP += str(decVal)
        if list_len>c:
            dec_IP += ' . '
        c+=1
    return dec_IP


# All the stuff inside your window.
classless = [[sg.Text('Subnet Mask')],
             [sg.Combo(['32', '31', '30'], default_value='32', key='sbmsk1')]]

classfull = [[sg.Text('Network Class')],
             [sg.Radio('Any', default=False, group_id='1',
                       key='any', enable_events=True)],
             [sg.Radio('A', default=False, group_id='1',
                       key='a', enable_events=True)],
             [sg.Radio('B', default=False, group_id='1',
                       key='b', enable_events=True)],
             [sg.Radio('C', default=False, group_id='1', key='c', enable_events=True)]]

layout = [[sg.Text('IP Address'), sg.InputText()],
          [sg.Radio('Fixed-Length', "RADIO1", enable_events=True, key='fl', default=False),
           sg.Radio('Variable-Length', "RADIO1", enable_events=True, key='vl', default=False)],
          [sg.Frame('Select A Class', classfull, title_color='White'),
           sg.Frame('Select Subnet Mask', classless, title_color='White')],
          [sg.Text('Subnet Mask')],
          [sg.Combo(['\t\t\t'], key='sbmsk', readonly=True, enable_events=True)],
          [sg.Text('No. of Hosts'), sg.InputText(
              '', size=(10, 1), key='input_host', enable_events=True)],
          [sg.Text(' No. of Subnets')],
          [sg.Combo(['\t\t\t'], key='no_sbnts',
                    readonly=True, enable_events=True)],
          [sg.Text('\n')],
          [sg.Text('Results')],
          [sg.Multiline('', size=(65, 10), key='resultbox')],
          [sg.Listbox(values=['Welcome Drink', 'Extra Cushions', 'Organic Diet', 'Blanket', 'Neck Rest', 'fgf',
                      'fgfgfg', 'dfgdfg', 'weqrwer', 'reterter', 'rete'], select_mode='extended', key='fac', size=(30, 6))],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Subnet Calculator', layout, finalize=True)
# window['no_hosts'].bind("<Return>", "_Enter")

new_values = ['Bill', 'Jeff']
key_list_class = 'any', 'a', 'b', 'c'
sb_msk_list = 'any', 'a', 'b', 'c'

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    # classless selected
    if event == 'vl':
        # window['ntaddr'].Widget.configure(state = 'normal')
        for key in key_list_class:
            window[key].update(disabled=True)
        window.Element('sbmsk').Update(values=sb_32)

    # classful selected
    if event == 'fl':
        for key in key_list_class:
            window[key].update(disabled=False)

    # change sbnet by class
    if event == 'a':
        window.Element('sbmsk').Update(values=sb_a)

    if event == 'b':
        window.Element('sbmsk').Update(values=sb_b)

    if event == 'c':
        window.Element('sbmsk').Update(values=sb_c)

    if event == 'any':
        window.Element('sbmsk').Update(values=sb_32)

    # event happens when press enter
    # if event == 'no_hosts' + '_Enter':
    #     selected_sbmskk=values['sbmsk']
    #     print (selected_sbmskk)

    if event == 'input_host':
        z = 1
        while (2**z) < int(values['input_host'])+2:
            z += 1
        subnetmsk = 32-z
        sbnt_str= str(toBinarySubnet(int(subnetmsk)))
        ok_binsbnt=' . '.join(sbnt_str[i:i+8] for i in range(0, len(sbnt_str), 8))
        DecSbnet_msk=getSubnetDecimal(str(ok_binsbnt))

        #network address get
        bin_ip_str = getBinaryIP((values[0]))
        y=str(bin_ip_str)[subnetmsk:32]
        h=str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '0'
        netwrk_addr=h

        #braodcast address get
        h=str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '1'
        bdcst_addr=h

        #take 1st host
        ip_rangeLeft=int(netwrk_addr)+1
        ip_rangeLeft=('{:032d}'.format(ip_rangeLeft))

        #take last host
        ip_rangeRight=int(bdcst_addr)-1
        ip_rangeRight=('{:032d}'.format(ip_rangeRight))

        window.Element('resultbox').Update(value='Host IP Range:\t '+ip_rangeLeft+' - '+ip_rangeRight+'\n' +
                                         'Subnet Mask:\t'+DecSbnet_msk+'\n' +
                                         'Binary Subnet Mask: \t'+ok_binsbnt+'\n' +
                                         'CIDR Notation:\t '+'\\ ' +
                                         str(subnetmsk)+'\n'+
                                         'Network Address:\t '+netwrk_addr+'\n' +
                                         'Broadcast Addresss:\t '+'645.5435.353.535'+'\n' +
                                         'Wildcard Mask:\t '+'0.21.212.452'+'\n'

                                         )

    if event == 'sbmsk':
        selected_sbmsk = values['sbmsk']
        print(selected_sbmsk)
        user_ip = (values[0])
        split_IP = splitIP(user_ip)
        print(split_IP)

        mn = getBinaryIP(user_ip)
        print(mn)

        sb_load()

    # I run when clicked
    # sb_load()

    # print('You entered ', values[0])

window.close()
