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
    return int(n, 2)


def getBinaryIP(num):  # get split value  from splitIP
    bin_IP = ''
    for x in splitIP(num):
        binVal = decimalToBinary(int(x))
        bin_IP += str(binVal)
    return bin_IP


def getSubnetDecimal(num):  # get split value  from splitIP
    dec_IP = ''
    list_len = len(splitIP_2(num))-1
    c = 0
    for x in splitIP_2(num):
        decVal = binaryToDecimal(str(x))
        dec_IP += str(decVal)
        if list_len > c:
            dec_IP += ' . '
        c += 1
    return dec_IP


# All the stuff inside window
fixedlen = [[sg.Text('Network Class')],
            [sg.Radio('Any', default=False, group_id='1',
                      key='any', enable_events=True)],
            [sg.Radio('A', default=False, group_id='1',
                      key='a', enable_events=True)],
            [sg.Radio('B', default=False, group_id='1',
                      key='b', enable_events=True)],
            [sg.Radio('C', default=False, group_id='1', key='c', enable_events=True)]]

varlen = [[sg.Text('Subnet Mask'),
           sg.Combo(['\t\t\t'], key='vl_sbmsk', readonly=True, enable_events=True)],
          [sg.Text('Ex: 100,12,20')],
          [sg.Multiline('', size=(20, 5), key='vl_hosts', enable_events=True)]]


