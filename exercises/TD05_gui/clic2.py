from tkinter import *

def cercle(evt):
    if evt.x > 250:
        my_color = "red"
    else:
        my_color = "blue"
    canvas.create_oval((evt.x-50, evt.y-50),(evt.x+50, evt.y+50), fill = my_color)



root = Tk()
root.resizable(width = False, height = False)
canvas = Canvas(root, width = 500, height = 500, bg = "Black", highlightthickness = 0)
canvas.pack()
canvas.create_line(250,0,250,500, fill = "White")
canvas.bind("<Button-1>", cercle)


root.mainloop()