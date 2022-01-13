import random

import pygame
from pygame.math import Vector2
import core


class vaisseau:
    def __init__(self):
        self.position = Vector2(random.randint(0, 400), random.randint(0, 400))
        self.vitesse = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)

        self.couleur = (255, 255, 255)
        self.taille = 10

        self.maxVitesse = 6
        self.maxAcceleration = 4

        self.vision = 100

    def afficher(self):
        core.Draw.circle(self.couleur, self.position, self.taille)



    def deplacement(self,asteroid):

        if self.acceleration.length() > self.maxAcceleration:
            self.acceleration.scale_to_length(self.maxAcceleration)

        self.vitesse = self.vitesse + self.acceleration

        if self.vitesse.length()>self.maxVitesse:
            self.vitesse.scale_to_length(self.maxVitesse)

        self.position = self.position + self.vitesse

        self.acceleration = Vector2(0,0)


    def bordure(self,fenetre):
        if self.position.y<0:
            self.position.y = fenetre[1]

        if self.position.y > fenetre[1]:
            self.position.y=0

        if self.position.x < 0:
            self.position.x = fenetre[0]

        if self.position.x > fenetre[0]:
            self.position.x = 0

    def manger(self,asteroid):
        for p in asteroid:
            if p.position.distance_to(self.position)<self.taille+p.taille:
                p.vivante = False