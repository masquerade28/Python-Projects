from tkinter import Label, Tk
import time

app_window = Tk()

# Giving Title To Our Clock Window
app_window.title("Digital Clock")

# Setting Up The Dimensions Of The window 
app_window.geometry("420x150")

# By Setting Up The Resizeable Fuction As True(1,1), We Are Making The Window Resizeable
app_window.resizable(1,1)

# Defining The Label With Characteristics Of Clock
label = Label(app_window, font=("Boulder", 68, 'bold'), bg="#000", fg="#fff", bd=25)

# Placing The Label on Our Window 
label.grid(row=1, column=1)

# Defining The Main Function Of Our Clock
def digital_clock():
    time_live = time.strftime("%H:%M:%S")

    # Updating The Label
    label.config(text=time_live)

    # Now we will Schedule The calling Of Our Function
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
