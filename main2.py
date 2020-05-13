import pygame
import sys
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("images/smallball.png")
        self.position = [x, y]
        self.name = "Bola"
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __posY = (160,200,240,280)
    __names = ('Speedy', 'Lucera', 'Tonio', 'Toribio')
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("1.png")
        pygame.display.set_caption("Carrera de Bichos")
        
        for i in range (4):
            theRunner =  Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)          
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print("{} ah ganado".format(runner.name))
                    gameOver = True
           
                       
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
                       
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()