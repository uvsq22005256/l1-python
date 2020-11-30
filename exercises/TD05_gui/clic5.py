from tkinter import *

def cercle(evt):
    items.append(canvas.create_oval((evt.x-50, evt.y-50),(evt.x+50, evt.y+50), fill = "blue", tag = "cercle"))

def onClick(evt):
    global clicks
    clicks += 1

    if clicks <= 8:
            cercle(evt)
    elif clicks == 9:
        for i in items:
            canvas.itemconfig(i, fill="yellow")
    else:
        canvas.delete("cercle")
        clicks = 0
        


items = []
clicks = 0
root = Tk()
root.resizable(width = False, height = False)
canvas = Canvas(root, width = 500, height = 500, bg = "Black", highlightthickness = 0)
canvas.pack()
canvas.bind("<Button-1>", onClick)


root.mainloop()