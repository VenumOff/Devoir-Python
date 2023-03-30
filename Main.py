import tkinter as tk


def change_nom():
    label_nom.config(text=value.get())


def change_age():
    label_age.config(text=value.get())


pr = tk.Tk()

pr.config(bg="Skyblue")
bouton_nom = tk.Button(pr, text="Changer le nom", command=change_nom, bg="Black", fg="White", font="50", bd=5, width=14)
bouton_nom.pack()
bouton_age = tk.Button(pr, text="Changer l'âge", command=change_age, bg="Black", fg="White", font="50", bd=5, width=14)
bouton_age.pack()

label_nom = tk.Label(pr, text="Mathias", bg="Skyblue", fg="Black", font="50")
label_nom.pack()
label_age = tk.Label(pr, text="19", bg="Skyblue", fg="Black", font="50")
label_age.pack()

value = tk.StringVar()
value.set("Nom ou  Âge")
entree = tk.Entry(pr, textvariable=value, bg="Skyblue", fg="Black", width=20, font="50")
entree.pack()

bouton_quit = tk.Button(pr, text="Fermer", command=pr.quit, bg="Red", fg="White", font="50")
bouton_quit.pack()

pr.mainloop()

# 2 ligne qui affiche une info different genre nom et age
# 2 bouttons qui change le nom et l'autre l'age
# 1 zone de texte qui permet d'ecrire soit le nom soit l'age