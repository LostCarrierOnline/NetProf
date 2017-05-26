import wmi
import fileinput
import re
#pip install pypiwin32

def backup_nic(device):
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)
    nic = nic_configs[int(device)]
    print(nic)
    output = str(nic)
    with open('nic-backup.txt', 'w') as f:
        f.write(output)

def list_nic():
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=True)


def gw_ip(gateway_ip, device):
    backup_nic(device)
    #DefaultIPGateway = {"(.*?)"};
    with open('nic-backup.txt', 'r') as myfile:
        #data = myfile.read()
        #modified = data.replace('DefaultIPGateway = {"(.?)"};', 'DefaultIPGateway = {"%s"};' % gateway_ip)
        modified = re.sub(r'DefaultIPGateway = {"(.*)"};\n', 'DefaultIPGateway = {"%s"};\n' % gateway_ip, myfile.read())
        print(modified)


#backup_nic(0)
gw_ip('Just a test', '0')