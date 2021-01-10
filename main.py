"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : Fontions d'appels de fonction (tir et deplacement vaisseau)
Pareil pour le debut du jeu quand on appuie sur jouer
"""
import random
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu

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

class alien:

    def __init__(self, canvas, vitesse, taille, mw, Xpos, Ypos, image_alien, image_tir, vaisseau):
        
        self.vitesse = vitesse
        self.taille = taille
        self.fenetre = mw
        self.descente=0
        self.xpos_tir = xpos_tir_alien
        self.ypos_tir = ypos_tir_alien
        self.canvas = canvas
        coord = 10, 50, 240, 210
        self.alien = PhotoImage(file=image_alien)
        self.laser = PhotoImage(file=image_tir)
        self.vaisseau = vaisseau 
        self.arc = C.create_image(100,100,image=self.alien)
        self.X= Xpos-50
        self.Y= Ypos
        self.sens=1
        self.canShoot = True
         #Creation du tir 
        self.mouvement()
        self.creation_tir()
        position_vaisseau = C.coords(self.vaisseau.imageVaisseau)[0]
        
    def mouvement(self):
        
        
        if self.X+self.taille > lar_canv:
            self.sens=-1
            
        
        if self.X-self.taille/2 < 0:
            self.sens=1
            self.descente =1
        if self.descente==1:
            self.Y+=70
            self.descente=0


        self.X=self.X+self.vitesse*self.sens
        C.coords(self.arc ,self.X - self.taille,self.Y - self.taille)#Y-self.taille
        # mise a jour 
        self.fenetre.after(80,self.mouvement)
        '''if C.coords(self.tir)[0] > C.coords(self.vaisseau.imageVaisseau)[0] and C.coords(self.tir)[0] < C.coords(self.vaisseau.imageVaisseau)[2] and C.coords(self.tir)[3] > C.coords(self.vaisseau.imageVaisseau)[1]:
            C.delete(self.vaisseau.imageVaisseau)'''
        #Fonction lambda (Permet d'ajouter des arguments a la fonction)
        #self.fenetre.after(80,lambda: self.mouvement())
        
    def creation_tir(self):#Crée le tir à l'endroit ou est l'alien

        self.xpos_tir=self.X
        self.ypos_tir=self.Y

        self.tir = C.create_image(self.xpos_tir, self.ypos_tir,image= self.laser )
        
        if self.canShoot:
            self.tir_alien()
            self.canShoot = False

        #Mettre ici des conditions pour supprimer la boule (si vaisseau touché)
        self.fenetre.after(2100,lambda: C.delete(self.tir))
        
        self.fenetre.after( random.randint(2100, 2400),self.creation_tir)

    def tir_alien(self): #Deplacement du tir a partir du moment ou il est envoye
        self.ypos_tir=self.ypos_tir+3.4
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir)
        self.fenetre.after(8,self.tir_alien)

class vaisseau:
    def __init__(self, vitesse_de_tir, taille_vaisseau):
        self.tir=vitesse_de_tir
        self.taille= taille_vaisseau
        self.xpos=lar_canv / 2
        self.ypos=480
        self.xpos_tir=xpos_tir_vaisseau
        self.ypos_tir=ypos_tir_vaisseau
        self.vaisseau=PhotoImage(file="Images/vaisseau2.png")
        self.imageTir=PhotoImage(file="Images/tir2.png")
        self.canShoot=True
        self.shoot=True
        #Creation du tir 
        #self.tir = C.create_arc(self.xpos_tir, self.ypos_tir, 275, 275, start=-270, extent=359, fill="yellow")
        #self.tir_vaisseau()

        self.imageVaisseau = C.create_image(self.xpos - self.taille, self.ypos_tir - self.taille, image=self.vaisseau)
        
        mw.bind('<Right>', self.droite)
        mw.bind('<Left>', self.gauche)
        mw.bind('<space>', self.creation_tir)

    def creation_tir(self,event):
        #self.tir1=PhotoImage(file="Images/tir2.png")
        #self.imageTir = C.create_image(self.xpos, self.ypos, image=self.tir1)
        
        self.tir = C.create_image(self.xpos_tir, self.ypos, image=self.imageTir)
        '''self.tir = C.create_arc(self.xpos, self.ypos, 275, 75, start=-270, extent=359, fill="yellow")
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos
        if self.canShoot==True:
            self.tir_vaisseau()
            self.canShoot=False
            self.shoot=False'''
        #self.tir = C.create_arc(self.xpos, self.ypos, 275, 75, start=-270, extent=359, fill="yellow")
        self.tir_vaisseau()
        #self.ypos_tir=self.ypos
        mw.after(1500, lambda: C.delete(self.tir))
        '''if self.canShoot:
            self.tir_vaisseau()
            mw.after(1500, lambda: C.delete(self.tir))
            self.canShoot = False'''
        self.tir_vaisseau()
        mw.after(2000, lambda: C.delete(self.tir))    

    def tir_vaisseau(self): #Deplacement du tir a partir du moment ou il est envoye
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos
        #self.ypos_tir=self.ypos_tir-10
        #C.move(self.tir, self.xpos_tir, self.ypos_tir)
        #C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-20,self.xpos_tir+20,self.ypos_tir+20)
        C.move(self.tir, 0, -10)
        mw.after(50,self.tir_vaisseau)
        '''if self.ypos_tir>haut_canv:
            C.delete(self.tir)
            self.shoot=True'''

    def droite(self,event):
        posx = 10
        posy=0
        self.xpos = self.xpos + posx

        if self.xpos<lar_canv:
            C.move(self.imageVaisseau, posx, posy)
        else:
            self.xpos=lar_canv-10

    def gauche(self,event):
        posx = -10
        posy=0
        self.xpos = self.xpos + posx
        
        if self.xpos>33:
            C.move(self.imageVaisseau, posx, posy)
        else:
            self.xpos=35
    #def collision(self):

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
        

class obstacle:
    def __init__(self,posX,posY):
        self.obs_x=posX
        self.obs_y=posY
        self.obs=PhotoImage(file="Images/obstacle.png")
        self.obstacle = C.create_image(self.obs_x,self.obs_y, image=self.obs)
    def retourpos(self):
        return(self.obs_x)
        return(self.obs_y)
        
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
    
    alien0 = alien(C,5,50, mw, X, 180, "Images/alien.png", "Images/tir.png", vaiss)
    alien1 = alien(C,5,50, mw, X+400, 180, "Images/alien5.png", "Images/tir.png", vaiss)
    alien2 = alien(C,5,50, mw, X+200, 180, "Images/alien.png", "Images/tir.png", vaiss)
    alien3 = alien(C,5,50, mw, X-200, 180, "Images/alien5.png", "Images/tir.png", vaiss)
    alien4 = alien(C,5,50, mw, X-400, 180, "Images/alien.png", "Images/tir.png", vaiss)
    alien5 = alien(C,5,50, mw, X-600, 180, "Images/alien5.png", "Images/tir.png", vaiss)

    alien6 = alien(C,7, 50, mw, X, 100, "Images/alien2.png", "Images/tir4.png", vaiss)
    alien7 = alien(C,7, 50, mw, X+500, 100, "Images/alien2.png", "Images/tir4.png", vaiss)
    alien8 = alien(C,7, 50, mw, X-600, 100, "Images/alien2.png", "Images/tir4.png", vaiss)

    # aliens plus rapides
    '''
    alien7 = alien(10, 50, mw, X, 300, "Images/alien3.png")
    alien8 = alien(10, 50, mw, X+200, 300, "Images/alien3.png")
    alien9 = alien(10, 50, mw, X-200, 300, "Images/alien3.png")
    '''

    #test
    print(alien2.xpos_tir)
    print(vaiss.imageVaisseau.coords[0])
    print(vaiss.xpos_tir)
    print(vaiss.ypos_tir)

    #condition de collision
    if lar_w==10:
        C.delete(vaiss.imageVaisseau)
        print("Game Over")

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
