#Simple Calculator using Python(GUI)
from tkinter import *
from tkinter import messagebox
import math
#root = Tk()
root_calculator = Tk()
label_expression = Label(root_calculator, text="Enter Expression:")
label_expression.grid(row=0, sticky=W)

entry_cal = Entry(root_calculator, bd=3)
entry_cal.grid(row=0, column=1, columnspan=2, ipadx=30, ipady=10)

def backspace():
        entry_cal.delete(entry_cal.index(INSERT) - 1)

btn_backspace = Button(root_calculator, text="<--",  bg="tomato", width=15, height=2, relief="groove", command=backspace)
btn_backspace.grid(row=4, column=4)
label_answer = Label(root_calculator, text="Answer: ")
label_answer.grid(row=3, column=0, sticky=W)
label_space_cal=Label(root_calculator, text=" ",  width=17, height=2, relief="groove")
label_space_cal.grid(row=3, column=1, columnspan=2, ipadx=30)

def reset_cal():
        entry_cal.delete(0, END)
        entry_cal.insert(0, "")
        label_space_cal: Label = Label(root_calculator, text="                                         ")
        label_space_cal.grid(row=3, column=1, columnspan=2)
def bracket_start():
        entry_cal.insert(entry_cal.index(INSERT), "(")

def bracket_end():
        entry_cal.insert(entry_cal.index(INSERT), ")")

def entry_divide():
        entry_cal.insert(entry_cal.index(INSERT), "/")
btn_reset = Button(root_calculator, text="CLEAR", width=15, height=2, bg="#F24B4B", command=reset_cal)
btn_reset.grid(row=4)

btn_bracket_start = Button(root_calculator, text="(", width=15, height=2, bg="cyan", command=bracket_start)
btn_bracket_start.grid(row=4, column=1)

btn_bracket_end = Button(root_calculator, text=")", width=15, height=2, bg="cyan", command=bracket_end)
btn_bracket_end.grid(row=4, column=2)

btn_divide = Button(root_calculator, text="/", width=15, height=2, bg="pink", command=entry_divide)
btn_divide.grid(row=4, column=3)
def entry_7():
        entry_cal.insert(entry_cal.index(INSERT), "7")

def entry_8():
        entry_cal.insert(entry_cal.index(INSERT), "8")

def entry_9():
        entry_cal.insert(entry_cal.index(INSERT), "9")

def entry_multiply():
        entry_cal.insert(entry_cal.index(INSERT), "*")

btn_7 = Button(root_calculator, text="7",  width=15, height=2, bg="white", command=entry_7)
btn_7.grid(row=5)

btn_8 = Button(root_calculator, text="8",  width=15, height=2, bg="white", command=entry_8)
btn_8.grid(row=5, column=1)

btn_9 = Button(root_calculator, text="9",  width=15, height=2, bg="white", command=entry_9)
btn_9.grid(row=5, column=2)

btn_multiply = Button(root_calculator, text="*",  width=15, height=2, bg="pink", command=entry_multiply)
btn_multiply.grid(row=5, column=3)
def entry_4():
        entry_cal.insert(entry_cal.index(INSERT), "4")

def entry_5():
        entry_cal.insert(entry_cal.index(INSERT), "5")

def entry_6():
        entry_cal.insert(entry_cal.index(INSERT), "6")

def entry_minus():
        entry_cal.insert(entry_cal.index(INSERT), "-")

btn_4 = Button(root_calculator, text="4",  width=15, height=2, bg="white", command=entry_4)
btn_4.grid(row=6)

btn_5 = Button(root_calculator, text="5",  width=15, height=2, bg="white", command=entry_5)
btn_5.grid(row=6, column=1)

btn_6 = Button(root_calculator, text="6",  width=15, height=2, bg="white", command=entry_6)
btn_6.grid(row=6, column=2)

btn_minus = Button(root_calculator, text="-",  width=15, height=2, bg="pink", command=entry_minus)
btn_minus.grid(row=6, column=3)

def entry_1():
        entry_cal.insert(entry_cal.index(INSERT), "1")

def entry_2():
        entry_cal.insert(entry_cal.index(INSERT), "2")

