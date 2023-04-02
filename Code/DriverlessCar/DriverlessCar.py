from datetime import datetime
from tkinter import *
import json
from tkinter import ttk
import tkinter.messagebox
import journey
 
# create main form
mainForm = Tk()

# root window title and dimension
mainForm.title("Service Toolkits")
# Set root window properties
mainForm.geometry('800x600')
mainForm.resizable(False,False)

#region classes

#class Drive:
#class Journey:
#class Sensor:




#endregion

def main():
    #mainForm.
    j = journey.JourneyDetails()
    print(j.setStartTime())
    charge = j.getChargeStatus()
    current_speed = 0

    if charge == False:
        print('The car is not charged')
        j.setChargeStatus('Y')
    else:
        print('The car is charged')




if __name__ == '__main__':
    #lbl_Charge_Status = Label(mainForm, width=15, text="ID:", anchor="w")
    #lbl_Charge_Status.place(relx=0.03, rely=0.51)

    #lbl_Start_Time = Label(mainForm, width=15, text="New Values:", anchor="w")
    #lbl_Start_Time.place(relx=0.44, rely=0.51)
    main()


