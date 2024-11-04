import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, special=False, required_keys=0, teleport_position=None):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.required_keys = required_keys
        self.teleport_position = teleport_position  

    def interact(self, player):
        if self.teleport_position:
            player.rect.x, player.rect.y = self.teleport_position
class SuperDoor(Door):
    def __init__(self, x, y, required_keys=8, teleport_position=None):
        super().__init__(x, y, required_keys=required_keys, teleport_position=teleport_position)

    def interact(self, player):
        if player.keys >= self.required_keys:
            player.keys -= self.required_keys  
            super().interact(player)
        