layout = [[sg.Text('IP Address'), sg.InputText()],
          [sg.Radio('Fixed-Length', "RADIO1", enable_events=True, key='fl', default=False),
           sg.Radio('Variable-Length', "RADIO1", enable_events=True, key='vl', default=False)],
          [sg.Frame('Select A Class', fixedlen, title_color='White'),
           sg.Frame('Type needed no of hosts', varlen, title_color='White')],
          [sg.Text('Subnet Mask'), sg.Combo(
              ['\t\t\t'], key='sbmsk', readonly=True, enable_events=True)],
          [sg.Text('No. of Hosts '), sg.InputText(
              '', size=(10, 1), key='input_host', enable_events=True)],
          [sg.Text('\n')],
          [sg.Text('Results')],
          [sg.Multiline('', size=(65, 15), key='resultbox')],
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
        window.Element('vl_sbmsk').Update(values=sb_32)

        # resultbox

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
        no_hosts = values['input_host']
        z = 1
        while (2**z) < int(values['input_host'])+2:
            z += 1
        max_hosts = 2**z
        subnetmsk = 32-z
        sbnt_str = str(toBinarySubnet(int(subnetmsk)))
        ok_binsbnt = ' . '.join(sbnt_str[i:i+8]
                                for i in range(0, len(sbnt_str), 8))
        DecSbnet_msk = getSubnetDecimal(str(ok_binsbnt))

        # network address get
        bin_ip_str = getBinaryIP((values[0]))
        y = str(bin_ip_str)[subnetmsk:32]
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '0'
        netwrk_addr = h
        # convert
        ok_binNetwrk_addr = ' . '.join(netwrk_addr[i:i+8]
                                       for i in range(0, len(netwrk_addr), 8))
        Dec_binNetwrk_addr = getSubnetDecimal(str(ok_binNetwrk_addr))

        # broadcast address get
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '1'
        bdcst_addr = h
        # convert
        ok_binBrdcst_addr = ' . '.join(bdcst_addr[i:i+8]
                                       for i in range(0, len(bdcst_addr), 8))
        Dec_binBrdcst_addr = getSubnetDecimal(str(ok_binBrdcst_addr))

        # take 1st host
        ip_rangeLeft = int(netwrk_addr)+1
        ip_rangeLeft = ('{:032d}'.format(ip_rangeLeft))
        # convert
        ok_ip_rangeLeft = ' . '.join(ip_rangeLeft[i:i+8]
                                     for i in range(0, len(ip_rangeLeft), 8))
        Dec_ip_rangeLeft = getSubnetDecimal(str(ok_ip_rangeLeft))

        # take last host
        ip_rangeRight = int(bdcst_addr)-1
        ip_rangeRight = ('{:032d}'.format(ip_rangeRight))
        # convert
        ok_ip_rangeRight = ' . '.join(ip_rangeRight[i:i+8]
                                      for i in range(0, len(ip_rangeRight), 8))
        Dec_ip_rangeRight = getSubnetDecimal(str(ok_ip_rangeRight))

        # Get Wildcart
        bin_wildcart = 11111111111111111111111111111111-int(sbnt_str)
        bin_wildcart = ('{:032d}'.format(bin_wildcart))
        # convert
        ok_wildcart = ' . '.join(bin_wildcart[i:i+8]
                                 for i in range(0, len(bin_wildcart), 8))
        Dec_wildcart = getSubnetDecimal(str(ok_wildcart))

        window.Element('resultbox').Update(value='Host IP Range:\t '+Dec_binNetwrk_addr+' - '+Dec_binBrdcst_addr+'\n' +
                                           'First usable Host IP in Binary:\t '+ip_rangeLeft+'\n' +
                                           'Last usable Host IP in Binary:\t '+ip_rangeRight+'\n' +
                                           'No. of hosts:\t '+no_hosts+' max ('+str(max_hosts)+')'+'\n' + '\n' +

                                           'Subnet Mask:\t'+DecSbnet_msk+'\n' +
                                           'Binary Subnet Mask: \t'+ok_binsbnt+'\n' +
                                           'CIDR Notation:\t '+'\\ ' +
                                           str(subnetmsk)+'\n' + '\n' +

                                           'Network Address:\t '+Dec_binNetwrk_addr+'\n' +
                                           'Broadcast Addresss:\t '+Dec_binBrdcst_addr+'\n' +
                                           'Binary Network Address:\t '+netwrk_addr+'\n' +
                                           'Binary Broadcast Address:\t '+bdcst_addr+'\n' +
                                           'Wildcard Mask:\t '+Dec_wildcart+'\n'
                                           'Wildcard Mask in Binary:\t '+bin_wildcart+'\n'
                                           )

    if event == 'sbmsk':
        subnetmsk = values['sbmsk']
        no_hosts = str((2**(32-subnetmsk))-2)
        sbnt_str = str(toBinarySubnet(int(subnetmsk)))
        ok_binsbnt = ' . '.join(sbnt_str[i:i+8]
                                for i in range(0, len(sbnt_str), 8))
        DecSbnet_msk = getSubnetDecimal(str(ok_binsbnt))

        # network address get
        bin_ip_str = getBinaryIP((values[0]))
        y = str(bin_ip_str)[subnetmsk:32]
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '0'
        netwrk_addr = h
        # convert
        ok_binNetwrk_addr = ' . '.join(netwrk_addr[i:i+8]
                                       for i in range(0, len(netwrk_addr), 8))
        Dec_binNetwrk_addr = getSubnetDecimal(str(ok_binNetwrk_addr))

        # broadcast address get
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '1'
        bdcst_addr = h
        # convert
        ok_binBrdcst_addr = ' . '.join(bdcst_addr[i:i+8]
                                       for i in range(0, len(bdcst_addr), 8))
        Dec_binBrdcst_addr = getSubnetDecimal(str(ok_binBrdcst_addr))

        # take 1st host
        ip_rangeLeft = int(netwrk_addr)+1
        ip_rangeLeft = ('{:032d}'.format(ip_rangeLeft))
        # convert
        ok_ip_rangeLeft = ' . '.join(ip_rangeLeft[i:i+8]
                                     for i in range(0, len(ip_rangeLeft), 8))
        Dec_ip_rangeLeft = getSubnetDecimal(str(ok_ip_rangeLeft))

        # take last host
        ip_rangeRight = int(bdcst_addr)-1
        ip_rangeRight = ('{:032d}'.format(ip_rangeRight))
        # convert
        ok_ip_rangeRight = ' . '.join(ip_rangeRight[i:i+8]
                                      for i in range(0, len(ip_rangeRight), 8))
        Dec_ip_rangeRight = getSubnetDecimal(str(ok_ip_rangeRight))

        # Get Wildcart
        bin_wildcart = 11111111111111111111111111111111-int(sbnt_str)
        bin_wildcart = ('{:032d}'.format(bin_wildcart))
        # convert
        ok_wildcart = ' . '.join(bin_wildcart[i:i+8]
                                 for i in range(0, len(bin_wildcart), 8))
        Dec_wildcart = getSubnetDecimal(str(ok_wildcart))

        window.Element('resultbox').Update(value='Host IP Range:\t '+Dec_binNetwrk_addr+' - '+Dec_binBrdcst_addr+'\n' +
                                           'First usable Host IP in Binary:\t '+ip_rangeLeft+'\n' +
                                           'Last usable Host IP in Binary:\t '+ip_rangeRight+'\n' +
                                           'No. of Maximum hosts:\t '+no_hosts+'\n'+'\n' +

                                           'Subnet Mask:\t'+DecSbnet_msk+'\n' +
                                           'Binary Subnet Mask: \t'+ok_binsbnt+'\n' +
                                           'CIDR Notation:\t '+'\\ ' +
                                           str(subnetmsk)+'\n' + '\n' +

                                           'Network Address:\t '+Dec_binNetwrk_addr+'\n' +
                                           'Broadcast Addresss:\t '+Dec_binBrdcst_addr+'\n' +
                                           'Binary Network Address:\t '+netwrk_addr+'\n' +
                                           'Binary Broadcast Address:\t '+bdcst_addr+'\n' +
                                           'Wildcard Mask:\t '+Dec_wildcart+'\n'
                                           'Wildcard Mask in Binary:\t '+bin_wildcart+'\n'
                                           )
    if event == 'vl_hosts':
        no_hosts = values['vl_hosts']
        subnetmsk = values['sbmsk']
        no_hosts = str((2**(32-subnetmsk))-2)
        sbnt_str = str(toBinarySubnet(int(subnetmsk)))
        ok_binsbnt = ' . '.join(sbnt_str[i:i+8]
                                for i in range(0, len(sbnt_str), 8))
        DecSbnet_msk = getSubnetDecimal(str(ok_binsbnt))

        # network address get
        bin_ip_str = getBinaryIP((values[0]))
        y = str(bin_ip_str)[subnetmsk:32]
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '0'
        netwrk_addr = h
        # convert
        ok_binNetwrk_addr = ' . '.join(netwrk_addr[i:i+8]
                                       for i in range(0, len(netwrk_addr), 8))
        Dec_binNetwrk_addr = getSubnetDecimal(str(ok_binNetwrk_addr))

        # broadcast address get
        h = str(bin_ip_str)[0:subnetmsk]
        for r in range(0, len(y)):
            h += '1'
        bdcst_addr = h
        # convert
        ok_binBrdcst_addr = ' . '.join(bdcst_addr[i:i+8]
                                       for i in range(0, len(bdcst_addr), 8))
        Dec_binBrdcst_addr = getSubnetDecimal(str(ok_binBrdcst_addr))

        # take 1st host
        ip_rangeLeft = int(netwrk_addr)+1
        ip_rangeLeft = ('{:032d}'.format(ip_rangeLeft))
        # convert
        ok_ip_rangeLeft = ' . '.join(ip_rangeLeft[i:i+8]
                                     for i in range(0, len(ip_rangeLeft), 8))
        Dec_ip_rangeLeft = getSubnetDecimal(str(ok_ip_rangeLeft))

        # take last host
        ip_rangeRight = int(bdcst_addr)-1
        ip_rangeRight = ('{:032d}'.format(ip_rangeRight))
        # convert
        ok_ip_rangeRight = ' . '.join(ip_rangeRight[i:i+8]
                                      for i in range(0, len(ip_rangeRight), 8))
        Dec_ip_rangeRight = getSubnetDecimal(str(ok_ip_rangeRight))

        # Get Wildcart
        bin_wildcart = 11111111111111111111111111111111-int(sbnt_str)
        bin_wildcart = ('{:032d}'.format(bin_wildcart))
        # convert
        ok_wildcart = ' . '.join(bin_wildcart[i:i+8]
                                 for i in range(0, len(bin_wildcart), 8))
        Dec_wildcart = getSubnetDecimal(str(ok_wildcart))

        window.Element('resultbox').Update(value='Host IP Range:\t '+Dec_binNetwrk_addr+' - '+Dec_binBrdcst_addr+'\n' +
                                           'First usable Host IP in Binary:\t '+ip_rangeLeft+'\n' +
                                           'Last usable Host IP in Binary:\t '+ip_rangeRight+'\n' +
                                           'No. of Maximum hosts:\t '+no_hosts+'\n'+'\n' +

                                           'Subnet Mask:\t'+DecSbnet_msk+'\n' +
                                           'Binary Subnet Mask: \t'+ok_binsbnt+'\n' +
                                           'CIDR Notation:\t '+'\\ ' +
                                           str(subnetmsk)+'\n' + '\n' +

                                           'Network Address:\t '+Dec_binNetwrk_addr+'\n' +
                                           'Broadcast Addresss:\t '+Dec_binBrdcst_addr+'\n' +
                                           'Binary Network Address:\t '+netwrk_addr+'\n' +
                                           'Binary Broadcast Address:\t '+bdcst_addr+'\n' +
                                           'Wildcard Mask:\t '+Dec_wildcart+'\n'
                                           'Wildcard Mask in Binary:\t '+bin_wildcart+'\n'
                                           )

    # I run when clicked
    # sb_load()

    # print('You entered ', values[0])

window.close()
