from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)
    return
def add():
    first_num = e.get()
    global f_num
    f_num = int(first_num)
    e.delete(0, END)
def equal():
    sec_num = e.get()
    e.delete(0, END)
    e.insert(0, int(sec_num) + int(f_num))

#Define the Buttons
button1 = Button(root, text="1", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(9))
button0 = Button(root, text="0", padx=40, pady=20, fg='black', bg='yellow', command=lambda: button_click(0))
a1 = Button(root, text="C", padx=40, pady=50, fg='black', bg='yellow', command= clear)
a5 = Button(root, text="+", padx=40, pady=50, fg='black', bg='yellow', command= add)
a6 = Button(root, text="=", padx=85, pady=20, fg='black', bg='yellow', command= equal)

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
a1.grid(row=1,column=3, rowspan=2)
a5.grid(row=3,column=3, rowspan=2)
a6.grid(row=4,column=1, columnspan=2)

root.mainloop()