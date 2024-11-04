import pygame
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y