import wmi
import re

# pip install pypiwin32

debug = 'ON'

def dprint(printable_string):
    if debug == 'ON':
        print('Debug: ' + str(printable_string))
    else:
        pass


def create_profile(name, deviceid, gatewayip, ipaddress, subnet):
    output = deviceid + ',' + gatewayip + ',' + ipaddress + ',' + subnet
    with open('Device' + deviceid + '-' + name + '.bak', 'w') as f:
        f.write(output)


def backup_nic(device):
    dprint('grabbing nic data')
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nic = nic_configs[int(device)]
    dprint(str(nic))
    gateway = re.search('DefaultIPGateway = {"(.*)"};', str(nic)).group(1) #if match find the first one in the group
    dprint('Gateway IP: ' + gateway)
    #Do one for dns 1 and 2
    ipaddress = re.search('IPAddress = {"(.*)"};', str(nic)).group(1)
    dprint('IP address: ' + ipaddress)
    subnet = re.search('IPSubnet = {"(.*)"};', str(nic)).group(1)
    dprint('Subnet: ' + subnet)
    output = device + ',' + gateway + ',' + ipaddress + ',' + subnet
    with open('Device' + device + '.bak', 'w') as f:
        f.write(output)

def current_ip():
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
        dprint(interface.Description, interface.MACAddress)
        for ip_address in interface.IPAddress:
            dprint(ip_address)


def list_nic():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    #device_list = len(nic_configs)
    #go through (starting with zero) and grab the name of each nic with it's device id. Starting with zero.
    #print(device_list)

    for i in range(0, 10): #count up to 10, to be used to find network devices
        try:
            nic_iter = nic_configs[i]
            name_search = re.search('Description = "(.*)";', str(nic_iter)).group(1)
            device_name = str(i) + ' ' + name_search
            print(device_name)
        except(ValueError, IndexError):
            dprint('nic for ' + str(i) + ' doesnt exist')
            pass




# modified = data.replace('DefaultIPGateway = {"(.?)"};', 'DefaultIPGateway = {"%s"};' % gateway_ip)


def set_nic(deviceid, gatewayip, ipaddress, subnet):
    dprint('Setting nic with the following: \r\n \r\n Device ID: ' + str(deviceid) + '\r\n IPAddress: ' + ipaddress + '\r\n Subnet Mask: ' + subnet + '\r\n Gateway: ' + gatewayip)
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    # First network adaptor
    nic = nic_configs[deviceid]
    # Set IP address, subnetmask and default gateway
    # Note: EnableStatic() and SetGateways() methods require *lists* of values to be passed
    nic.EnableStatic(IPAddress=[ipaddress], SubnetMask=[subnet])
    nic.SetGateways(DefaultIPGateway=[gatewayip])

def restore_bak(file):
    data = open(file, 'r').readline().split(',')
    set_nic(int(data[0]), data[1], data[2], data[3])


# backup_nic(0)
# gw_ip('192.168.0.5', '0')

#backup_nic('0')
#set_nic('192.168.0.45', '255.255.255.0', '192.168.0.1', 0)
#restore_bak('Device0.bak')
#create_profile('Default', '0', '192.168.0.1', '192.168.0.45', '255.255.255.0') Testing profile creation
list_nic()