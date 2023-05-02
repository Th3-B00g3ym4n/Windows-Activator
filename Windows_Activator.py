from customtkinter import *
from time import sleep as wait
from os import system as cmd

home = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
homeN = "3KHY7-WNT83-DGQKR-F7HPR-844BM"
homeSL = "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
homeCS = "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR"
pro = "W269N-WFGWX-YVC9B-4J6C9-T83GX"
proN = "MH37W-N47XK-V7XM9-C7227-GCQG9"
edu = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
eduN = "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
ent = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
entN = "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"

Enabled = False

Key_Lib=["Home Edition", "Home N Edition", "Home Single Language", "Home Country Specific", "Professional Edition", "Professional N Edition", "Education Edition", "Education N Edition", "Enterprise Edition", "Enterprise N Edition", "Custom"]

set_appearance_mode("dark")

win = CTk()
win.title("Windows Activator")
win.geometry("450x400")
win.resizable(False, False)



def Activate():
  selection = op.get()

  sel = Key_Lib.index(selection)

  if sel == 0:
    key = home
  elif sel == 1:
    key = homeN
  elif sel == 2:
    key = homeSL
  elif sel == 3:
    key = homeCS
  elif sel == 4:
    key = pro
  elif sel == 5:
    key = proN
  elif sel == 6:
    key = edu
  elif sel == 7:
    key = eduN
  elif sel == 8:
    key = ent
  elif sel == 9:
    key = entN
  elif sel == 10:
    key = custom_key.get()

  cmd(f"slmgr /ipk {key}")
  cmd(f"slmgr /skms kms8.msguides.com")
  cmd("slmgr /ato")


def enabler():
  global Enabled

  if Enabled == True:
    custom_key.configure(placeholder_text="", state='disabled')
    
    Enabled = False
  
  else:
    custom_key.configure(placeholder_text ="Enter Custom Key...", state='normal')
    
    Enabled = True

  
title = CTkLabel(win, text = "Windows Activator", font=("Impact", 20))
title.place(x=125, y=50)


op = CTkOptionMenu(win, values=["Home Edition", "Home N Edition", "Home Single Language", "Home Country Specific", "Professional Edition", "Professional N Edition", "Education Edition", "Education N Edition", "Enterprise Edition", "Enterprise N Edition", "Custom"])
op.configure(height=30, width=400)
op.place(x=25, y=150)


custom_key_Enabler = CTkSwitch(win, text="Custom Key", command=enabler)
custom_key_Enabler.place(x=25, y=245)

custom_key = CTkEntry(win, placeholder_text ="Enter Custom Key...", height=30, width=400, state='disabled')
custom_key.place(x=25, y=275)


activate_btn = CTkButton(win, text="Activate", font=("Impact", 15), command=Activate)
activate_btn.configure(height=30, width=400)
activate_btn.place(x=25, y=350)


win.mainloop()

