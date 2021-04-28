from tkinter import *
root = Tk()
root.title('calculator')
root.resizable(False, False)

displayValue = StringVar()
displayValue.set("0")
displayValue1 = StringVar()

display = Entry(root, width=10, textvariable=displayValue, font='Consolas 15 bold', justify='right', relief='flat',
                readonlybackground='grey', selectbackground='grey', borderwidth=15, state='readonly')
display.grid(row=1, column=0, columnspan=5, sticky=N+E+W+S, padx=3, pady=0)
display1 = Entry(root, width=10, textvariable=displayValue1, font="Consolas 15 bold", justify="right", relief="flat",
                 readonlybackground="grey", selectbackground="grey", borderwidth=5, state='readonly')
display1.grid(row=0, column=0, columnspan=5, sticky=N+E+W+S, padx=3, pady=0)

def btn_click(number):
    if displayValue.get() == "0":
        displayValue.set((displayValue.get() + number)[1:])
    else:
        if displayValue1.get().count("="):
            displayValue.set("")
        displayValue.set(displayValue.get() + number)
        displayValue1.set(displayValue.get())

def addN(sign):
    displayValue1.set(displayValue.get() + sign)
    displayValue.set(displayValue.get() + sign)
def subN(sign):
    displayValue.set(displayValue.get() + sign)
def mulN(sign):
    displayValue.set(displayValue.get() + sign)
def divN(sign):
    displayValue.set(displayValue.get() + sign)
def dot(sign):
    displayValue.set(displayValue.get() + sign)

def result(sign):
    try:
        displayValue1.set(displayValue1.get() + sign)
        displayValue.set(eval(displayValue.get()))
    except ZeroDivisionError:
        displayValue.set("0으로 나눌 수 없습니다.")
    except SyntaxError:
        displayValue.set("잘못된 계산식입니다.")
def c():
    displayValue.set('0')
    displayValue1.set('')
def back():
    displayValue.set(displayValue.get()[:-1])
    displayValue1.set(displayValue1.get()[:-1])
    print(len(displayValue.get()))
def change():
    displayValue.set(eval(displayValue.get() + '* -1'))

btn_7 = Button(root, font='Consolas', text=7, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click('7'))
btn_8 = Button(root, font='Consolas', text=8, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("8"))
btn_9 = Button(root, font='Consolas', text=9, width=5, height=2,
               relief='flat', bg='ghostwhite', activebackground='grey', command=lambda: btn_click("9"))

btn_7.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)

btn_4 = Button(root, font='Consolas', text=4, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("4"))
btn_5 = Button(root, font='Consolas', text=5, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("5"))
btn_6 = Button(root, font='Consolas', text=6, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("6"))

btn_4.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)

btn_1 = Button(root, font='Consolas', text=1, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("1"))
btn_2 = Button(root, font='Consolas', text=2, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("2"))
btn_3 = Button(root, font='Consolas', text=3, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("3"))

btn_1.grid(row=5, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=5, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

btn_change = Button(root, font='Consolas', text='+/-', width=5, height=2, relief='flat',
                    bg='ghostwhite', activebackground='grey', command=change)
btn_0 = Button(root, font='Consolas', text=0, width=5, height=2, relief='flat',
               bg='ghostwhite', activebackground='grey', command=lambda: btn_click("0"))
btn_dot = Button(root, font='Consolas', text='.', width=5, height=2, relief='flat',
                 bg='ghostwhite', activebackground='grey', command=lambda: dot("."))

btn_change.grid(row=6, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_0.grid(row=6, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_dot.grid(row=6, column=2, sticky=N+E+W+S, padx=3, pady=3)

btn_add = Button(root, font='Consolas', text='+', width=5, height=2, relief='flat',
                 bg='#E6E6E6', activebackground='grey', command=lambda : addN("+"))
btn_sub = Button(root, font='Consolas', text='-', width=5, height=2, relief='flat',
                 bg='#E6E6E6', activebackground='grey', command=lambda: subN("-"))
btn_mul = Button(root, font='Consolas', text='x', width=5, height=2, relief='flat',
                 bg='#E6E6E6', activebackground='grey', command=lambda: mulN("*"))
btn_div = Button(root, font='Consolas', text='÷', width=5, height=2, relief='flat',
                 bg='#E6E6E6', activebackground='grey', command=lambda: divN("/"))

btn_add.grid(row=5, column=3, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=4, column=3, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

btn_percent = Button(root, font='Consolas', text='%', width=5, height=2, relief='flat',
                     bg='#E6E6E6', activebackground='grey', command=lambda: btn_click("%"))
btn_c = Button(root, font='Consolas', text='c', width=5, height=2, relief='flat',
               bg='#E6E6E6', activebackground='grey', command=c)
btn_back = Button(root, font='Consolas', text='←', width=5, height=2, relief='flat',
                  bg='#E6E6E6', activebackground='grey', command=back)
btn_equal = Button(root, font='Consolas', text='=', width=5, height=2, relief='flat',
                   bg='skyblue', activebackground='grey', command=lambda: result("="))

btn_percent.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_c.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_back.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=6, column=3, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()

