from tkinter import *
screen = Tk()
screen.title('My Calcuator')
screen.geometry('365x500')
def click(number):
    global operator
    operator += str(number)
    text.set(operator)

def clear():
    global operator
    operator =''
    text.set(operator)

def equal():
    global operator
    result=eval(operator)
    operator=str(result)
    text.set(operator)

text = StringVar()
operator =''
entry1 = Entry(screen,font=('arial',20),bd='30',justify='right',textvariable = text)
entry1.grid(row=0,columnspan=5)

btn7 = Button(screen,text='7',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(7),
              activebackground='gray54',activeforeground='white')
btn7.grid(row=1,column=0)

btn8 = Button(screen,text='8',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(8),
              activebackground='gray54',activeforeground='white')
btn8.grid(row=1,column=1)

btn9 = Button(screen,text='9',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(9),
              activebackground='gray54', activeforeground='white')
btn9.grid(row=1,column=2)

btnadd = Button(screen,text='+',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click('+'),
                activebackground='gray54', activeforeground='white')
btnadd.grid(row=1,column=3)

btn4 = Button(screen,text='4',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(4),
              activebackground='gray54',activeforeground='white')
btn4.grid(row=2,column=0)

btn5 = Button(screen,text='5',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(5),
              activebackground='gray54',activeforeground='white')
btn5.grid(row=2,column=1)

btn6 = Button(screen,text='6',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(6),
              activebackground='gray54',activeforeground='white')
btn6.grid(row=2,column=2)

btnsub = Button(screen,text='-',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click('-'),
                activebackground='gray54',activeforeground='white')
btnsub.grid(row=2,column=3)

btn1 = Button(screen,text='1',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(1),
              activebackground='gray54',activeforeground='white')
btn1.grid(row=3,column=0)

btn2 = Button(screen,text='2',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(2),
              activebackground='gray54',activeforeground='white')
btn2.grid(row=3,column=1)

btn3 = Button(screen,text='3',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(3),
              activebackground='gray54',activeforeground='white')
btn3.grid(row=3,column=2)

btnmul = Button(screen,text='*',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click('*'),
                activebackground='gray54',activeforeground='white')
btnmul.grid(row=3,column=3)

btn0 = Button(screen,text='0',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click(0),
              activebackground='gray54',activeforeground='white')
btn0.grid(row=4,column=0)

btnclear = Button(screen,text='C',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = clear,
                  activebackground='gray54',activeforeground='white')
btnclear.grid(row=4,column=1)

btnequal = Button(screen,text='=',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = equal,
                  activebackground='gray54',activeforeground='white')
btnequal.grid(row=4,column=2)

btndiv = Button(screen,text='/',font=('arial',20,'bold'),bd='10',padx=18,pady=16,command = lambda:click('/'),
                activebackground='gray54',activeforeground='white')
btndiv.grid(row=4,column=3)

screen.mainloop()