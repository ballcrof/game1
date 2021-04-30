import pygame
White = (255, 255, 255)

class Car(pygame.sprite.Sprite):
    #car class

    def __init__(self, colour, width, height):
        #call to the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(White)
        self.image.set_colorkey(White)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        self.rect = self.image.get_rect()
