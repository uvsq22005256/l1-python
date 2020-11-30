from tkinter import *

def draw_line(evt):
    global points
    points.append([evt.x, evt.y])
    if len(points) == 2:
        if points[0][0] >= 250 and points[1][0] >= 250 or points[0][0] <= 250 and points[1][0] <= 250:
            my_color = "blue"
        else:
            my_color = "red"
        canvas.create_line(points[0][0], points[0][1], points[1][0], points[1][1], fill = my_color)
        points = []




points = []
root = Tk()
root.resizable(width = False, height = False)
canvas = Canvas(root, width = 500, height = 500, bg = "Black", highlightthickness = 0)
canvas.pack()
canvas.create_line(250,0,250,500, fill = "White")
canvas.bind("<Button-1>", draw_line)


root.mainloop()