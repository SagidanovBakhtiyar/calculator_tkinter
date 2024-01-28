from tkinter import *
from tkinter import ttk


class Calculator:
    def __init__(self) -> None:
        self.number = 0
        self.accumulator = 0
        self.decimal_entered = False

    def update_display(self):
        btnnumber.config(text=f"{self.number}")

    def decimal(self):
        if "." not in str(self.number):
            self.decimal_entered = True
            self.number = str(self.number) + "."
        self.update_display()

    def number_input(self, n):
        if len(str(self.number)) >= 17:
            return
        if self.decimal_entered:
            self.number = str(self.number) + str(n)
            self.number = float(self.number)
        else:
            self.number = self.number * 10 + n
        self.update_display()
    
    def delete(self, n):
        self.number = int(self.number / n)
        self.update_display()

    def clear(self):
        self.number = 0
        self.decimal_entered = False
        self.update_display()

    def operators(self, operation):
        self.accumulator = self.number
        self.operation = operation
        self.clear()
        if self.operation == "square":
            self.number = self.accumulator * self.accumulator
            self.accumulator = 0
            self.operation = None
            self.update_display()
        elif self.operation == "percent":
            self.number = self.accumulator / 100
            self.accumulator = 0
            self.operation = None
            self.update_display()
    

    def calculate(self):
        if self.operation == "plus":
            self.number = self.accumulator + self.number
        elif self.operation == "minus":
            self.number = self.accumulator - self.number
        elif self.operation == "multiply":
            self.number = self.accumulator * self.number
        try:
            if self.operation == "divide":
                self.number = self.accumulator / self.number
        except ZeroDivisionError:
            self.number = "Can't divide by zero"
        self.accumulator = 0
        self.operation = None
        self.update_display()


calculator = Calculator()

root = Tk()
root.title("Calculator")
icon = PhotoImage(file="calculator.png")
root.iconphoto(False, icon)
root.resizable(False, False)

# Font Style
style = ttk.Style()
style.configure("TButton", font=("arial", 15))

# Numbers button input
btn0 = ttk.Button(text="0", command=lambda: calculator.number_input(0))
btn1 = ttk.Button(text="1", command=lambda: calculator.number_input(1))
btn2 = ttk.Button(text="2", command=lambda: calculator.number_input(2))
btn3 = ttk.Button(text="3", command=lambda: calculator.number_input(3))
btn4 = ttk.Button(text="4", command=lambda: calculator.number_input(4))
btn5 = ttk.Button(text="5", command=lambda: calculator.number_input(5))
btn6 = ttk.Button(text="6", command=lambda: calculator.number_input(6))
btn7 = ttk.Button(text="7", command=lambda: calculator.number_input(7))
btn8 = ttk.Button(text="8", command=lambda: calculator.number_input(8))
btn9 = ttk.Button(text="9", command=lambda: calculator.number_input(9))

# Number packing to grid
btn0.grid(row=4, column=2, ipadx=5, ipady=30, sticky=NSEW)
btn1.grid(row=3, column=1, ipadx=5, ipady=30, sticky=NSEW)
btn2.grid(row=3, column=2, ipadx=5, ipady=30, sticky=NSEW)
btn3.grid(row=3, column=3, ipadx=5, ipady=30, sticky=NSEW)
btn4.grid(row=2, column=1, ipadx=5, ipady=30, sticky=NSEW)
btn5.grid(row=2, column=2, ipadx=5, ipady=30, sticky=NSEW)
btn6.grid(row=2, column=3, ipadx=5, ipady=30, sticky=NSEW)
btn7.grid(row=1, column=1, ipadx=5, ipady=30, sticky=NSEW)
btn8.grid(row=1, column=2, ipadx=5, ipady=30, sticky=NSEW)
btn9.grid(row=1, column=3, ipadx=5, ipady=30, sticky=NSEW)

# Keyboard input
root.bind("<Key-0>", lambda event: calculator.number_input(0))
root.bind("<Key-1>", lambda event: calculator.number_input(1))
root.bind("<Key-2>", lambda event: calculator.number_input(2))
root.bind("<Key-3>", lambda event: calculator.number_input(3))
root.bind("<Key-4>", lambda event: calculator.number_input(4))
root.bind("<Key-5>", lambda event: calculator.number_input(5))
root.bind("<Key-6>", lambda event: calculator.number_input(6))
root.bind("<Key-7>", lambda event: calculator.number_input(7))
root.bind("<Key-8>", lambda event: calculator.number_input(8))
root.bind("<Key-9>", lambda event: calculator.number_input(9))

