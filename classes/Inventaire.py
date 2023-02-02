import pygame
from classes.Objet import Objet


class Inventaire(object):
    inventaire: [Objet] = []

    def __init__(self):
        self.inventaire = []

    def get_inventory(self):
        return self.inventaire

    def get_objects(self):  # pour débug principalement
        objects = []
        for obj in self.inventaire:
            objects += [[obj.nom, obj.count, obj.nom_image]]

        return objects

    def has_object_by_name(self, objet: str):
        for obj in self.inventaire:
            if obj.nom == objet:
                return True

        return False

    def add_item(self, objet: Objet):
        try:
            already_exist = False
            for obj in self.inventaire:
                if obj.nom == objet.nom:
                    already_exist = True
                    obj.count += 1

            if not already_exist:
                self.inventaire.append(objet)

            # print("l'objet " + objet.nom + " a été ajouté à l'inventaire")  # debug
        except:
            print("une erreur s'est produite")

    def remove_item(self, objet: Objet):
        exist = False
        for obj in self.inventaire:
            if obj.nom == objet.nom:
                exist = True

                if obj.count > 1:  # si il a plus d'un objet, n'en n'enlève qu'un
                    obj.count -= 1
                else:
                    self.inventaire.remove(obj)  # sinon retirer complètement l'objet

        if not exist:
            print("l'objet n'existe pas")
