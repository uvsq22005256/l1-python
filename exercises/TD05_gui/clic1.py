from tkinter import *

def draw_pixel(i, j, color):
    """fonction qui colorie le pixel (i, j) du canvas de la couleur color."""
    #canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1,fill = color)
    canvas.create_line(i, j, i + 1, j + 1, fill = color, tag = "pix")

def reaction(evt):
    draw_pixel(evt.x, evt.y, "red")


root = Tk()
root.resizable(width = False, height = False)
canvas = Canvas(root, width = 500, height = 500, bg = "Black", highlightthickness = 0)
canvas.pack()
canvas.bind("<Button-1>", reaction)


root.mainloop()