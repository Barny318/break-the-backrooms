import pygame
SCREEN_WIDTH, SCREEN_HEIGHT = 1067, 600
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Carga las secuencias de imágenes y escálalas a 32x32 píxeles
        self.images_up = [pygame.image.load("asset/back1.png"), pygame.image.load("asset/back.png"),pygame.image.load("asset/back3.png")]
        self.images_down = [pygame.image.load("asset/front1.png"), pygame.image.load("asset/front.png"),pygame.image.load("asset/front3.png")]
        self.images_left = [pygame.image.load("asset/left1.png"), pygame.image.load("asset/leftside.png"),pygame.image.load("asset/left3.png")]
        self.images_right = [pygame.image.load("asset/right1.png"), pygame.image.load("asset/rightside.png"),pygame.image.load("asset/right3.png")]
        self.image_idle = pygame.image.load("asset/front.png")

        self.images_up = [pygame.transform.scale(img, (32, 32)) for img in self.images_up]
        self.images_down = [pygame.transform.scale(img, (32, 32)) for img in self.images_down]
        self.images_left = [pygame.transform.scale(img, (32, 32)) for img in self.images_left]
        self.images_right = [pygame.transform.scale(img, (32, 32)) for img in self.images_right]
        self.image_idle = pygame.transform.scale(self.image_idle, (32, 32))

        self.image = self.image_idle  # Imagen inicial
        self.direction = "idle"  # Dirección inicial
        self.frame = 0  # Índice de la imagen actual en la secuencia
        self.animation_speed = 0.2  # Velocidad de la animación
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.keys = 0
        self.lives = 5
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # Resto del código de inicialización
        self.injured = False  # Inicialmente el jugador no está herido
        self.injured_time = 0  # Tiempo en que el jugador se lastimó
        self.injured_duration = 3000
        self.damaged = False  # Nueva variable de instancia para rastrear el daño
        self.damage_animation_time = 1000

    def update(self):
         if self.direction == "up":
            self.images = self.images_up
         elif self.direction == "down":
            self.images = self.images_down
         elif self.direction == "left":
            self.images = self.images_left
         elif self.direction == "right":
            self.images = self.images_right
         else:
            self.images = [self.image_idle]

        # Calcula el índice basado en el tiempo transcurrido y la velocidad de animación
         self.frame += self.animation_speed
         if self.frame >= len(self.images):
             self.frame = 0
        # Actualiza la imagen según la dirección y el índice calculado
         self.image = self.images[int(self.frame)]
            
         if self.injured:
            elapsed_time = pygame.time.get_ticks() - self.injured_time
            if elapsed_time < self.injured_duration:
                    # Calcula la imagen a mostrar (idle o rojo) en función del tiempo
                if (elapsed_time // 200) % 2 == 0:
                    self.image 
                else:
                    if self.image_idle:
                        self.image = pygame.image.load("asset/red.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                    if self.moving_down == True:    
                        self.image = pygame.image.load("asset/red.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                    if self.moving_up == True:   
                        self.image = pygame.image.load("asset/red1.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                    if self.moving_left == True:   
                        self.image = pygame.image.load("asset/red2.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
                    if self.moving_right == True:    
                        self.image = pygame.image.load("asset/red3.png")
                        self.image = pygame.transform.scale(self.image, (32, 32))
            else:
                    self.injured = False
                    self.image = self.images[int(self.frame)]
    def move(self, direction, walls):
        speed = 4

        if direction == "up":
            self.rect.y -= speed
            self.direction = "up"
        elif direction == "down":
            self.rect.y += speed
            self.direction = "down"
        elif direction == "left":
            self.rect.x -= speed
            self.direction = "left"
        elif direction == "right":
            self.rect.x += speed
            self.direction = "right"
        else:
            self.direction = "idle"

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if direction == "up":
                    self.rect.y += speed
                elif direction == "down":
                    self.rect.y -= speed
                elif direction == "left":
                    self.rect.x += speed
                elif direction == "right":
                    self.rect.x -= speed
    
    def draw(self, surface, camera_x, camera_y):
        player_x_on_screen = self.rect.x + camera_x
        player_y_on_screen = self.rect.y + camera_y

        surface.blit(self.image, (player_x_on_screen, player_y_on_screen))
    def subtract_life(self):  
            if self.lives > 0:
                self.rect.x = SCREEN_WIDTH // 7
                self.rect.y = SCREEN_HEIGHT // 4
                self.lives -= 1 
                self.injured = True
                self.injured_time = pygame.time.get_ticks()

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.animation_images = [pygame.image.load("asset/1.png"), pygame.image.load("asset/2.png"),pygame.image.load("asset/3.png"),pygame.image.load("asset/4.png")]
        self.current_frame = 0

        self.image = self.animation_images[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.creation_time = pygame.time.get_ticks()

        self.animation_delay = 100  
        self.last_frame_change = pygame.time.get_ticks()
        self.creation_time = pygame.time.get_ticks() 
    def update(self):

        if pygame.time.get_ticks() - self.last_frame_change > self.animation_delay:
            self.current_frame = (self.current_frame + 1) % len(self.animation_images)
            self.image = self.animation_images[self.current_frame]
            self.last_frame_change = pygame.time.get_ticks()

        self.rect.y -= 5  
        if self.rect.bottom < 0:
            self.kill()