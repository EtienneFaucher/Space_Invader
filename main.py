"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : rien
"""

from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu

#Variables
lar_w=580
haut_w=560
lar_canv=480
haut_canv=360
X=lar_canv/2
Y=haut_canv/2

class alien:
    def __init__(self, vitesse, taille, mw, Xpos):
        
        self.vitesse=vitesse
        self.taille=taille
        self.fenetre=mw
        coord = 10, 50, 240, 210
        self.arc = C.create_arc(coord, start=20, extent=320, fill="red")
        self.X=Xpos-50
        self.sens=1
        self.mouvement()
        
    def mouvement(self):
        Y=haut_canv/2
        
        

        
        if self.X+self.taille > lar_canv:
            self.sens=-1
            
        
        if self.X-self.taille/2 < 0:
            self.sens=1

        self.X=self.X+self.vitesse*self.sens
        C.coords(self.arc ,self.X-self.taille,Y-self.taille,self.X+self.taille,Y+self.taille)
        # mise à jour toutes les 50 ms
        self.fenetre.after(80,self.mouvement)
        
        #Fonction lambda (Permet d'ajouter des arguments à la fonction)
        #self.fenetre.after(80,lambda: self.mouvement())

class vaisseau:
    def __init__(self, vitesse_de_tir, taille_vaisseau):
        self.tir=vitesse_de_tir
        self.taille= taille_vaisseau
        self.xpos=20
        self.ypos=20
        self.xpos_tir=300
        self.ypos_tir=300
        self.tir_vaisseau
        self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")


    def tir_vaisseau(self):
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos_tir+5
        
        
        self.ypos_tir+=self.tir
        C.coords(self.tir ,self.xpos_tir-200,self.ypos_tir-200,self.xpos_tir+400,self.ypos_tir+400)


        mw.after(80,self.tir_vaisseau)

    def deplacement(self):
        #Meme code que "mouvement" mais pas de repetition. La fonction est appellée via un évenement de touche.
        c=3

# Création de la fenêtre graphique
mw = Tk()
mw.title('Space Invader')
#Taille de fenêtre
mw.geometry('780x660+900+150')
mw.configure(bg='black')

#Menu
menubar= Menu(mw)
menufichier= Menu(menubar,tearoff=0)
menufichier.add_command(label="Quitter", command = mw.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)
mw.config(menu=menubar)


#Zone de texte
score= Label(mw, bg="darkgray", text="Votre Score :")
score.pack(padx=0, pady=0)

#Bouton début de partie
ButtonJouer=Button(mw,text='Jouer',command="")
ButtonJouer.pack(padx=50, pady=0)

#Canevas
filename = PhotoImage(file="Images/fond.gif" , master=mw,)
C = Canvas(mw, height=540, width=460)
C.create_image(200,200, image=filename)



arc=alien(5,50, mw, X)
m=vaisseau(10,10)
C.pack()

m=vaisseau(10,10)
#Bouton quitter
ButtonQuitter=Button(mw,text='Quitter',command=mw.destroy)
ButtonQuitter.pack(padx=50, pady=0)




#lancement du gestionnaire d'événements
mw.mainloop()
