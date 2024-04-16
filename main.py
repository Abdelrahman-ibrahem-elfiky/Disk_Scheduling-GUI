from tkinter import *
import turtle
import pandas as pd
import numpy as np
from copy import copy
#------------------------------------------------------------------------------
def FCFS(Request, Start):
    Sum = 0
    position = Start
    Order = []
    Order.append(Start)
    for i in Request:
        Sum += abs(i-position)
        position = i
        Order.append(i)
    return Order, Sum
#------------------------------------------------------------------------------
def SSTF(Request,Start):
    templist = copy(Request)
    position = Start
    highest = max(templist)
    mindiff=abs(Start-highest)
    j=highest
    templist.sort()
    Order = []
    Order.append(Start)
    Sum = 0
    while len(templist) > 0:
        for i in templist:
                diff= abs(position-i)
                if diff<mindiff:
                    mindiff=diff
                    j=i
        Sum+= abs(position-j)
        position = j
        templist.remove(j)
        Order.append(j)
        mindiff=abs(position-highest)
        j=highest
    return Order, Sum
#------------------------------------------------------------------------------
def SCAN_Inword(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if  Start > Request_tmp[0]:
        Request_tmp.append (199)
    p = len(Request_tmp)

    k = Start + 1
    Order.append(Start)
    while k < 200:
        for l in range(0, p):
            if (Request_tmp[l] == k):
                Order.append(k)
        k += 1


    i = Start - 1
    while i >= 0:
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i -= 1


    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#----------------------------------------------------
def SCAN_Outword(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1



    k = Start + 1
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def CSCAN_Outword(Request, Start):
    n = len(Request)
    Order = []
    Request_tmp=copy(Request)
    Request_tmp.sort()
    if Start != 0 and Start < Request_tmp[n-1]:
        Request_tmp.append (0)
    p = len(Request_tmp)

    i = Start - 1
    Order.append(Start)
    while i >= 0:
        for j in range(0,p):
            if(Request_tmp[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        if(k == 199):
            Order.append(k)
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    for p in range(0,len(Order)-1):
         Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def CSCAN_Inword(Request, Start):
    n = len(Request)
    Order = []
    Request_in = copy(Request)
    Request_in.sort()
    if Start >Request_in[0]:
        Request_in.append(199)
    h=len(Request_in)

    k = Start + 1
    Order.append(Start)
    while k < 200:
        for l in range(0, h):
            if (Request_in[l] == k):
                Order.append(k)
        k += 1

    i = 0
    while i < Start:
        if(i==0):
            Order.append(i)
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i += 1


    Sum = 0
    for p in range(0,len(Order)-1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def LOOK_Outword(Request, Start):
    n = len(Request)
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i -= 1

    k = Start + 1
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def LOOK_Inword(Request, Start):
    n = len(Request)
    Order = []

    k = Start + 1
    Order.append(Start)
    while k < 200:
        for l in range(0, n):
            if (Request[l] == k):
                Order.append(k)
        k += 1


    i = Start - 1
    while i > 0:
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i -= 1


    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def CLOOK_Outword(Request, Start):
    n = len(Request)
    Order = []
    i = Start - 1
    Order.append(Start)
    while i > 0:
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i -= 1

    k = 199
    while k > Start:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k -= 1

    Sum = 0
    for p in range(0,len(Order) - 1):
        Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def CLOOK_Inword(Request, Start):
    n = len(Request)
    Order = []

    k = Start+1
    Order.append(Start)
    while k < 200:
        for l in range(0,n):
            if(Request[l] == k):
                Order.append(k)
        k += 1


    i = 0
    while i < Start:
        for j in range(0,n):
            if(Request[j] == i):
                Order.append(i)
        i += 1


    Sum = 0
    for p in range(0,len(Order) - 1):
         Sum += abs(Order[p] - Order[p+1])
    return Order, Sum
#------------------------------------------------------------------------------
def Visualise(option, request_arr, start,direction):
    request=list(request_arr.split(" "))
    request=[int(i) for i in request]
    if option == "FCFS":                        #
        Order, Sum = FCFS(request, start)
    elif option =="SSTF":
        Order, Sum = SSTF(request, start)
    elif option =="SCAN":
        if direction == "Inword":
            Order, Sum = SCAN_Inword(request, start)
        else:
            Order, Sum = SCAN_Outword(request, start)
    elif option =="CSCAN":
        if direction == "Inword":
            Order, Sum = CSCAN_Inword(request, start)
        else:
            Order, Sum = CSCAN_Outword(request, start)
    elif option =="LOOK":
        if direction == "Inword":
            Order, Sum = LOOK_Inword(request, start)
        else:
            Order, Sum = LOOK_Outword(request, start)
    elif option =="CLOOK":
        if direction == "Inword":
            Order, Sum = CLOOK_Inword(request, start)
        else:
            Order, Sum = CLOOK_Outword(request, start)

    turtle.clearscreen()
    Disk = turtle.Screen()
    Disk.title(option)
    Disk.bgcolor("white")
    Disk.setworldcoordinates(-5, -20, 210, 10)
    head = turtle.Turtle()
    head.shape("square")
    head.color("blue")
    head.turtlesize(.3, .3, 1)
    head.speed(1)
    head.pensize(0)

    head2 = turtle.Turtle()
    head2.shape("circle")
    head2.color("orange")
    head2.turtlesize(.3, .3, 1)
    head2.speed(4)
    head2.pensize(0)

    n = len(Order)
    y = -1
    y2=0

    temp_order=[int(i*10) for i in range(0,21)]
    for i in range(0,len(temp_order)):
        head2.goto(temp_order[i], y2)
        head2.stamp()
        head2.write(temp_order[i], False, align="right")


    for i in range(0, n):
        if i == 0:
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right")
        else:
            head.goto(Order[i], y-1)
            head.stamp()
            head.write(Order[i], False, align="right")
            y -= 1
    head.hideturtle()
    head.speed(0)
    head.penup()
    head.goto(100, 5)


    message1 = "Disk Scheduling Algorithm: " + option +" "+ direction
    message2 = "Total Head Movement: " + str(Sum)
    start = "\033[1m"
    end = "\033[0;0m"
    head.write(message1, False, align="center",font=("Century Gothic", 14) )
    head.goto(100,4)
    head.write(message2, False, align="center",font=("Century Gothic", 14))
    head.goto(100,3)
    head.pendown
    Disk.exitonclick()
#------------------------------------------------------------------------------
def Main():

    #List of colours
    mainbg="white"
    HeaderBG="orange"
    TextCol="blue"
    eleBG="#f0f0f0"
    #List of Messages
    algo="Choose Algorithm:"
    vals="Enter your values:"
    current="Current position of R/W head:"
    direction="Choose direction for use:"

    Menu = Tk()
    Menu.title("Adv_OS PROJECT")
    Menu.overrideredirect(False)
    Menu.geometry("811x700+0+0")
    Menu.resizable(False, False)
    Menu.configure(bg='white')
    user_inp=Text(Menu,font=("Century Gothic", 16),width=20,height=1,bg=eleBG,fg=TextCol,bd=0)
    user_inp.grid(row=7, column=0)
    user_inp.config(highlightbackground = "Red",highlightcolor="Red")
    title=Label(Menu, text="   Disk Scheduling    ",anchor=CENTER, bd=12,padx=200, bg="blue", fg=mainbg, font=("Century Gothic",30), pady=2).grid(row=0)



    # List of options in dropdown menu
    optionlist = ('FCFS', 'SSTF', 'SCAN','LOOK', 'CSCAN','CLOOK')
    Option = StringVar()
    direction_option=('Inword','Outword')
    Direction=StringVar()
    Start = IntVar()
    Option.set("FCFS")
    Direction.set("Outword")
    L1 = Label(Menu, text = algo,font=("Century Gothic", 16),bg=mainbg,fg=HeaderBG,pady=30)
    L1.grid(row=2,column=0)
    OM = OptionMenu(Menu, Option, *optionlist)
    OM.grid(row=3, column=0)
    OM.configure(bd = 0,bg=eleBG,fg=TextCol,highlightthickness = 0,padx=12,pady=12,font=("Century Gothic", 12))
    L2 = Label(Menu, text = current,font=("Century Gothic", 16),bg=mainbg,fg=HeaderBG,pady=30)
    L2.grid(row=12, column=0)
    E1 = Entry(Menu, textvariable = Start, bd = 0,fg=TextCol, width = 8,bg=eleBG,justify=CENTER,font=("Century Gothic", 16))
    E1.grid(row=13, column=0,)
    L1 = Label(Menu, text = "",font=("Century Gothic", 16),bg=mainbg,fg=mainbg,pady=5)
    L1.grid(row=14,column=0)


    L1 = Label(Menu, text = "",font=("Century Gothic", 16),bg=mainbg,fg=mainbg,pady=5)
    L1.grid(row=16,column=0)
    L1 = Label(Menu, text = vals,font=("Century Gothic", 16),bg="white",fg=HeaderBG,pady=30)
    L1.grid(row=5,column=0)


    L3 = Label(Menu, text=direction, font=("Century Gothic", 16), bg=mainbg, fg=HeaderBG, pady=30)
    L3.grid(row=16, column=0)
    DO = OptionMenu(Menu, Direction, *direction_option)
    DO.grid(row=18, column=0)
    DO.configure(bd = 0,bg=eleBG,fg=TextCol,highlightthickness = 0,padx=12,pady=12,font=("Century Gothic", 12))

    B2 = Button(Menu, borderwidth=0, padx=20, pady=10, bg=eleBG, fg=TextCol, text="Visualise", \
    command=lambda: Visualise(Option.get(), user_inp.get(1.0, END), Start.get(),Direction.get()),font=("Century Gothic", 12))
    B2.grid(row=15, column=0)
    Menu.mainloop()
Main()

