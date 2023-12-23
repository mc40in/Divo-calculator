import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc['state']  = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0, value+digit)
    calc['state'] = tk.DISABLED

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-*/':
        value = value[:-1]
    elif '+' in value or '-' in value or'*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc['state'] = tk.NORMAL
    calc.delete(0,tk.END)
    calc.insert(0, value + operation)
    calc['state'] = tk.DISABLED

def add_point_button(decimal):
    value = calc.get()
    if value[-1] in ".":
        value = value[:-1]
    calc.insert(0, value + decimal)

def make_digit_button(digit):
    return tk.Button(text=digit, bd=2, font=("Arial", 20), command=lambda : add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bd=2, font=("Arial", 20),fg='red',
                     command=lambda : add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bd=2, font=("Arial", 20),fg='red',
                     command=calculate)

def make_clear_button(operation):
    return tk.Button(text=operation, bd=2, font=("Arial", 20),fg='red',
                     command=clear)

def make_point_button(decimal):
    return tk.Button(text=point, bd=2, font=("Arial", 20),fg='red',
                     command=lambda : add_point_button(decimal))

def calculate():
    value = calc.get()
    if value[-1] in "+-*/":
        value = value + value[:-1]
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Warning', 'Print only digit available')
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo('Warning', 'Сannot be divided by 0')
        calc.insert(0, eval(value))
    calc['state'] = tk.DISABLED

def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char == "\r":
        calculate()
    elif event.char == "\x1b":
        clear()
    elif event.char in ".":
        add_point_button(event.char)

win = tk.Tk()
photo = tk.PhotoImage(file="favik.png")
win.iconphoto(False, photo)
win.config(bg='#3F3E3E')
win.title('DIVO CALC')
win.geometry('240x320+20+50')
win.resizable()
win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 25), width=15)
calc.insert(0, '0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='we', padx=2)

make_digit_button('7').grid(row = 2, column = 0, sticky='wens', padx=2, pady=2)
make_digit_button('8').grid(row = 2, column = 1, sticky='wens', padx=2, pady=2)
make_digit_button('9').grid(row = 2, column = 2, sticky='wens', padx=2, pady=2)
make_digit_button('4').grid(row = 3, column = 0, sticky='wens', padx=2, pady=2)
make_digit_button('5').grid(row = 3, column = 1, sticky='wens', padx=2, pady=2)
make_digit_button('6').grid(row = 3, column = 2, sticky='wens', padx=2, pady=2)
make_digit_button('1').grid(row = 4, column = 0, sticky='wens', padx=2, pady=2)
make_digit_button('2').grid(row = 4, column = 1, sticky='wens', padx=2, pady=2)
make_digit_button('3').grid(row = 4, column = 2, sticky='wens', padx=2, pady=2)
make_digit_button('0').grid(row = 5, column = 0, columnspan = 2, sticky='wens', padx=2, pady=2)
make_digit_button('.').grid(row = 5, column = 2, sticky='wens', padx=2, pady=2)


make_operation_button('/').grid(row = 1, column = 1, sticky='wens', padx=2, pady=2)
make_operation_button('*').grid(row = 1, column = 2, sticky='wens', padx=2, pady=2)
make_operation_button('-').grid(row = 1, column = 3, sticky='wens', padx=2, pady=2)
make_operation_button('+').grid(row = 2, column = 3, rowspan = 2, sticky='wens', padx=2, pady=2)

make_calc_button('=').grid(row = 4, column = 3, rowspan = 2, sticky='wens', padx=2, pady=2)
make_clear_button('C').grid(row = 1, column = 0, sticky='wens', padx=2, pady=2)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()