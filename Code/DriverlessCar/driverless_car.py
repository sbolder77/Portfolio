'''module to represent a car and how it interacts with the class simulated data in a simple UI'''
from tkinter import *
import tkinter.messagebox
import tkinter as tk
import journey
import sensor
import drive

#region objects
j = journey.JourneyDetails()
s = sensor.Sensors()
d = drive.Speed()
#endregion

#region form
'''main form definition'''
mainForm = Tk()
mainForm.title("Driverless Car")
mainForm.geometry('310x400')
mainForm.resizable(False,False)
mainForm.configure(background="grey90")
#endregion

#region functions
def update():
    '''update the control contents after updates'''
    lbl_distance_covered.configure(text = '')
    lbl_distance_covered.configure(text = 'Distance covered - ' + str(j.get_miles_covered()) + ' - miles')
    lbl_elapsed_minutes.configure(text = '')
    lbl_elapsed_minutes.configure(text = 'Time travelled - ' + str(j.get_elapsed_minutes()) + ' - minutes')
    btn_start.configure(text = '')
    btn_start.configure(text = 'Update Journey')

def charge_battery():
    '''updates the 'virtual' battery charge state and set the initial state of the labels on the main form'''
    msg_box = tkinter.messagebox.askquestion("Notification", "Are you sure you want to charge the battery?", icon='warning')
    if msg_box == 'yes':
        lbl_charge_status.config(text = d.set_charge_status('Y'))
        btn_start.config(state = ACTIVE)
        lbl_start_time.config(text = 'Start Time - ' + str(j.get_start_time()))
        lbl_start_address.config(text = 'Start Address - ' + j.get_start_address())
        lbl_finish_address.config(text = 'Finish Address - ' + j.get_finish_address())
        lbl_distance.config(text = 'Distance - ' + str(j.get_distance()) + ' miles')
        lbl_distance_covered.config(text = 'Distance covered - 0 - miles')
        lbl_elapsed_minutes.config(text = 'Time travelled - 0 - minutes')

def start_journey():
    '''public variables to be used for initialisation on main form'''
    journey_started = False
    elapsed_minutes = 0
    miles_covered = j.get_miles_covered()
    speed_zone = ''
    current_speed = 0

    if miles_covered >= j.get_distance():
        btn_start.configure(state = DISABLED)
        speed_zone = ''
        miles_covered = 0.0
        current_speed = 0
        btn_close.config(text = 'Journey ended - Close form', state = ACTIVE)
    else:
        journey_started = True
        if journey_started:
            assert journey_started is True, f"Journey started is {True}"
            btn_start.after(1000, update)
            if miles_covered <= j.get_res_miles():
                speed_zone = 'R'
                assert speed_zone == 'R', "Your are in a residential speed limit zone"
                current_speed = d.get_speed(speed_zone)
                assert current_speed == 30, f"Current speed is {current_speed} mph"
                lbl_speed.configure(text = 'Current Speed - ' + str(current_speed) + ' mph', background="LightGreen", foreground="White")
            else:
                speed_zone = 'N'
                assert speed_zone == 'N', "Your are in a national speed limit zone"
                current_speed = d.get_speed(speed_zone)
                assert current_speed > 30, "Current speed is {CURRENT_SPEED} mph"
                lbl_speed.configure(text = 'Current Speed - ' + str(current_speed) + ' mph', background="LightGreen", foreground="White")

    elapsed_minutes += 1
    alert = s.get_alerts(speed_zone, miles_covered, current_speed)
    if len(alert) > 0:
        if alert[0] == 0:
            msg_box = tkinter.messagebox.askquestion("Notfication", "You are stopped for a red traffic light - do you want to continue?", icon='info')
            if msg_box == 'yes':
                assert msg_box == 'yes', "You have chosen to continue"
                j.set_miles_covered(alert[0], elapsed_minutes)
                j.set_elapsed_minutes(elapsed_minutes)
                lbl_speed.configure(text = 'Current Speed - ' + str(alert[0]) + ' mph')
                lbl_alert.configure(text = 'Warning - ' + alert[1], background="Blue", foreground="White")
        else:
            assert len(alert) > 0, f"You have an alert - {str(alert[0])} mph and alert is {str(alert[1])}"
            j.set_miles_covered(alert[0], elapsed_minutes)
            j.set_elapsed_minutes(elapsed_minutes)
            lbl_speed.configure(text = 'Current Speed - ' + str(alert[0]) + ' mph')
            lbl_alert.configure(text = 'Warning - ' + alert[1], background="Blue", foreground="White")
    else:
        j.set_miles_covered(current_speed, elapsed_minutes)
        j.set_elapsed_minutes(elapsed_minutes)
        lbl_alert.configure(text = '', background="grey90", foreground="grey90")

    lbl_distance_covered.after(1000, update)
    lbl_elapsed_minutes.after(1000, update)


def close():
    '''closes the tkinter form'''
    mainForm.quit()
#endregion

#region controls
btn_charge_battery = Button(mainForm, bd=3, width=40, height=1, text="Charge Battery", command = charge_battery, background="grey90")
btn_charge_battery.place(relx=0.03, rely=0.04)

lbl_charge_status = tk.Label(mainForm, width=20, anchor="w", background="grey90")
lbl_charge_status.place(relx=0.03, rely=0.12)

btn_start = Button(mainForm, bd=3, width=40, height=1, text="Start Journey", command = start_journey, state = DISABLED, background="grey90")
btn_start.place(relx=0.03, rely=0.18)

lbl_start_time = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_start_time.place(relx=0.03, rely=0.26)

lbl_start_address = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_start_address.place(relx=0.03, rely=0.31)

lbl_finish_address = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_finish_address.place(relx=0.03, rely=0.36)

lbl_distance = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_distance.place(relx=0.03, rely=0.41)

lbl_distance_covered = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_distance_covered.place(relx=0.03, rely=0.46)

lbl_elapsed_minutes = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_elapsed_minutes.place(relx=0.03, rely=0.51)

lbl_speed = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_speed.place(relx=0.03, rely=0.58)

lbl_alert = tk.Label(mainForm, width=40, anchor="w", background="grey90")
lbl_alert.place(relx=0.03, rely=0.65)

btn_close = Button(mainForm, bd=3, width=40, height=1, text="Close form", command = close, state = DISABLED, background="grey90")
btn_close.place(relx=0.03, rely=0.75)
#endregion

def main():
    '''on initial load of form to display th battery charge status'''
    charge = d.get_charge_status()
    if charge is False:
        lbl_charge_status.config(text = 'The car is not charged')

if __name__ == '__main__':
    main()
    mainForm.mainloop()
