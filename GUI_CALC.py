from tkinter import *
from turtle import bgcolor, right

root = Tk()
root.title("Calculator App")
root.geometry("375x332")

e = Entry(root, width=50, borderwidth=15)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)
    return
def add():
    global a5
    a5 = True
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
    a5 == True
def minus():
    global a2
    a2 = True
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
    a2 == True
def mult():
    global a3
    a3 = True
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
def div():
    global a4
    a4 = True
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
def equal():
    sec_num = e.get()
    e.delete(0, END)
    if a5 == True:
        e.insert(0, int(f_num) + int(sec_num))
    if a2 == True:
        e.insert(0, int(f_num) - int(sec_num))
    if a3 == True:
        e.insert(0, int(f_num) * int(sec_num))
    if a4 == True:
        e.insert(0, int(f_num) / int(sec_num))

#Define the Buttons
button1 = Button(root, text="1", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, fg='white', bg='#263652', command=lambda: button_click(0))
a1 = Button(root, text="C", padx=39, pady=20, fg='black', bg='#49618a', command= clear)
a2 = Button(root, text="-", padx=40, pady=20, fg='black', bg='#49618a', command= minus)
a3 = Button(root, text="X", padx=40, pady=20, fg='black', bg='#49618a', command= mult)
a4 = Button(root, text="%", padx=39, pady=20, fg='black', bg='#49618a', command= div)
a5 = Button(root, text="+", padx=39, pady=20, fg='black', bg='#49618a', command= add)
a6 = Button(root, text="=", padx=39, pady=20, fg='black', bg='#49618a', command= equal)

#Put the Buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
a1.grid(row=4,column=2, columnspan=1)
a2.grid(row=2,column=3, columnspan=1)
a3.grid(row=3,column=3, columnspan=1)
a4.grid(row=4,column=3, columnspan=1)
a5.grid(row=1,column=3, rowspan=1)
a6.grid(row=4,column=1, columnspan=1)

root.mainloop()