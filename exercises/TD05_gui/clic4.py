from tkinter import *

def onClick(evt):
    global clicks
    clicks += 1
    if clicks%2 != 0:
        canvas.itemconfig(carre, fill="red")
    else:
        canvas.itemconfig(carre, fill="")
        if clicks == 10:
            root.destroy()



clicks = 0
root = Tk()
root.resizable(width = False, height = False)
canvas = Canvas(root, width = 500, height = 500, bg = "Black", highlightthickness = 0)
canvas.pack()
carre = canvas.create_rectangle(200,200,300,300, fill = "", outline = "red")
canvas.bind("<Button-1>", onClick)


root.mainloop()