def entry_3():
        entry_cal.insert(entry_cal.index(INSERT), "3")

def entry_plus():
        entry_cal.insert(entry_cal.index(INSERT), "+")

btn_1 = Button(root_calculator, text="1",  width=15, bg="white", height=2, command=entry_1)
btn_1.grid(row=7)

btn_2 = Button(root_calculator, text="2",  width=15, bg="white", height=2, command=entry_2)
btn_2.grid(row=7, column=1)

btn_3 = Button(root_calculator, text="3",  width=15, height=2, bg="white", command=entry_3)
btn_3.grid(row=7, column=2)

btn_plus = Button(root_calculator, text="+",  width=15, height=2, bg="pink", command=entry_plus)
btn_plus.grid(row=7, column=3)

def entry_0():
        entry_cal.insert(entry_cal.index(INSERT), "0")

def entry_decimal():
        entry_cal.insert(entry_cal.index(INSERT), ".")

def result():
        try:
            if entry_cal.get()== "":
                messagebox.showinfo("INVALID", "Please enter expression")
            else:
                res = eval(str(entry_cal.get()))
                label_result = Label(root_calculator, text=res)
                label_result.grid(row=3, column=1, columnspan=2)
        except ZeroDivisionError:
            messagebox.showinfo("ERROR", "Can not divisible by zero")
        except SyntaxError:
            messagebox.showinfo("ERROR", "You have entered invalid syntax")
        except NameError:
            messagebox.showinfo("ERROR", "Only numbers are allowed")

btn_exit = Button(root_calculator, text="EXIT",  width=15, height=2, bg="red", command=root_calculator.destroy)
btn_exit.grid(row=8)

btn_0 = Button(root_calculator, text="0",  width=15, height=2, bg="white", command=entry_0)
btn_0.grid(row=8, column=1)

btn_decimal = Button(root_calculator, text=".",  width=15, height=2, bg="cyan", command=entry_decimal)
btn_decimal.grid(row=8, column=2)

btn_result = Button(root_calculator, text="=",  width=15, height=2, bg="#0BD72D", command=result)
btn_result.grid(row=8, column=3)

def pow1():
       
        entry_cal.insert(entry_cal.index(INSERT), "**")     
        
btn_exit = Button(root_calculator, text="POW",  width=15, height=2, bg="greenyellow", command=pow1)
btn_exit.grid(row=7, column=4)

def pi():
        result =  False
        current = math.pi
        entry_cal.insert(entry_cal.index(INSERT), current)
def pm():
        result =  True
        current = -(int(entry_cal.get()))
        '''label_result = Label(root_calculator, text=current)
        label_result.grid(row=0, column=1, columnspan=1)'''
        entry_cal.delete(0, END)
        entry_cal.insert(0, "")
        entry_cal.insert(entry_cal.index(INSERT), current)
def sqrt():
        result =  False
        current = math.sqrt(float(entry_cal.get()))
        label_result = Label(root_calculator, text=current)
        label_result.grid(row=3, column=1, columnspan=2)
btn_0 = Button(root_calculator, text="PI",  width=15, height=2, bg="greenyellow", command=pi)
btn_0.grid(row=5, column=4)

btn_decimal = Button(root_calculator, text="SQRT",  width=15, height=2, bg="greenyellow", command=sqrt)
btn_decimal.grid(row=6, column=4)

btn_result = Button(root_calculator, text=chr(177),  width=15, height=2, bg="cyan", command=pm)
btn_result.grid(row=8)
def mod():
        entry_cal.insert(entry_cal.index(INSERT), "%")
btn_result = Button(root_calculator, text="MOD",  width=15, height=2, bg="greenyellow", command=mod)
btn_result.grid(row=8, column=4)

root_calculator.title("CALCULATOR")
try:
    root_calculator.iconbitmap("calculator.ico")
except:
        pass
root_calculator.mainloop()


'''btn_calculator = Button(root, text="CALCULATOR", bd=5, width=15, bg="#2B00FF", relief="groove", command=calculator)
btn_calculator.grid(row=2, column=4)'''
root_calculator.mainloop()  
