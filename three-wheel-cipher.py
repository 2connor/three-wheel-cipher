from tkinter import *
import string 

# creating basic window
window = Tk()
window.geometry("284x168") # size of the window width: 500, height: 375
window.resizable(0, 0) # window cannot be resized
window.title("Cipher")

## functions
# 'btn_click' function continuously updates the input field whenever you enters a number
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")
    output_text.set("")

def change(x, y, z, enorde):
    global new
    new = [] # stores each letter of the de/encrypted message
    i = 0
    e = 0
    a = listMessage
    for t in a:
        if z < len(alpha): z += 1
        elif y < len(alpha) and z > (len(alpha)-1): z = 0; y += 1
        elif x > (len(alpha) - 1): x = y = z = 0
        else: z = y = 0; x += 1
        # finds position of a[i] in alpha[e]
        # sets n to index of corrosponding equal value
        for e in range(len(alpha)):
            if a[i] == alpha[e]:
                n = e
        # encode
        if enorde == "e":
            try:
                new.append(alpha[n - y + 1 + z])
            except IndexError:
                new.append(alpha[(n - y + 1 + z) - len(alpha)])
        # decode
        else:
            try:
                new.append(alpha[n + y - 1 - z])
            except IndexError:
                new.append(alpha[(n + y - 1 - z) - len(alpha)])
        i += 1

def output():
    q = 0
    newStr = ''.join(str(q) for q in new)
    output_text.set(newStr)

# 'btn_encode' encodes the expression present in input field
def btn_encode():
    global expression, listMessage
    expression = ""
    enorde = "e"
    message = input_text.get()
    keyx = 0
    try:
        keyx = int(key1_text.get())
        keyy = int(key2_text.get())
        keyz = int(key3_text.get())
    except ValueError:
        print("ValueError")
    listMessage = list(message)
    change(keyx, keyy, keyz, enorde)
    output()

# 'btn_decode' decodes the expression present in input field
def btn_decode():
    #global expression
    #result = input_field.get()
    #output_text.set(result)
    #expression = ""
    global expression, listMessage
    expression = ""
    enorde = "d"
    message = input_text.get()
    keyx = 0
    try:
        keyx = int(key1_text.get())
        keyy = int(key2_text.get())
        keyz = int(key3_text.get())
    except ValueError:
        print("ValueError")
    listMessage = list(message)
    change(keyx, keyy, keyz, enorde)
    output()

expression = ""
# 'StringVar()' is used to get the instance of input field
input_text = StringVar()
output_text = StringVar()
key1_text = StringVar()
key2_text = StringVar()
key3_text = StringVar()

## graphical interface
# creating a frame for everything
frame = Frame(window, width = 312, height = 50, bg = "black", bd = 0, highlightbackground = "black",
              highlightcolor = "black", highlightthickness = 1)
frame.pack() #frame.pack(side = TOP)

# frame for output field
#output_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black",
#                     highlightcolor = "black", highlightthickness = 1)
#output_frame.pack(side = TOP)

# frame for buttons
#btns_frame = Frame(window, width = 30, height = 272.5, bg = "black")
#btns_frame.pack()

# creating a input field inside the 'Frame'
input_field = Entry(frame, font = ('arial', 16), textvariable = input_text, width = 20, bg = "#eee",
                    bd = 0, justify = LEFT) #show = "*"
input_field.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1, sticky = W+E)
#input_field.pack(ipady = 0) # 'ipady' is internal padding to increase the height of input field
input_field.insert(0, "text")

# output field inside 'frame'
output_field = Entry(frame, font = ('arial', 16), textvariable = output_text, width = 20,
                     bg = "#eee", bd = 0, justify = LEFT)
output_field.grid(row = 1, column = 0, columnspan = 3, padx = 1, pady = 1, sticky = W+E)
#output_field.pack(ipady = 0)
output_field.insert(0, "result")

# first key
key1 = Entry(frame, font = ('arial', 12), textvariable = key1_text, width = 10, bg = "#eee",
             bd = 0, justify = LEFT)
key1.grid(row = 2, column = 0, columnspan = 1, padx = 1, pady = 1, sticky = W)
key1.insert(0, "0")

# second key
key2 = Entry(frame, font = ('arial', 12), textvariable = key2_text, width = 10, bg = "#eee",
             bd = 0, justify = LEFT)
key2.grid(row = 2, column = 1, columnspan = 1, padx = 1, pady = 1, sticky = W)
key2.insert(0, "0")

# third key
key3 = Entry(frame, font = ('arial', 12), textvariable = key3_text, width = 10, bg = "#eee",
             bd = 0, justify = LEFT)
key3.grid(row = 2, column = 2, columnspan = 1, padx = 1, pady = 1, sticky = W)
key3.insert(0, "0")

# buttons, all inside 'frame'
clear = Button(frame, font = ('arial', 12), text = "clear", fg = "black", width = 30,
               bd = 0, bg = "#eee", cursor = "hand2",
               command = lambda: btn_clear()).grid(row = 3, column = 0, columnspan = 3,
                                                   padx = 1, pady = 1, sticky = W+E)
encode = Button(frame, font = ('arial', 12), text = "encode", fg = "black", width = 30,
                height = 1, bd = 0, bg = "#eee", cursor = "hand2",
                command = lambda: btn_encode()).grid(row = 4, column = 0, columnspan = 3,
                                                     padx = 1, pady = 0, sticky = W+E)
decode = Button(frame, font = ('arial', 12), text = "decode", fg = "black", width = 30,
                height = 1, bd = 0, bg = "#eee", cursor = "hand2",
                command = lambda: btn_decode()).grid(row = 5, column = 0, columnspan = 3,
                                                     padx = 1, pady = 1, sticky = W+E)

## top level
# 'alpha' is an array storing most available ascii characters
alpha = list(string.ascii_letters)
# appends numbers
#for i in range(len(string.digits)):
#    alpha.append(string.digits[i])
# appends punctuation
#for i in range(len(string.punctuation)):
#    a = string.punctuation[i]
#    if a != "(', ')" or "\\":
#        alpha.append(string.punctuation[i])
alpha.append(" ") # add "space" character

window.mainloop()

