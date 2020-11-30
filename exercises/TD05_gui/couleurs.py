from tkinter import *
from random import randint


def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def draw_pixel(i, j, color):
    """fonction qui colorie le pixel (i, j) du canvas de la couleur color."""
    #canvas.create_rectangle(i - 1, j - 1, i + 1, j + 1,fill = color)
    canvas.create_line(i, j, i + 1, j + 1, fill = color, tag = "pix")

def ecran_aleatoire():
    """fonction qui est appelée par le bouton aleatoire et qui remplit le canvas de manière à ce que chaque pixel soit d'une couleur choisie au hasard."""
    canvas.delete("pix")
    for i in range(1,257):
        for a in range(1,257):
            draw_pixel(a,i, get_color(randint(0, 255), randint(0, 255), randint(0, 255)))

def degrade_gris():
    """fonction qui affiche un dégradé de gris sur le canvas"""
    canvas.delete("pix")
    for i in range(1,257):
        for a in range(1,257):
            draw_pixel(a,i, get_color(a-1, a-1, a-1))

def degrade_2D():
    """fonction qui affiche le dégradé de rouge et bleu sur le canvas"""
    canvas.delete("pix")
    for i in range(1,257):
        for a in range(1,257):
            draw_pixel(a,i, get_color(a-1, 0, i-1))

root = Tk()
Button1 = Button(root, text="Aléatoire", fg = "Blue", command = ecran_aleatoire)
Button2 = Button(root, text="Dégradé gris", command = degrade_gris)
Button3 = Button(root, text="Dégradé 2D", command = degrade_2D)

canvas = Canvas(root, width = 256, height = 256, bg = "Black")
draw_pixel(10,10, get_color(255,255,255))

Button1.grid(row = 0, column = 0)
Button2.grid(row = 1, column = 0)
Button3.grid(row = 2, column = 0)

canvas.grid(row = 0, column = 1, rowspan = 3)
root.mainloop()
