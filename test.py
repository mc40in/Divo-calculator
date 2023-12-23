from tkinter import *

<> = Tk()
root = Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title("DYVO CALCULATOR")
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)