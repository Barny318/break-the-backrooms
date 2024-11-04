import pygame
class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = [pygame.image.load("asset/trap.png"), pygame.image.load("asset/trap1.png")]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.image_index = 0
        self.image_change_interval = 1500 
        self.time_since_last_image_change = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - self.time_since_last_image_change
        
        if time_elapsed >= self.image_change_interval:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.time_since_last_image_change = current_time

    def activate(self, player):
        if pygame.sprite.collide_rect(self, player):
            
            if self.image_index == len(self.images) - 1:
                player.subtract_life()
                  