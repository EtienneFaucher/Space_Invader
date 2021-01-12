"""
qui : Etienne Faucher / Silia Taider
quand : le 08/12/2020 
Jeu Space invader
TODO : Fontions d'appels de fonction (tir et deplacement vaisseau)
Pareil pour le debut du jeu quand on appuie sur jouer
"""
#On importe les modules
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
nbrvie=3

#On crée notre premiere classe "alien", qui va nous permettre des créer les differents méchants du jeu.
class alien:
    #On initialise ici toutes les variables utiles. ON en importe certaine depuis le programme principal.
    def __init__(self, canvas, vitesse, taille, mw, Xpos, Ypos, image_alien, image_tir, vaisseau, obstacle1, obstacle2, obstacle3, obstacle4, obstacle5):
        
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
        self.obstacle1 = obstacle1
        self.obstacle2 = obstacle2
        self.obstacle3 = obstacle3
        self.obstacle4 = obstacle4
        self.obstacle5 = obstacle5
         #Creation du tir 
        self.mouvement()
        self.creation_tir()
        position_vaisseau = C.coords(self.vaisseau.imageVaisseau)[0]
        collision=True
        self.detruit1= False
        self.detruit2= False
        self.detruit3= False
        self.detruit4= False
        self.detruit5= False

    def mouvement(self):
        #print(C.coords(self.vaisseau.imageVaisseau)[1])
        
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

        
        if self.canShoot:
            self.tir = C.create_image(self.xpos_tir, self.ypos_tir, image=self.laser )
            self.tir_alien()
            self.canShoot = False

        #Mettre ici des conditions pour supprimer la boule (si vaisseau touché)
        #self.fenetre.after(1000,lambda: C.delete(self.tir))
        self.fenetre.after( random.randint(4100, 4500),self.creation_tir)
        if self.ypos_tir > haut_canv - 100:
            C.delete(self.tir)
        
    def tir_alien(self): #Deplacement du tir a partir du moment ou il est créé.
        afterTir=None
        if self.tir:
            
            self.ypos_tir=self.ypos_tir+1
            C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir)
            afterTir=self.fenetre.after(8,self.tir_alien)
            if self.ypos_tir > haut_canv-50:
                C.delete(self.tir)

            if (self.xpos_tir >= self.obstacle1.obs_x - 30) and (self.xpos_tir <= self.obstacle1.obs_x + 50) and (self.ypos_tir  >= self.obstacle1.obs_y):
                print("Obstacle1 touché")
                C.delete(self.tir)
                self.tir=None
                C.delete(self.obstacle1.obstacle)
                self.obstacle1.obs_x = self.xpos_tir +35
                #self.detruit1 == True
            if (self.xpos_tir >= self.obstacle2.obs_x -30 ) and (self.xpos_tir <= self.obstacle2.obs_x + 30) and (self.ypos_tir  >= self.obstacle2.obs_y):
                print("Obstacle2 touché")
                C.delete(self.tir)
                self.tir=None
                C.delete(self.obstacle2.obstacle)
                self.obstacle1.obs_x = self.xpos_tir +35
                #self.detruit2 == True
            if (self.xpos_tir >= self.obstacle3.obs_x -30) and (self.xpos_tir <= self.obstacle3.obs_x + 30) and (self.ypos_tir  >= self.obstacle3.obs_y):
                print("Obstacle3 touché")
                C.delete(self.tir)
                self.tir=None
                C.delete(self.obstacle3.obstacle)
                self.obstacle1.obs_x = self.xpos_tir +35
                #self.detruit3 == True
            if (self.xpos_tir >= self.obstacle4.obs_x -30) and (self.xpos_tir <= self.obstacle4.obs_x + 30) and (self.ypos_tir  >= self.obstacle4.obs_y):
                print("Obstacle4 touché")
                C.delete(self.tir)
                self.tir=None
                C.delete(self.obstacle4.obstacle)
                self.obstacle1.obs_x = self.xpos_tir +35
                #self.detruit4 == True
            if (self.xpos_tir >= self.obstacle5.obs_x -30) and (self.xpos_tir <= self.obstacle5.obs_x + 30) and (self.ypos_tir  >= self.obstacle5.obs_y):
                print("Obstacle5 touché")
                C.delete(self.tir)
                self.tir=None

                C.delete(self.obstacle5.obstacle)
                self.obstacle1.obs_x = self.xpos_tir +35
                #self.detruit == True

            if (self.xpos_tir >= C.coords(self.vaisseau.imageVaisseau)[0] -40) and (self.xpos_tir <= C.coords(self.vaisseau.imageVaisseau)[0] +40) and (self.ypos_tir  >= C.coords(self.vaisseau.imageVaisseau)[1]):
                if self.vaisseau.vie > 1:
                    C.delete(self.tir)
                    self.tir=None
                    self.vaisseau.vie = self.vaisseau.vie - 1
                    print("vie =", self.vaisseau.vie)
                if self.vaisseau.vie == 1:
                    #C.delete(self.vaisseau.imageVaisseau)
                    mw.destroy()
                    gameOver_window=Tk()
                    gameOver_window.title("Game Over")
                    txt_lbl=Label(gameOver_window, text="GAME OVER!\n\n\n Jeu développé en Python ! !\n\n\n Createurs: Silia et Etienne :)")
                    txt_lbl.pack(padx=100,pady=100)
                    bouton_rejouer = Button(gameOver_window, text = "Rejouer", command = jeu)
                    bouton_rejouer.pack(padx=50, pady=0)
                    gameOver_window.mainloop()
        elif afterTir:
            self.fenetre.after_cancel(afterTir)
        else:
            self.canShoot=True 
              
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
        self.vie = 15
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
        
        #self.tir_vaisseau()
        #self.ypos_tir=self.ypos
        #mw.after(1500, lambda: C.delete(self.tir))
        '''if self.canShoot:
            self.tir_vaisseau()
            mw.after(1500, lambda: C.delete(self.tir))
            self.canShoot = False'''
        if self.canShoot:
            self.tir_vaisseau()
            mw.after(2000, lambda: C.delete(self.tir)) 
            self.canShoot=False   

    def tir_vaisseau(self): #Deplacement du tir a partir du moment ou il est envoye
        self.xpos_tir=self.xpos
        self.ypos_tir=self.ypos
        #self.ypos_tir=self.ypos_tir-10
        #C.move(self.tir, self.xpos_tir, self.ypos_tir)
        #C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir-20,self.xpos_tir+20,self.ypos_tir+20)
        C.move(self.tir, 0, -10)
        mw.after(50,self.tir_vaisseau)
        alien_touche()


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

    def init2(self,alien0, alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8):

        self.alien0 = alien0
        self.alien1 = alien1
        self.alien2 = alien2
        self.alien3 = alien3
        self.alien4 = alien4
        self.alien5 = alien5
        self.alien6 = alien6
        self.alien7 = alien7
        self.alien8 = alien8
 
    def alien_touche(self):
        print(self.xpos_tir, self.alien0.xpos_tir)
        if ((self.xpos_tir >= self.alien0.xpos_tir -50) or (self.xpos_tir <= self.alien0.xpos_tir + 50)) and (self.ypos_tir  <= self.alien0.ypos_tir):
            print("alien0 touché")
            C.delete(self.tir)
            C.delete(self.alien0.arc)
        if ((self.xpos_tir >= self.alien1.xpos_tir -50) or (self.xpos_tir <= self.alien1.xpos_tir + 50)) and (self.ypos_tir  <= self.alien1.ypos_tir):
            print("alien1 touché")
            C.delete(self.tir)
            C.delete(self.alien1.arc)
        if ((self.xpos_tir >= self.alien2.xpos_tir -50) or (self.xpos_tir <= self.alien2.xpos_tir + 50)) and (self.ypos_tir  <= self.alien2.ypos_tir):
            print("alien2 touché")
            C.delete(self.tir)
            C.delete(self.alien2.arc)
        if ((self.xpos_tir >= self.alien3.xpos_tir -50) or (self.xpos_tir <= self.alien3.xpos_tir + 50)) and (self.ypos_tir  <= self.alien3.ypos_tir):
            print("alien3 touché")
            C.delete(self.tir)
            C.delete(self.alien3.arc)
        if ((self.xpos_tir >= self.alien4.xpos_tir -50) or (self.xpos_tir <= self.alien4.xpos_tir + 50)) and (self.ypos_tir  <= self.alien4.ypos_tir):
            print("alien4 touché")
            C.delete(self.tir)
            C.delete(self.alien4.arc)
        if ((self.xpos_tir >= self.alien5.xpos_tir -30) or (self.xpos_tir <= self.alien5.xpos_tir + 30)) and (self.ypos_tir  >= self.alien5.ypos_tir):
            print("alien5 touché")
            C.delete(self.tir)
            C.delete(self.alien5.arc)
        if ((self.xpos_tir >= self.alien6.xpos_tir -30) or (self.xpos_tir <= self.alien6.xpos_tir + 30)) and (self.ypos_tir  >= self.alien6.ypos_tir):
            print("alien6 touché")
            C.delete(self.tir)
            C.delete(self.alien6.arc)
        if ((self.xpos_tir >= self.alien7.xpos_tir -30) or (self.xpos_tir <= self.alien7.xpos_tir + 30)) and (self.ypos_tir  >= self.alien7.ypos_tir):
            print("alien7 touché")
            C.delete(self.tir)
            C.delete(self.alien7.arc)
        if ((self.xpos_tir >= self.alien8.xpos_tir -30) or (self.xpos_tir <= self.alien8.xpos_tir + 30)) and (self.ypos_tir  >= self.alien8.ypos_tir):
            print("alien8 touché")
            C.delete(self.tir)
            C.delete(self.alien8.arc)  
           

