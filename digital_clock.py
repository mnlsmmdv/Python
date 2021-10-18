#######################################################
# Name: Ahmed Affaan                                  #
# Title: digital_clock.py                             #
# Date: 19/10/2021                                    #
# Country: Maldives                                   #
# Description: Digital Clock                          #
# Note: Uncomment codes to execute and comment        #
#       them when not in use.                         #
#######################################################

# Program start
import tkinter as digital_clock
import time

window = digital_clock.Tk()
window.title("hehe")

def update_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    digital_clock_label.config(text = time_text, background = "black", foreground = "red")
    digital_clock_label.after(1000, update_clock)

# The default time for the clock and the font is set
digital_clock_label = digital_clock.Label(window, text = "00:00:00", font = "Monospace 72 ")
# Packing the label configuration to execute
digital_clock_label.pack()

# Calling the update clock function
update_clock()
# Calling the main window of the program so that it executes as a GUI
window.mainloop()

# Program end
