import pygame.draw
from pygame import *
from pygame import font
from pygame.sprite import Sprite

#souris

#Fenetre
pygame.init()
screen = display.set_mode((1530, 780))
display.set_caption("Rob's Quest")

#Image de Fond
image = pygame.image.load("assets/LogoA.png")

#Musique de fond
# pygame.mixer.music.load("ssets/menuson.mp3")
# pygame.mixer.music.play()

# Boucle des evennements
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == K_p:
#                 # Lancer le jeu à la place
#                 pygame.quit()
#             if event.key == K_s:
#                 # Afficher le score à la place
#                 pygame.quit()
#
#     # Affichage sur la fenêtre du menu
#     screen.blit(image, (250, 200))
#
#     # Bouton Play & Score
#     police = pygame.font.SysFont("monospace", 50)
#     TextPlay = police.render("'P' = Play", True, (255, 0, 0))
#     TextQuit = police.render("'S' = Quitter", True, (255, 0, 0))
#     screen.blit(TextPlay, (640, 500))
#     screen.blit(TextQuit, (640, 550))
#
#     # ????
#     pygame.display.update()




