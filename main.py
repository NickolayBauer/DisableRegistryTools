from tkinter import *
from winreg import *
root = Tk()

def box_set():
	key = OpenKey(HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Policies\System",0, KEY_ALL_ACCESS)
	SetValueEx(key, "DisableRegistryTools", 0, REG_DWORD, 1)
	key.Close()
	print("Регистр заблокирован")

def box_clear():
	key = OpenKey(HKEY_CURRENT_USER,r"Software\Microsoft\Windows\CurrentVersion\Policies\System",0, KEY_ALL_ACCESS)
	SetValueEx(key, "DisableRegistryTools", 0, REG_DWORD, 0)
	key.Close()
	print("Регистр заблокирован")	


button1 = Button(root,						   
             	 text="SET",
             	 width=30,height=5,
             	 bg="white",fg="black", command = box_set)
button1.pack()


button2 = Button(root,						    
             	 text="CLEAR",
             	 width=30,height=5,
             	 bg="white",fg="black", command = box_clear)
button2.pack()





root.mainloop()
