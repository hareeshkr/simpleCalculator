from tkinter import Tk,Entry,Label,Button,StringVar,END

root = Tk()

#space for screeen
screen = Entry(root, width="40")
screen.grid(row="0", column="0", columnspan="4")

number = ""
first_num = ""

#functions
def buttonClick(num):
    global number
    number = number + str(num)
    screen.delete(0, END)
    screen.insert(0, number)

def buttonFunc(maths):
    global math
    global number
    global first_num
    math = maths
    screen.delete(0, END)
    first_num = first_num + number
    number = ""

def buttonClear():
    screen.delete(0, END)

def buttonEqual():
    global math
    global first_num
    global number
    screen.delete(0, END)
    if (math == "+"):
        result = int(first_num) + int(number)
        screen.insert(0, str(result))
    elif (math == "-"):
        result = int(first_num) - int(number)
        screen.insert(0, str(result))
    elif (math == "*"):
        result = int(first_num) * int(number)
        screen.insert(0, str(result))
    elif (math == "/"):
        result = int(first_num) / int(number)
        screen.insert(0, str(result))
    result = ""
    first_num = ""
    number = ""
    
#buttons
Button(root, text="1",width="10", height="5", command=lambda: buttonClick(1)).grid(row="1",column="0")
Button(root, text="2",width="10", height="5", command=lambda: buttonClick(2)).grid(row="1",column="1")
Button(root, text="3",width="10", height="5", command=lambda: buttonClick(3)).grid(row="1",column="2")
Button(root, text="4",width="10", height="5", command=lambda: buttonClick(4)).grid(row="2",column="0")
Button(root, text="5",width="10", height="5", command=lambda: buttonClick(5)).grid(row="2",column="1")
Button(root, text="6",width="10", height="5", command=lambda: buttonClick(6)).grid(row="2",column="2")
Button(root, text="7",width="10", height="5", command=lambda: buttonClick(7)).grid(row="3",column="0")
Button(root, text="8",width="10", height="5", command=lambda: buttonClick(8)).grid(row="3",column="1")
Button(root, text="9",width="10", height="5", command=lambda: buttonClick(9)).grid(row="3",column="2")
Button(root, text="0",width="10", height="5", command=lambda: buttonClick(0)).grid(row="4",column="0")
Button(root, text="+",width="10", height="5", command=lambda: buttonFunc("+")).grid(row="1",column="3")
Button(root, text="-",width="10", height="5", command=lambda: buttonFunc("-")).grid(row="2",column="3")
Button(root, text="*",width="10", height="5", command=lambda: buttonFunc("*")).grid(row="3",column="3")
Button(root, text="Clear",width="10", height="5", command= buttonClear).grid(row="4",column="1")
Button(root, text="=",width="10", height="5", command= buttonEqual).grid(row="4",column="2")
Button(root, text="/",width="10", height="5", command=lambda: buttonFunc("/")).grid(row="4",column="3")

root.mainloop()

