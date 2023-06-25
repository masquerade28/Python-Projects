
from tkinter import *

root = Tk()
root.title("Calculator")

displayframe = Entry(root, width=18, borderwidth=0.5, font=("Arial", 20), highlightthickness=2)
displayframe.grid(row=0, column=0, columnspan=4, padx=5, pady=5, rowspan=2, sticky = "nsew")
displayframe.config(highlightbackground = "black", highlightcolor= "black")

for i in range(6):
    Grid.rowconfigure(root, index = i, weight = 1)
    i += 1

for j in range(4):
    Grid.columnconfigure(root, index = j, weight = 1)
    j += 1

# Defining Functions
def button_clear():
    displayframe.delete(0, END)

def button_addition():
    global f_num
    first_num = displayframe.get()
    f_num = int(first_num)
    global math
    math = "Addition"
    displayframe.delete(0, END)

def button_subtract():
    global f_num
    first_num = displayframe.get()
    f_num = int(first_num)
    global math
    math = "Substraction"
    displayframe.delete(0, END)

def button_multiply():
    global f_num
    first_num = displayframe.get()
    f_num = int(first_num)
    global math
    math = "Multiplication"
    displayframe.delete(0, END)

def button_divide():
    global f_num
    first_num = displayframe.get()
    f_num = int(first_num)
    global math
    math = "Division"
    displayframe.delete(0, END)

def button_equalto():
    s_num = displayframe.get()
    displayframe.delete(0, END)

    if math == "Addition":
        displayframe.insert(0, f_num + int(s_num))

    elif math == "Substraction":
        displayframe.insert(0, f_num - int(s_num))

    elif math == "Multiplication":
        displayframe.insert(0, f_num * int(s_num))

    elif math == "Division":
        displayframe.insert(0, f_num / float(s_num))    
    

# Creating and Placing the Buttons
button_0 = Button(root, text="0", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 0)).grid(row=5, column=1, pady=1, padx=1, sticky = "nsew")
button_1 = Button(root, text="1", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 1)).grid(row=4, column=0, pady=1, padx=1, sticky = "nsew")
button_2 = Button(root, text="2", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 2)).grid(row=4, column=1, pady=1, padx=1, sticky = "nsew")
button_3 = Button(root, text="3", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 3)).grid(row=4, column=2, pady=1, padx=1, sticky = "nsew")
button_4 = Button(root, text="4", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 4)).grid(row=3, column=0, pady=1, padx=1, sticky = "nsew")
button_5 = Button(root, text="5", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 5)).grid(row=3, column=1, pady=1, padx=1, sticky = "nsew")
button_6 = Button(root, text="6", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 6)).grid(row=3, column=2, pady=1, padx=1, sticky = "nsew")
button_7 = Button(root, text="7", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 7)).grid(row=2, column=0, pady=1, padx=1, sticky = "nsew")
button_8 = Button(root, text="8", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 8)).grid(row=2, column=1, pady=1, padx=1, sticky = "nsew")
button_9 = Button(root, text="9", padx=10, pady=15, font=("Arial", 15), bg= '#878787', command=lambda: displayframe.insert(END, 9)).grid(row=2, column=2, pady=1, padx=1, sticky = "nsew")

button_add = Button(root, text="+", padx=10, pady=15, font=("Arial", 15), bg= '#555555', command=button_addition).grid(row=5, column=3, pady=1, padx=1, sticky = "nsew")
button_sub = Button(root, text="-", padx=10, pady=15, font=("Arial", 15), bg= '#555555', command=button_subtract).grid(row=4, column=3, pady=1, padx=1, sticky = "nsew")
button_mul = Button(root, text="x", padx=10, pady=15, font=("Arial", 15), bg= '#555555',command=button_multiply).grid(row=3, column=3, pady=1, padx=1, sticky = "nsew")
button_div = Button(root, text="/", padx=10, pady=15, font=("Arial", 15), bg= '#555555',command=button_divide).grid(row=2, column=3, pady=1, padx=1, sticky = "nsew")
button_equal = Button(root, text="=", padx=10, pady=15, font=("Arial", 15), bg= '#ff8426', command=button_equalto).grid(row=5, column=0, pady=1, padx=1, sticky = "nsew")
button_clr = Button(root, text="Clr", padx=10, pady=15, font=("Arial", 15), bg= '#555555',command=button_clear).grid(row=5, column=2, pady=1, padx=1, sticky = "nsew")

root.mainloop()
