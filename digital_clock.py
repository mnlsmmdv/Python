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

digital_clock_label = digital_clock.Label(window, text = "00:00:00", font = "Monospace 72 ")
digital_clock_label.pack()

update_clock()
window.mainloop()
