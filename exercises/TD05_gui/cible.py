from tkinter import *
root = Tk()
cote = 500
colors = ["Blue", "green", "black", "yellow", "magenta", "red"]
nb_cercle = 20
canvas = Canvas(root, width = cote, height = cote, bg="Black")
canvas.pack()
for i in range(nb_cercle):
    canvas.create_oval((0 + ((cote/2)//nb_cercle)*i, 0 + ((cote/2)//nb_cercle)*i), (cote - ((cote/2)//nb_cercle)*i,cote - ((cote/2)//nb_cercle)*i ), fill = colors[i%len(colors)])
root.mainloop()