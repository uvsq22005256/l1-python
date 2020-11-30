from tkinter import *
import random

def random_coords():
    x = random.randint(0,400)
    y = random.randint(0,400)
    return x, y

def cercle():
    global objets
    x, y = random_coords()
    objets.append(canvas.create_oval((x, y),(x+100, y+100), fill = my_color))

def carre():
    global objets
    x, y = random_coords()
    objets.append(canvas.create_rectangle((x, y),(x+100, y+100), fill = my_color))

def croix():
    global objets
    x, y = random_coords()
    objets.extend((canvas.create_line((x, y),(x+100, y+100), fill = my_color), canvas.create_line((x+100, y),(x, y+100), fill = my_color)))

def set_color():
    global my_color
    my_color = input("Quel doit-être la nouvelle couleur?\n")

def undo():
    global objets
    if len(objets) != 0:
        if canvas.type(objets[-1]) == "line":
            canvas.delete(objets[-1])
            objets.pop(-1)
            canvas.delete(objets[-1])
            objets.pop(-1)
        else:
            canvas.delete(objets[-1])
            objets.pop(-1)


my_color = "Blue"
objets = []
root = Tk()
root.title("Mon dessin")

canvas = Canvas(root, width = 500, height = 500, bg = "black", bd = 10, relief = "raised")

bouton_color = Button(root, text="Choisir une couleur", fg = "blue", command = set_color, bd = 5)
bouton_cercle = Button(root, text="Cercle", command = cercle, bd = 5)
bouton_carre = Button(root, text="Carre", command = carre, bd = 5)
bouton_croix = Button(root, text="Croix", command = croix, bd = 5)
bouton_undo = Button(root, text="Undo", command = undo, bd = 5, font = ("Arial", 16, "bold"))


bouton_color.grid(row = 0, column = 1)
bouton_cercle.grid(row = 1, column = 0)
bouton_carre.grid(row = 2, column = 0)
bouton_croix.grid(row = 3, column = 0)
bouton_undo.grid(row = 0, column = 2)
canvas.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)

root.mainloop()