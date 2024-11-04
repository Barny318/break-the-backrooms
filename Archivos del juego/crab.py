import pygame
import math

class CrabBoss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [ pygame.transform.scale(pygame.image.load("asset/CrabMoving1.png"), (64, 64)),
                        pygame.transform.scale(pygame.image.load("asset/CrabMoving2.png"), (64, 64)),
                        pygame.transform.scale(pygame.image.load("asset/CrabMoving3.png"), (64, 64)),
                        pygame.transform.scale(pygame.image.load("asset/CrabMoving4.png"), (64, 64))]
        self.index=0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 1504
        self.rect.y = 929
        self.timer = 0
        self.image_index = 0
        self.steps = 0
        self.max_steps = 4
        self.image_change_interval = 100  
        self.time_since_last_image_change = 0
        self.direction = 1 
        self.attacking = False
        self.attack_timer = 0
        self.attack_cooldown = 1000
        self.attack_interval=2000 
        self.last_attack_time = pygame.time.get_ticks()
        self.attacking = False 
        self.health = 5  
        self.move_distance = 40
        self.initial_position = (1501, 929) 
        self.returning_to_center = False
        self.return_speed = 4
        self.movement_timer = 0
        self.movement_interval = 450
        self.movement_distance = 40 
        self.movement_speed = 2  
        self.moving_right = True  
        self.moving_left = False
        self.center_x = self.rect.centerx
        
    def update(self, player):
        current_time = pygame.time.get_ticks()

        if current_time - self.time_since_last_image_change >= self.image_change_interval:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.time_since_last_image_change = current_time

        if current_time - self.movement_timer >= self.movement_interval:
            self.movement_timer = current_time
        if self.moving_right:
            self.rect.x += self.movement_speed
            if self.rect.centerx >= self.center_x + self.movement_distance:
                self.moving_right = False
                self.moving_left = True

        if self.moving_left:
            self.rect.x -= self.movement_speed
            if self.rect.centerx <= self.center_x - self.movement_distance:
                self.moving_left = False
                self.moving_right = True

        distance_to_player = math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
        if current_time - self.last_attack_time >= self.attack_cooldown:
            distance_to_player = math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
            if distance_to_player < 200:
                self.attacking = True
                self.last_attack_time = current_time

        if self.attacking:
            current_time = pygame.time.get_ticks()
            if current_time - self.attack_timer >= self.attack_interval:
                self.launch_projectile(player)
                self.attack_timer = current_time
                self.attacking = False
                
    def launch_projectile(self, player):
        projectile = BossProjectile(self.rect.centerx, self.rect.centery, player.rect.centerx, player.rect.centery)
        self.projectiles.add(projectile)

class BossProjectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.image.load("asset/bum.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = 4
        self.creation_time = pygame.time.get_ticks() 

    def update(self):
        angle = math.atan2(self.target_y - self.rect.centery, self.target_x - self.rect.centerx)
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)