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
from obstacle import obstacle
from main import mw, C


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

    def mouvement(self):
        print(C.coords(self.vaisseau.imageVaisseau)[1])
        
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

        self.tir = C.create_image(self.xpos_tir, self.ypos_tir, image=self.laser )
        
        if self.canShoot:
            self.tir_alien()
            self.canShoot = False

        #Mettre ici des conditions pour supprimer la boule (si vaisseau touché)
        #self.fenetre.after(1000,lambda: C.delete(self.tir))
        self.fenetre.after( random.randint(3100, 3500),self.creation_tir)
        if self.ypos_tir > 300:
            C.delete(self.tir)

    def tir_alien(self): #Deplacement du tir a partir du moment ou il est envoye
        self.ypos_tir=self.ypos_tir+1.4
        C.coords(self.tir ,self.xpos_tir-20,self.ypos_tir)
        self.fenetre.after(8,self.tir_alien)
        if self.ypos_tir > haut_canv-50:
            C.delete(self.tir)

        if (self.xpos_tir >= self.obstacle1.obs_x - 30) and (self.xpos_tir <= self.obstacle1.obs_x + 50) and (self.ypos_tir  >= self.obstacle1.obs_y):
            print("Obstacle1 touché")
            C.delete(self.tir)
            C.delete(self.obstacle1.obstacle)
        if (self.xpos_tir >= self.obstacle2.obs_x -30 ) and (self.xpos_tir <= self.obstacle2.obs_x + 30) and (self.ypos_tir  >= self.obstacle2.obs_y):
            print("Obstacle2 touché")
            C.delete(self.tir)
            C.delete(self.obstacle2.obstacle)
        if (self.xpos_tir >= self.obstacle3.obs_x -30) and (self.xpos_tir <= self.obstacle3.obs_x + 30) and (self.ypos_tir  >= self.obstacle3.obs_y):
            print("Obstacle3 touché")
            C.delete(self.tir)
            C.delete(self.obstacle3.obstacle)
        if (self.xpos_tir >= self.obstacle4.obs_x -30) and (self.xpos_tir <= self.obstacle4.obs_x + 30) and (self.ypos_tir  >= self.obstacle4.obs_y):
            print("Obstacle4 touché")
            C.delete(self.tir)
            C.delete(self.obstacle4.obstacle)
        if (self.xpos_tir >= self.obstacle5.obs_x -30) and (self.xpos_tir <= self.obstacle5.obs_x + 30) and (self.ypos_tir  >= self.obstacle5.obs_y):
            print("Obstacle5 touché")
            C.delete(self.tir)
            C.delete(self.obstacle5.obstacle)

        if (self.xpos_tir >= C.coords(self.vaisseau.imageVaisseau)[0] -50) and (self.xpos_tir <= C.coords(self.vaisseau.imageVaisseau)[0] +50) and (self.ypos_tir  >= C.coords(self.vaisseau.imageVaisseau)[1]):
            print("- 1 vie")
            C.delete(self.tir)
            #C.delete(self.vaisseau.imageVaisseau)
            '''if collision:
                collision=False
                #C.delete(self.vaisseau.imageVaisseau)
                print("Game over")
                C.delete(self.tir)
                self.fenetre.after(80, collision=True)'''
