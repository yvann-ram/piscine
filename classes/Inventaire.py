import pygame
from Objet import Objet


class Inventaire(object):
    inventaire: [Objet] = []

    def __init__(self):
        self.inventaire = []