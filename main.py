"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : Fontions d'appels de fonction (tir et deplacement vaisseau)
Pareil pour le debut du jeu quand on appuie sur jouer
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
        # mise a jour 
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
        
        #Creation du tir 
        self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")
        self.tir_vaisseau()

        #Creation du vaisseau (ne s'affiche pas c'est bizarre)
        imagevaisseau= PhotoImage(file="Images/vaisseau2.png")
        self.vaisseau = C.create_image(self.xpos_tir, self.ypos_tir, image=imagevaisseau)

    def tir_vaisseau(self): #Deplacement du tir à partir du moment ou il est envoyé
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos_tir-10
        
        
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-20,self.xpos_tir+20,self.ypos_tir+20)


        mw.after(80,self.tir_vaisseau)

    def deplacement(self): #Deplacement du vaisseau
        #Meme code que "mouvement" mais pas de repetition. La fonction est appellée via un évenement de touche.
        c=3

#lancement du jeu
def jeu():
    print("Lancement du jeu")
    arc=alien(5,50, mw, X)
    mw.bind("<space>", lambda x: tir())

#Fonction qui tire (appelée par jeu)
def tir():
    vaisseau(10,10)

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
menufichier.add_command(label="Jouer",command=jeu)
menubar.add_cascade(label="Fichier", menu=menufichier)
mw.config(menu=menubar)

#Zone de texte
score= Label(mw, bg="darkgray", text="Votre Score :")
score.pack(padx=0, pady=0)

#Bouton début de partie
ButtonJouer=Button(mw,text='Jouer',command=jeu)
ButtonJouer.pack(padx=50, pady=0)

#Canevas
filename = PhotoImage(file="Images/fond.gif" , master=mw,)
C = Canvas(mw, height=540, width=460)
C.create_image(200,200, image=filename)





C.pack()

#Bouton quitter
ButtonQuitter=Button(mw,text='Quitter',command=mw.destroy)
ButtonQuitter.pack(padx=50, pady=0)




#lancement du gestionnaire d'événements
mw.mainloop()
