"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : rien
"""

from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu


# création de la fenêtre graphique
mw = Tk()
mw.title('Space Invader')
#Taille de fenêtre
mw.geometry('480x360+900+150')
mw.configure(bg='black')

#Menu
menubar= Menu(mw)
menufichier= Menu(menubar,tearoff=0)
menufichier.add_command(label="Quitter", command = mw.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)
mw.config(menu=menubar)




#lancement du gestionnaire d'événements
mw.mainloop()
