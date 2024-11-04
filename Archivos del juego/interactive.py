import pygame

class InteractiveObject(pygame.sprite.Sprite):
    def __init__(self, x, y, gives_key=False):
        super().__init__()
        self.image_path = "asset/kei.png" 
        if gives_key:
            self.image_path = "asset/key.png"  
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.interactable = False

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.interactable = True
        else:
            self.interactable = False

    def interact(self, player):
        if self.image_path == "asset/key.png":
            player.keys += 1
        self.kill()
