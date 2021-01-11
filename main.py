"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : Fontions d'appels de fonction (tir et deplacement vaisseau)
Pareil pour le debut du jeu quand on appuie sur jouer
"""
import random
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu
from vaisseau import vaisseau
from alien import alien
from obstacle import obstacle

#Variables
lar_w=580
haut_w=560
lar_canv=960
haut_canv=540
X = lar_canv / 2
Y = haut_canv / 2
xpos_tir_alien=300
ypos_tir_alien=300
xpos_tir_vaisseau=490
ypos_tir_vaisseau=500
  
#lancement du jeu
def jeu():
    print("Lancement du jeu")
    ButtonJouer.destroy()

    vaiss = vaisseau(10,20)

    obs1 = obstacle(80, 380)
    obs2 = obstacle(300,380)
    obs3 = obstacle(500,380)
    obs4 = obstacle(700,380)
    obs5 = obstacle(900,380)
    
    alien0 = alien(C,5,50, mw, X, 180, "Images/alien.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien1 = alien(C,5,50, mw, X+400, 180, "Images/alien5.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien2 = alien(C,5,50, mw, X+200, 180, "Images/alien.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien3 = alien(C,5,50, mw, X-200, 180, "Images/alien5.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien4 = alien(C,5,50, mw, X-400, 180, "Images/alien.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien5 = alien(C,5,50, mw, X-600, 180, "Images/alien5.png", "Images/tir.png", vaiss, obs1, obs2, obs3, obs4, obs5)

    alien6 = alien(C,7, 50, mw, X, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien7 = alien(C,7, 50, mw, X+500, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien8 = alien(C,7, 50, mw, X-300, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)

    # aliens plus rapides
    '''
    alien7 = alien(10, 50, mw, X, 300, "Images/alien3.png")
    alien8 = alien(10, 50, mw, X+200, 300, "Images/alien3.png")
    alien9 = alien(10, 50, mw, X-200, 300, "Images/alien3.png")
    '''

    #test
    print(alien2.xpos_tir)
    #print(vaiss.imageVaisseau.coords[0])
    print(vaiss.xpos_tir)
    print(vaiss.ypos_tir)

    #condition de collision
    if lar_w==10:
        C.delete(vaiss.imageVaisseau)
        print("Game Over")

    #def rejouer():
        


def propos():
    propos_window=Tk()
    propos_window.title("A propos de notre jeux")
    txt_lbl=Label(propos_window, text="A propos:\n\n\n Jeu développé en Python ! !\n\n\n Createurs: Silia et Etienne :)")
    txt_lbl.pack(padx=100,pady=100)
    propos_window.mainloop()
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
menufichier.add_command(label="A propos",command=propos)
menubar.add_cascade(label="Fichier", menu=menufichier)
mw.config(menu=menubar)

#Zone de texte
score= Label(mw, bg="darkgray", text="Votre Score :")
score.pack(padx=0, pady=0)
vie= Label(mw, bg="darkgray", text="Nombre de vies restantes :")
vie.pack(padx=0, pady=0)

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

#Bouton A propos
ButtonPropos=Button(mw,text='A propos',command=propos)
ButtonPropos.pack(padx=50, pady=0)
#lancement du gestionnaire d'evenements
mw.mainloop()

'''class missile:

    def tir_alien(self): #Deplacement du tir a partir du moment ou il est envoye
        self.ypos_tir=self.ypos_tir+3.4
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-150)
        
        self.fenetre.after(8,self.tir_alien)

    def __init__(self,X,Y):
        self.xpos_tir=self.X
        self.ypos_tir=self.Y
        self.laser=PhotoImage(file="Images/tir.png")

        self.tir = C.create_image(self.xpos_tir, self.ypos_tir,image= self.laser )

        if self.canShoot:
            self.tir_alien()
            self.canShoot = False

        
        #Mettre ici des conditions pour supprimer la boule (si vaisseau touché)
        self.fenetre.after(2100,lambda: C.delete(self.tir))
            
        self.fenetre.after( random.randint(2100, 2400),self.creation_tir)    

    #Fonction permettant de retourner les positions du missile
    def fGet(self):
        return (self.xpos_tir, self.ypos_tir)
    
    def tir_alien(self): #Deplacement du tir a partir du moment ou il est envoye
        self.ypos_tir=self.ypos_tir+3.4
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-150)
        
        self.fenetre.after(8,self.tir_alien)'''