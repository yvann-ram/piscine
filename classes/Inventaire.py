import pygame
from classes.Objet import Objet


class Inventaire(object):
    inventaire: [Objet] = []

    def __init__(self):
        self.inventaire = []

    def get_inventory(self):
        return self.inventaire

    def get_object_by_name(self, objet: str):
        for obj in self.inventaire:
            if obj.nom == objet:
                return True

        return False

    def add_item(self, objet: Objet):
        try:
            for obj in self.inventaire:
                if obj.nom == objet.nom:
                    if obj.count > 1:
                        obj.count += 1
                    else:
                        self.inventaire.append(objet)
            print("l'objet " + objet.nom + " a été ajouté à l'inventaire")
        except:
            print("une erreur s'est produite")

    def remove_item(self, objet: Objet):
        for obj in self.inventaire:
            print(obj.nom, obj.count)
            print(objet.nom, objet.count)
            if obj.nom == objet.nom:
                if obj.count > 1:
                    obj.count -= 1
                else:
                    self.inventaire.remove(obj)
            print("aa", obj.nom)

