"""
qui : Etienne FAucher   
quand : le 08/12/2020 
Interface graphique du pendu
TODO : Fontions d'appels de fonction (tir et deplacement vaisseau)
Pareil pour le debut du jeu quand on appuie sur jouer
"""
import random
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage, Canvas, Menu
from alien import alien
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