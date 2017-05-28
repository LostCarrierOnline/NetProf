from tkinter import *
import tkinter.messagebox
import profile

rootW = Tk()
rootW.title('NetProf')
rootW.geometry("250x150")


def save_popup():
    tkinter.messagebox.showinfo(title='Save Dialog', message='Profile Configuration Saved')

def addProfile(self):
    profileW = Toplevel()
    profileW.title('Add Network Profile')
    profileW.geometry("250x150")

    label_name = Label(profileW, text='Name: ')
    name_entry = Entry(profileW)
    label_name.grid(row=0, sticky=E)
    name_entry.grid(row=0, column=1)

    label_ip = Label(profileW, text='IP: ')
    ip_entry = Entry(profileW)
    label_ip.grid(row=1, sticky=E)
    ip_entry.grid(row=1, column=1)

    label_subnet = Label(profileW, text='Subnet: ')
    subnet_entry = Entry(profileW)
    label_subnet.grid(row=2, sticky=E)
    subnet_entry.grid(row=2, column=1)

    label_gateway = Label(profileW, text='Gateway: ')
    gateway_entry = Entry(profileW)
    label_gateway.grid(row=3, sticky=E)
    gateway_entry.grid(row=3, column=1)

    buttonSave = Button(profileW, text='Save')
    buttonSave.bind('buttonSave', lambda event: save_popup) #still doesn't fucking work, no idea why.
    buttonSave.grid(row=4, column=0)


    buttonSet = Button(profileW, text='Set')
    buttonSet.bind('buttonSet', meh) #still doesn't fucking work, no idea why.
    buttonSet.grid(row=5, column=0)

    #buttonSave = Button(profileW, text='Save')
    #buttonSave.bind("<Button-2>", command=save_popup)
    #buttonSave.grid(row=4, column=1)


topFrame = Frame(rootW)
topFrame.pack()

buttonAdd = Button(topFrame, text='Add Network Profile')
buttonAdd.bind("<Button-1>", addProfile)
buttonAdd.pack(side=RIGHT)

##create the status bar
status = Label(rootW, text='Network Profiles Disabled...', bd=1, relief=SUNKEN, anchor=W)# adding boarder and relief to change how the status bar looks
status.pack(side=BOTTOM, fill=X)


rootW.mainloop()