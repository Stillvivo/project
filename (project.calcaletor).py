from tkinter import *
import tkinter.messagebox

# ============================= setting ====================

root = Tk()
root.title("CALCULATOR")
root.geometry("400x200")
root.resizable(width=False, height=False)
color = "gray"
root.configure(bg=color)

# ============================= variables ====================
num1 = StringVar()
num2 = StringVar()
res_Value = StringVar()

# ============================= Frames ====================

top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)


top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)

# ============================= Functions ====================

def errorMsg():
    if errorMsg == "error":
        tkinter.messagebox.showerror("Error","Something went wrong")
    elif errorMsg == "division zero error":
        tkinter.messagebox.showerror("division zero error"
                                     ,"can not divide by zero")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_Value.set(value)
    except:
        errorMsg("error")


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_Value.set(value)
    except:
        errorMsg("error")


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_Value.set(value)
    except:
        errorMsg("error")

def div():
    if num2.get() == "0":
        errorMsg()
    elif num2.get() != "0":
        try:
            value = float(num1.get()) / float(num2.get())
            res_Value.set(value)
        except:
            errorMsg("error")


# ============================= Buttons ====================

btn_plus = Button(top_third,text="+",width=5,highlightbackground=color
                  ,command=lambda: plus())
btn_plus.pack(side=LEFT,padx=5,pady=5)

btn_minus = Button(top_third,text="-",width=5,highlightbackground=color
                   ,command=lambda: minus())
btn_minus.pack(side=LEFT,padx=5,pady=5)

btn_mul = Button(top_third,text="x",width=5,highlightbackground=color
                 ,command=lambda: mul())
btn_mul.pack(side=LEFT,padx=5,pady=5)

btn_divide = Button(top_third,text="%",width=5,highlightbackground=color
                    ,command=lambda : div())
btn_divide.pack(side=LEFT,padx=5,pady=5)

# ============================= Entries and Labels ====================

label_firt_num = Label(top_first,text="Input Number 1: ",bg=color)
label_firt_num.pack(side=LEFT,padx=10,pady=10)

first_num = Entry(top_first,highlightbackground=color,textvariable=num1)
first_num.pack(side=LEFT)

label_second_num = Label(top_second,text="Input Number 2: ",bg=color)
label_second_num.pack(side=LEFT,padx=10,pady=10)

second_num = Entry(top_second,highlightbackground=color,textvariable=num2)
second_num.pack(side=LEFT)

res = Label(top_forth,text="Result:",bg=color)
res.pack(side=LEFT,padx=10,pady=10)

res_num = Entry(top_forth,highlightbackground=color,textvariable=res_Value)
res_num.pack(side=LEFT)

root.mainloop()
