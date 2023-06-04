#imports
from tkinter import *


# Adding functionality to GUI -------------------------

operand1 = operand2 = operator = None

def get_digit(digit):
    current_display = result_label['text']
    new_display = current_display + str(digit)
    result_label.config(
        text=new_display
    )

def get_operator(op):
    global operand1, operator
    operand1 = int(result_label['text'])
    operator = op
    result_label.config(
        text=''
    )

def get_result():
    global operand1,operand2,operator
    operand2 = int(result_label['text'])
    if operator == '+':
        result_label.config(
            text = str(operand1 + operand2)
        )
    elif operator == '-':
        result_label.config(
            text = str(operand1 - operand2)
        )
    elif operator == '*':
        result_label.config(
            text = str(operand1 * operand2)
        )
    elif operator == '/':
        if operand2 == 0:
            result_label.config(
                text=f"ERROR"
            )
        else:
            result_label.config(
                text = str(operand1 / operand2, 2)
            )

def clear():
    result_label.config(
        text=f''
    )


# Devloping GUI --------------------------------------

root = Tk()
root.title("CAL-C")
root.iconbitmap("calc.ico")
root.geometry('318x405+600+400')
root.resizable(0,0)
root.config(
    background='black'
)

# Result Display Label
result_label = Label(root, text=f'')
result_label.grid(
    row=0,
    column=0,
    columnspan=5,
    sticky='w',
    pady=(50,25)
)
result_label.config(
    bg = 'black',
    fg = 'white',
    font=('verdana',30)
)

#Button7
btn7 = Button(
    root, 
    text='7',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(7)
    )
btn7.grid(
    row=1,
    column=0
)

#Button8
btn8 = Button(
    root, 
    text='8',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(8)
    )
btn8.grid(
    row=1,
    column=1
)

#Button9
btn9 = Button(
    root, 
    text='9',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(9)
    )
btn9.grid(
    row=1,
    column=3
)

#ButtonADD
btn_add = Button(
    root, 
    text='+',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :get_operator('+')
    )
btn_add.grid(
    row=1,
    column=4
)

#Button4
btn4 = Button(
    root, 
    text='4',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(4)
    )
btn4.grid(
    row=2,
    column=0
)

#Button5
btn5 = Button(
    root, 
    text='5',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(5)
    )
btn5.grid(
    row=2,
    column=1
)

#Button6
btn6 = Button(
    root, 
    text='6',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(6)
    )
btn6.grid(
    row=2,
    column=3
)

#ButtonSUB
btn_sub = Button(
    root, 
    text='-',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :get_operator('-')
    )
btn_sub.grid(
    row=2,
    column=4
)

#Button1
btn1 = Button(
    root, 
    text='1',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(1)
    )
btn1.grid(
    row=3,
    column=0
)

#Button2
btn2 = Button(
    root, 
    text='2',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(2)
    )
btn2.grid(
    row=3,
    column=1
)

#Button3
btn3 = Button(
    root, 
    text='3',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(3)
    )
btn3.grid(
    row=3,
    column=3
)

#ButtonMUL
btn_mul = Button(
    root, 
    text='*',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :get_operator('*')
    )
btn_mul.grid(
    row=3,
    column=4
)

#ButtonCLR
btn_clr = Button(
    root, 
    text='CLR',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :clear()
    )
btn_clr.grid(
    row=4,
    column=0
)

#Button0
btn0 = Button(
    root, 
    text='0',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda : get_digit(0)
    )
btn0.grid(
    row=4,
    column=1
)

#ButtonEQUAL
btn_eql = Button(
    root, 
    text='=',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :get_result()
    )
btn_eql.grid(
    row=4,
    column=3
)

#ButtonDIV
btn_div = Button(
    root, 
    text='/',
    bg = '#00a65a',
    fg = 'white',
    width=5,
    height=2,
    font=('verdana', 15, 'bold'),
    command= lambda :get_operator('/')
    )
btn_div.grid(
    row=4,
    column=4
)

root.mainloop()