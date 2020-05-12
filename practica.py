import pygame, sys

alto = 640
ancho = 480

screen = pygame.display.set_mode((alto, ancho))
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo Basico Pygame")

pygame.font.init()

gameOver = False
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver =True

    pygame.display.flip()


pygame.quit()
            