class obstacle:
    def __init__(self,posX,posY):
        self.obs_x=posX
        self.obs_y=posY
        self.obs=PhotoImage(file="Images/obstacle.png")
        self.obstacle = C.create_image(self.obs_x,self.obs_y, image=self.obs)
    def retourpos(self):
        return(self.obs_x, self.obs_y)

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

    # aliens plus rapides
    alien6 = alien(C,7, 50, mw, X, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien7 = alien(C,7, 50, mw, X+500, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)
    alien8 = alien(C,7, 50, mw, X-300, 100, "Images/alien2.png", "Images/tir4.png", vaiss, obs1, obs2, obs3, obs4, obs5)

    vaiss.init2(alien0, alien1, alien2, alien3, alien4, alien5, alien6, alien7, alien8)

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


def propos():
    apropos_window=Tk()
    apropos_window.title("A propos de notre jeux")
    txt_lbl=Label(apropos_window, text="A propos:\n\n\n Jeu développé en Python ! !\n\n\n Createurs: Silia et Etienne :)")
    txt_lbl.pack(padx=100,pady=100)
    apropos_window.mainloop()
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
vie= Label(mw, bg="darkgray", text="Nombre de vies restantes :", textvariable=nbrvie)
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
Buttonpropos=Button(mw,text='A propos',command=propos)
Buttonpropos.pack(padx=50, pady=0)
#lancement du gestionnaire d'evenements
mw.mainloop()
