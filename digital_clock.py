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

# Giving the window a variable
window = digital_clock.Tk()
# Main window's title
window.title("hehe")

# Update clock function to display time in 24hrs format
def update_digital_clock():
    # Display the hour
    hours = time.strftime("%I")
    # Display the minute
    minutes = time.strftime("%M")
    # Display the second
    seconds = time.strftime("%S")
    # Display the current time format
    am_or_pm = time.strftime("%p")
    # Time layout in the digital clock
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    # Digital clock basic configurations
    digital_clock_label.config(text = time_text, background = "black", foreground = "red")
    # Configuration to update the clock after each second
    digital_clock_label.after(1000, update_digital_clock)

# The default time for the clock and the font is set
digital_clock_label = digital_clock.Label(window, text = "00:00:00", font = "Monospace 72 ")
# Packing the label configuration to execute
digital_clock_label.pack()

# Calling the update clock function
update_digital_clock()

# Calling the main window of the program so that it executes as a GUI
window.mainloop()

# Program end
