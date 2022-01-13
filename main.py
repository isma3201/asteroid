from logging import root

from asteroid import asteroid
from vaisseau import vaisseau
import pygame
import core


def setup():
    print('SetUp :')
    core.WINDOW_SIZE=[800,800]
    core.fps=30

    core.memory("asteroid",[])
    core.memory("vaisseau",[])

    core.memory("nbAsteroid",50)
    core.memory("nbVaisseau",1)

    for i in range(0,core.memory("nbAsteroid")):
        core.memory("asteroid").append(asteroid())

    for i in range(0,core.memory("nbVaisseau")):
        core.memory("vaisseau").append(vaisseau())



def run():
    core.cleanScreen()





    #CONTROL
    if core.getKeyPressList("q"):
        pygame.quit()
    if core.getKeyPressList("r"):
        core.memory("asteroid",[])
        core.memory("vaisseau", [])
        for i in range(0, core.memory("nbAsteroid")):
            core.memory("asteroid").append(asteroid())
        for i in range(0, core.memory("nbVaisseau")):
            core.memory("vaisseau").append(vaisseau())


    #AFFICHAGE
    for p in core.memory("asteroid"):
        p.afficher()
    for p in core.memory("vaisseau"):
        p.afficher()

    #MISE A JOUR DES POSITIONS
    for p in core.memory("asteroid"):
        p.deplacement()
        p.bordure(core.WINDOW_SIZE)

    for p in core.memory("vaisseau"):
        p.deplacement(core.memory("asteroid"))
        p.bordure(core.WINDOW_SIZE)

    for p in core.memory("vaisseau"):
        p.manger(core.memory("asteroid"))

core.main(setup,run)