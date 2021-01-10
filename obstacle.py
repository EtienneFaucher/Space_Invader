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

class obstacle:
    def __init__(self,posX,posY):
        self.obs_x=posX
        self.obs_y=posY
        self.obs=PhotoImage(file="Images/obstacle.png")
        self.obstacle = C.create_image(self.obs_x,self.obs_y, image=self.obs)
    def retourpos(self):
        return(self.obs_x, self.obs_y)