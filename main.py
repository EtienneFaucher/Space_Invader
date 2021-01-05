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
lar_canv=960
haut_canv=540
X=lar_canv/2
Y=haut_canv/2 

class alien:
    def __init__(self, vitesse, taille, mw, Xpos):
        
        self.vitesse=vitesse
        self.taille=taille
        self.fenetre=mw
        self.xpos_tir=300
        self.ypos_tir=300
        coord = 10, 50, 240, 210
        self.alien=PhotoImage(file="Images/alien.gif")
        self.arc = C.create_image(100,100,image=self.alien)
        self.X=Xpos-50
        self.Y= 240
        self.sens=1
        self.canShoot = True
         #Creation du tir 
        self.mouvement()

        self.creation_tir()
        
    def mouvement(self):
        Y=haut_canv/6+50
        
        if self.X+self.taille > lar_canv:
            self.sens=-1
            
        
        if self.X-self.taille/2 < 0:
            self.sens=1

        self.X=self.X+self.vitesse*self.sens
        C.coords(self.arc ,self.X-self.taille,Y-self.taille)
        # mise a jour 
        self.fenetre.after(80,self.mouvement)
        
        #Fonction lambda (Permet d'ajouter des arguments a la fonction)
        #self.fenetre.after(80,lambda: self.mouvement())
    def creation_tir(self):#Crée le tir à l'endroit ou est l'alien
        self.xpos_tir=self.X
        self.ypos_tir=self.Y-30

        self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 270, start=-270, extent=359, fill="yellow")
        
        if self.canShoot:
            self.tir_alien()
            self.canShoot = False

        #Mettre ici des conditions pour supprimer la boule (si vaisseau touché)
        self.fenetre.after(1100,lambda: C.delete(self.tir))
        
        self.fenetre.after(1400,self.creation_tir)

    def tir_alien(self): #Deplacement du tir a partir du moment ou il est envoye
        self.ypos_tir=self.ypos_tir+2
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-20,self.xpos_tir+20,self.ypos_tir+20)
        
        self.fenetre.after(8,self.tir_alien)

class vaisseau:
    def __init__(self, vitesse_de_tir, taille_vaisseau):
        self.tir=vitesse_de_tir
        self.taille= taille_vaisseau
        self.xpos=lar_canv / 2
        self.ypos=haut_canv / 2
        self.xpos_tir=490
        self.ypos_tir=500
        self.vaisseau=PhotoImage(file="Images/vaisseau2.png")

        #Creation du tir 
        #self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")
        #self.tir_vaisseau()

        #Creation du vaisseau (ne s'affiche pas c'est bizarre)
        #imagevaisseau= PhotoImage(file="Images/vaisseau2.png")
        #self.vaisseau = C.create_image(self.xpos_tir, self.ypos_tir, image=imagevaisseau)

        self.imageVaisseau = C.create_image(self.xpos - self.taille, self.ypos_tir - self.taille, image=self.vaisseau)

        mw.bind('<Right>', self.droite)
        mw.bind('<Left>', self.gauche)
        mw.bind('<space>', self.creation_tir)

    def creation_tir(self):
        self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")
        self.tir_vaisseau()

    def tir_vaisseau(self): #Deplacement du tir a partir du moment ou il est envoye
        self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos_tir-10
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-20,self.xpos_tir+20,self.ypos_tir+20)
        mw.after(80,self.tir_vaisseau)

    def droite(self,event):
        posx = 10
        posy=0
        C.move(self.imageVaisseau, posx, posy)

    def gauche(self,event):
        posx = -10
        posy=0
        C.move(self.imageVaisseau, posx, posy)

#lancement du jeu
def jeu():
    print("Lancement du jeu")
    ButtonJouer.destroy()
    vaiss = vaisseau(10,20)
    arc=alien(5,50, mw, X)
    arc2=alien(5,50, mw, X+200)
    arc3=alien(5,50, mw, X-200)
    #mw.bind("<space>", lambda x:vaiss.tir_vaisseau())

# Creation de la fenetre graphique
mw = Tk()
mw.title('Space Invader')
#Taille de fenetre
mw.geometry('1280x660')
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

#Bouton debut de partie
ButtonJouer=Button(mw,text='Jouer',command=jeu)
ButtonJouer.pack(padx=50, pady=0)

#Canevas
filename = PhotoImage(file="Images/fond1.gif" , master=mw,)
C = Canvas(mw, height=haut_canv, width=lar_canv)
C.create_image(200,200, image=filename)
C.pack()

#Bouton quitter
ButtonQuitter=Button(mw,text='Quitter',command=mw.destroy)
ButtonQuitter.pack(padx=50, pady=0)




#lancement du gestionnaire d'evenements
mw.mainloop()
