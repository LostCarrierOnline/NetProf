import wmi
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
    #You need to scrape

def add_nic():
    print('placeholder, add nic settings')
    #add nic settings


backup_nic(0)