# Numpad input
root.bind("<KP_0>", lambda event: calculator.number_input(0))
root.bind("<KP_1>", lambda event: calculator.number_input(1))
root.bind("<KP_2>", lambda event: calculator.number_input(2))
root.bind("<KP_3>", lambda event: calculator.number_input(3))
root.bind("<KP_4>", lambda event: calculator.number_input(4))
root.bind("<KP_5>", lambda event: calculator.number_input(5))
root.bind("<KP_6>", lambda event: calculator.number_input(6))
root.bind("<KP_7>", lambda event: calculator.number_input(7))
root.bind("<KP_8>", lambda event: calculator.number_input(8))
root.bind("<KP_9>", lambda event: calculator.number_input(9))

# Operators button input
btnclear = ttk.Button(text="C", command=calculator.clear)
btnresult = ttk.Button(text="=", command=lambda: calculator.calculate())
btnplus = ttk.Button(text="+", command=lambda: calculator.operators("plus"))
btnminus = ttk.Button(text="-", command=lambda: calculator.operators("minus"))
btnmultiply = ttk.Button(text="×", command=lambda: calculator.operators("multiply"))
btndivide = ttk.Button(text="÷", command=lambda: calculator.operators("divide"))
btnsquare = ttk.Button(text="x²", command=lambda: calculator.operators("square"))
btndelete = ttk.Button(text="Delete", command=lambda: calculator.delete(10))
btncomma = ttk.Button(text=",", command=lambda: calculator.decimal())
btnpercent = ttk.Button(text="%", command=lambda: calculator.operators("percent"))

# Operators packing to grid
btnclear.grid(row=4, column=1, ipadx=5, ipady=20, sticky=NSEW)
btnresult.grid(row=4, column=3, ipadx=5, ipady=20, sticky=NSEW)
btnplus.grid(row=4, column=4, ipadx=5, ipady=20, sticky=NSEW)
btnminus.grid(row=3, column=4, ipadx=5, ipady=20, sticky=NSEW)
btnmultiply.grid(row=2, column=4, ipadx=5, ipady=20, sticky=NSEW)
btndivide.grid(row=1, column=4, ipadx=5, ipady=20, sticky=NSEW)
btnsquare.grid(row=5, column=4, ipadx=5, ipady=20, sticky=NSEW)
btndelete.grid(row=5, column=1, ipadx=5, ipady=20, sticky=NSEW)
btncomma.grid(row=5, column=3, ipadx=5, ipady=20, sticky=NSEW)
btnpercent.grid(row=5, column=2, ipadx=5, ipady=20, sticky=NSEW)

# Operators Keyboard Input
root.bind("<Return>", lambda event: calculator.calculate())
root.bind("<plus>", lambda event: calculator.operators("plus"))
root.bind("<minus>", lambda event: calculator.operators("minus"))
root.bind("<asterisk>", lambda event: calculator.operators("multiply"))
root.bind("<slash>", lambda event: calculator.operators("divide"))
root.bind("<BackSpace>", lambda event: calculator.delete(10))
root.bind("<Delete>", lambda event: calculator.clear())
root.bind("<period>", lambda event: calculator.decimal())
root.bind("<percent>", lambda event: calculator.operators("percent"))

# Operators Numpad Input
root.bind("<KP_Enter>", lambda event: calculator.calculate())
root.bind("<KP_Add>", lambda event: calculator.operators("plus"))
root.bind("<KP_Subtract>", lambda event: calculator.operators("minus"))
root.bind("<KP_Multiply>", lambda event: calculator.operators("multiply"))
root.bind("<KP_Divide>", lambda event: calculator.operators("divide"))


# Number table
btnnumber = Label(
    root, text=f"{calculator.number}", font=("arial", 40), anchor=E, width=5, height=1
)
btnnumber.grid(row=0, ipadx=150, ipady=30, columnspan=5, sticky=NSEW, padx=20)


root.mainloop()