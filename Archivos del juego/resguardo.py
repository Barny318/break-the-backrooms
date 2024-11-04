import pygame
import sys
from crab import *
from interactive import InteractiveObject
from trampa import Trampa
from pared import Pared
from dor import *
from player import *
import feid
from disp import *
pygame.init()
pygame.mixer.init()

# Dimensiones de la ventana
SCREEN_WIDTH, SCREEN_HEIGHT = 1067, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Break the Backroom")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN=(0, 255, 0)

# Cargar imágenes
background_img = pygame.image.load("asset/Background.png")
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
font_path = "C:/Users/barba/AppData/Local/Microsoft/Windows/Fonts/Starstruck.ttf"  
normal="C:/Windows/Fonts/CENTAUR.ttf"

sound_llave=pygame.mixer.Sound("EFECTOLLAVE.mp3")
sound_llave.set_volume(1.0)
sound_fondo=pygame.mixer.Sound("FONDO.mp3")
sound_fondo.set_volume(0.5)
sound_menu=pygame.mixer.Sound("MENUMUSICA.mp3")

sound_menu.play(-1)
in_game=False
# Función para centrar texto en el botón
def draw_text(text, font, color, surface, x, y):
    text_surface = font.render(text, True, color) #Esta línea crea una superficie que contiene el texto que se va a dibujar. La función render() toma el texto, una bandera (True o False) que indica si se debe suavizar el texto (antialiasing) para hacerlo más suave, y el color del texto. El resultado se almacena en la variable text_surface.
    text_rect = text_surface.get_rect() #posiciona el texto en pantalla
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)
# Pantalla del menú
def show_menu():
    global in_game, sound_menu
    in_game = False
    while True:
        screen.blit(background_img, (0, 0)) #dibujar en pantalla .basicamente es un método que pone imagenes en pantalla

        # Mostrar el título
        font = pygame.font.Font(font_path, 50)
        title_text = font.render("Break the Backroom", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 180))

        # Posición de los botones
        button_x, button_y = SCREEN_WIDTH // 2, 320

        # Dibujar los botones
        for i, text in enumerate(["Iniciar Juego", "Info", "Salir"]):
            font = pygame.font.Font(normal, 50)
            text_color = WHITE
            if button_x - font.size(text)[0] // 2 <= pygame.mouse.get_pos()[0] <= button_x + font.size(text)[0] // 2 and button_y + (i * 70) - font.size(text)[1] // 2 <= pygame.mouse.get_pos()[1] <= button_y + (i * 70) + font.size(text)[1] // 2:
                text_color = RED
            draw_text(text, font, text_color, screen, button_x, button_y + (i * 70))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, text in enumerate(["Iniciar Juego", "Info", "Salir"]):
                    font = pygame.font.Font(normal, 30)
                    if button_x - font.size(text)[0] // 2 <= event.pos[0] <= button_x + font.size(text)[0] // 2 and button_y + (i * 70) - font.size(text)[1] // 2 <= event.pos[1] <= button_y + (i * 70) + font.size(text)[1] // 2:
                        if text == "Iniciar Juego":
                            return "game"
                            sound_menu.stop()
                        elif text == "Info":
                            return "info"
                        elif text == "Salir":
                            pygame.quit()
                            sys.exit()
# Pantalla de información
def show_info():
    info_text = (
        "Break The Backroom es un juego 2D con arte pixel (a excepción del menú) con vista Top-Down,",
        "en donde controlamos a Max, nuestro protagonista, el cual mediante un sueño logra quedarse atrapado",
        "en un espacio liminal sin razón aparente. Este lugar no existe dentro de nuestra dimensión, y es un lugar",
        "en el que muy raramente los humanos logran entrar.",
        "En este juego, trataremos de escapar de este lugar mediante exploración y sobrevivir a enemigos múltiples",
        "que se encuentran en el mapa. Contará con un solo nivel y un solo mapa en su versión Beta."
    )

    while True:
        screen.blit(background_img, (0, 0))

        # Mostrar el texto de información
        font = pygame.font.Font(normal, 20)
        text_color = WHITE
        for i, line in enumerate(info_text):
            draw_text(line, font, text_color, screen, SCREEN_WIDTH // 2, 160 + i * 50)

        # Mostrar el botón de volver al menú
        font = pygame.font.Font(normal, 30)
        if SCREEN_WIDTH // 5.5 - font.size("Volver")[0] // 2 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 5.5 + font.size("Volver")[0] // 2 and SCREEN_HEIGHT - 75 - font.size("Volver")[1] // 2 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 75 + font.size("Volver")[1] // 2:
            text_color = RED
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "menu"
        else:
            text_color = WHITE
        draw_text("Volver", font, text_color, screen, SCREEN_WIDTH // 5.5, SCREEN_HEIGHT - 75)

        # Mostrar el botón de controles
        if SCREEN_WIDTH - 190 - font.size("Controles")[0] // 2 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH - 190 + font.size("Controles")[0] // 2 and SCREEN_HEIGHT - 75 - font.size("Controles")[1] // 2 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 75 + font.size("Controles")[1] // 2:
            text_color = RED
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "controls"
        else:
            text_color = WHITE
        draw_text("Controles", font, text_color, screen, SCREEN_WIDTH - 190, SCREEN_HEIGHT - 75)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Pantalla de controles
def show_controls():
    controls_text ="Flechitas para moverse\n\n E para interactuar con objetos\n\n F para abrir puertas\n\n Espacio para disparar(solo si obtenes el poder)"

    while True:
        screen.blit(background_img, (0, 0))
        # Mostrar el texto de controles
        font = pygame.font.Font(normal, 25)
        text_color = WHITE
        text_lines = controls_text.split("\n")
        for i, line in enumerate(text_lines):
            draw_text(line, font, text_color, screen, SCREEN_WIDTH // 2, 150 + i * 30)

        # Mostrar el botón de volver a información
        font = pygame.font.Font(normal, 30)
        if SCREEN_WIDTH // 2 - font.size("Volver")[0] // 2 <= pygame.mouse.get_pos()[0] <= SCREEN_WIDTH // 2 + font.size("Volver")[0] // 2 and SCREEN_HEIGHT - 100 - font.size("Volver")[1] // 2 <= pygame.mouse.get_pos()[1] <= SCREEN_HEIGHT - 100 + font.size("Volver")[1] // 2:
            text_color = RED
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return "info"
        else:
            text_color = WHITE
        draw_text("Volver", font, text_color, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def show_dialogue():
    current_dialogue_part = 0
    advance_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 150, 100, 40)
    advance_button_color = WHITE
    while True:
        screen.blit(background_img, (0, 0))

        if current_dialogue_part < len(dialogue_parts):
            font = pygame.font.Font(normal, 20)
            for i, line in enumerate(dialogue_parts[current_dialogue_part]):
                draw_text(line, font, WHITE, screen, SCREEN_WIDTH // 2, 250 + i * 50)
            
            # Detectar si el mouse está sobre el botón
            if advance_button_rect.collidepoint(pygame.mouse.get_pos()):
                advance_button_color = RED
            else:
                advance_button_color = WHITE
                
            font = pygame.font.Font(normal, 25)
            draw_text("Avanzar", font, advance_button_color, screen, advance_button_rect.centerx, advance_button_rect.centery)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if advance_button_rect.collidepoint(event.pos):
                    current_dialogue_part += 1
                    if current_dialogue_part >= len(dialogue_parts):
                        return "game"                
dialogue_parts = [
    [
        "“Hay simples coincidencias en este mundo que estan mas allá de la comprensión humana,",
        " y aquel que se enfrente a ellas debe adaptarse para lograr volver a lo cotidiano, de lo contrario,",
        " todo terminara de forma catastrófica”"
    ],
    [
        "“Lamentablemente para un ser humano mortal como tu, llegaste a esta coincidencia.",
        " Un sueño o un viaje a un plano inexistente del que vivimos,",
        " debes saber como salir de este lugar antes de que sea muy tarde y tu mente no pueda procesar un lugar como este.”"
    ],
    [
        "NOTA DE UN VIAJERO DESCONOCIDO :",

        "“Si alguien esta leyendo esto, agarra las llaves y acaba con esa cosa,",
        " los jarrones son la respuesta, hay algunos vacios por que necesitaba abrir la puerta."
    ],
    [
        "PD : He tratado de acabar con el pero cada vez mi mente desfigura todo a mi alrededor",
        " incluyendo a esa cosa, no creo soportar mucho mas. ",
        "Cuando entres por esa puerta utiliza las pocas fuerzas que te quedan para poder defenderte,",
        "confia en mi. "
    ],
    [
        "Si hay algo que aprendi de este sitio es que todo depende de que tanta voluntad mental tengamos.",
        "Por favor no pierdas tiempo tratando de encontrarme, es muy tarde,",
        " la muerte es una regalo de dios antes que estar un segundo mas en este lugar”"
    ]
]
          
def show_game():
    global in_game, doors, sound_llave, sound_fondo, sound_menu
    in_game=True
    sound_menu.stop()  # Detener completamente el sonido del menú
    sound_fondo.play(-1)
    background_img = pygame.image.load("asset/sin nombre.png")
    projectiles = pygame.sprite.Group()
    projectile_timer = pygame.time.get_ticks()
    projectile_cooldown = 2500  # Tiempo en milisegundos (2.5 segundos)
    player_can_shoot = True
    show_key_message = False
    player = Player(SCREEN_WIDTH // 7, SCREEN_HEIGHT // 4)
    paredes = pygame.sprite.Group()
    camera_x, camera_y = 0, 0
    crab_boss = CrabBoss()
    crab_boss.projectiles = pygame.sprite.Group()
    player_passed_super_door = False
    nonollave=False
    block = Block(1506, 1057)
    lista_paredes = [
        (736, 38.67, 239, 75),(682.33, 126.67, 78.67,115),(426.67, 40, 266.67, 75),(430, 265.33, 266, 32),(810.67,170,106.67,126.67),
        (972,38.63,21.33,365.33),(776,396,237.33,18.67),(779,396,21.33,122.67),(299,134.67,140,69),(42.67,40,265.33,68),
        (160,230.67,150,68),(29.33,40,25,586.67),(29.33,618.67,153.33,22.67),(161.33,620,18,100),(167.33,716,804,25.33),
        (973.33,516,18.67,208),(496,501.33,2.67,213.33),(396,490.67,102.67,34),(299.67,538.67,108,48),(235,489.33,73.33,35),
        (175,425.33,70.67,35),(175,472,4,42.67),(106.67,521.5,73,32),(105,353,7.67,160),(236,394.67,74.67,22.67),
        (295,366.67,174,22.67),(448,384,16,49.33),(454.67,427,47,57.33),(585,389.33,117,34),(585,389.33,8,129.33),(585,520,367,68.67),
        (45,804,933,70),(971,875,21,202),(683,1067,309,20),(683,934,5,153),(270,934,421,37),(270,938,6,217),(139.33,939.67,73,95),(31,881,22,610),
        (107,1100,168,93),(107,1201,73,219),(179,1356,192,68),(369,1192.33,192,35),(44,1482.67,932,21),(970,1258,7,228),(463,1314,6,176),(366,1236,7,41),
        (554,1194,7.67,155),(458,1026,6,165),(554,1352,108,33),(655,1257,6.67,87),(655,1192,321,65),(683,1068,8,124),(1060,116,50,285),(1069,39,899,69),
        (1963,117,16,285),(1739,172,140,129),(1196,172,136,129),(1638,200,20,91),(1802,394.67,193,257),(1418,426,233,5),(1416,425,10,172),(1645,422,7,160),(1417,582,236,40),
        (1098,394.67,170,257),(1088,657.67,20,835),(1962,657.67,20,835),(1750,1481,211,22.62),(1109,1482,211,22.62),(1450,1322,171,41),
        (1386,1355,299,77),(1322,1419,427,77),(1227,1128,618.67,67),(1230,904.99,103,65),(1230,904.02,7,220),(1833.67,904.02,8,220),
        (1737.67,904.99,103.58,65),(1326.88,744.18,419.58,65.15),(1326.33,744.18,6.92,158.48),(1738.67,744.18,6.37,158.48)
    ]
    interactive_objects = pygame.sprite.Group()
    objects_positions = [
        (928, 128, True), (447, 544, True), (255, 129, True), (607, 1312, True),
        (192, 1216, True), (224, 1056, True), (1120, 1440, True), (1919, 1440, True),
        (641, 221, False), (129, 480, False), (608, 447, False), (640, 993, False),
        (416, 1151.33, False), (671, 1280.67, False), (1281, 865, False), (1762, 864.67, False)
        ]

    # Crear objetos interactivos y agregarlos al grupo de sprites
    for x, y, gives_key in objects_positions:
        interactive_object = InteractiveObject(x, y, gives_key)
        interactive_objects.add(interactive_object)
    screen.blit(background_img, (camera_x, camera_y)) 
    door_positions = [
    Door(832, 597,teleport_position=(816, 876)),
    Door(816, 876,teleport_position=(832, 597)),
    Door(767, 1281,teleport_position=(1505.42, 128.12)),
    Door(1505.42, 128.12,teleport_position=(767, 1281)),
    Door(1504,636,teleport_position=(1504,480)),
    Door(1504,520,teleport_position=(1504,636)),
    SuperDoor(1505, 1217, required_keys=8, teleport_position=(1504, 1058)),
    ]

    doors = []
    for i in range(len(door_positions)):
        door = door_positions[i]
        doors.append(door)

    for x, y, width, height in lista_paredes:
        pared = Pared(x, y, width, height)
        paredes.add(pared)
    # Coordenadas de la cámara
    camera_x, camera_y = 0,0 
    trampas = pygame.sprite.Group()
    trampas_positions = [
    (256, 322), (64, 482),(448,322),(511,449),(545,449),(511,545) ,(545,545),
    (64,386),(288,900),(64,1124),(64,1380),(384,1412),(417,1412),(640,900),
    (447,996)# Ejemplos de posiciones de trampas
    ]

    for x, y in trampas_positions:
        trampa = Trampa(x, y)
        trampas.add(trampa)   
    pygame.display.flip()
        
    while True:

        camera_x = SCREEN_WIDTH // 2 - player.rect.x
        camera_y = SCREEN_HEIGHT // 2 - player.rect.y
        camera_x = min(0, camera_x)  # Mover hacia la izquierda
        camera_x = max(SCREEN_WIDTH - background_img.get_width(), camera_x)  # Mover hacia la derecha
        camera_y = min(0, camera_y)  # Mover hacia arriba
        camera_y = max(SCREEN_HEIGHT - background_img.get_height(), camera_y)  # Mover hacia abajo
        screen.blit(background_img, (camera_x, camera_y)) 
        if crab_boss.health > 0:
         crab_boss.update(player)    
         if crab_boss.returning_to_center:
            crab_boss.move_to_center()
         screen.blit(crab_boss.image, (crab_boss.rect.x + camera_x, crab_boss.rect.y + camera_y))
         pygame.draw.rect(screen, RED, (crab_boss.rect.x + camera_x, crab_boss.rect.y + camera_y - 10, 64, 5))
         pygame.draw.rect(screen, GREEN, (crab_boss.rect.x + camera_x, crab_boss.rect.y + camera_y - 10, crab_boss.health * 12.8, 5))

        else:
            feid.set_initial_bg(SCREEN_WIDTH,SCREEN_HEIGHT,True)
            pygame.quit()  

        for trampa in trampas.sprites():
            trampa.update()
            screen.blit(trampa.image, (trampa.rect.x + camera_x, trampa.rect.y + camera_y))
            trampa.activate(player) 
             
        for obj in interactive_objects.sprites():
            obj.update(player)
            obj_x_on_screen = obj.rect.x + camera_x
            obj_y_on_screen = obj.rect.y + camera_y
            screen.blit(obj.image, (obj_x_on_screen, obj_y_on_screen))

            if obj.interactable and pygame.sprite.collide_rect(player, obj):
                font = pygame.font.Font(normal,30)
                draw_text("Presiona 'E' para interactuar", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 100)
                if pygame.key.get_pressed()[pygame.K_e]:
                    obj.interact(player)

        player.draw(screen, camera_x, camera_y)
        player.update() 
        # Mostrar el número de llaves recolectadas
        font = pygame.font.Font(normal, 25)
        draw_text(f"Llaves: {player.keys}", font, WHITE, screen, 985, SCREEN_HEIGHT - 580)  
        font = pygame.font.Font(normal, 25)
        draw_text(f"Vidas: {player.lives}", font, WHITE, screen, 985, SCREEN_HEIGHT - 550)
        for door in doors:
            if door.rect.colliderect(player.rect):
                font = pygame.font.Font(normal, 20)
                draw_text("Presiona 'F' para interactuar con la puerta", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 100)
            
        for door in doors:
            if isinstance(door, SuperDoor) and door.rect.collidepoint(player.rect.center):
                nonollave=True             
            if block.rect.colliderect(player.rect) :
                player_passed_super_door= True
            if player_passed_super_door:
                if player_can_shoot:
                    font = pygame.font.Font(normal, 20)
                    draw_text("Dispare con espacio", font, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 70)
                else:
                    font = pygame.font.Font(normal, 20)
                    draw_text("Espere para disparar", font,WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5 + 70)
            if nonollave == True and player.keys < 8:
                show_key_message = True
            if show_key_message and door.rect.colliderect(player.rect):
                font = pygame.font.Font(normal, 20)
                draw_text("No tienes suficientes llaves, vuelve cuando tengas 8.", font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.3 + 100)
            show_key_message=False

        for projectile in crab_boss.projectiles.sprites():
            projectile.update()
            screen.blit(projectile.image, (projectile.rect.x + camera_x, projectile.rect.y + camera_y))
            if pygame.sprite.collide_rect(projectile, player):
                player.subtract_life()
                player.rect.x=1507
                player.rect.y=1084
                crab_boss.projectiles.remove(projectile)

            if projectile.creation_time + 1000 < pygame.time.get_ticks():
                crab_boss.projectiles.remove(projectile)
               
        for projectile in projectiles.sprites():
            projectile.update()
            screen.blit(projectile.image, (projectile.rect.x + camera_x, projectile.rect.y + camera_y))
            if pygame.sprite.collide_rect(projectile, crab_boss):
                crab_boss.health -= 1
                projectiles.remove(projectile)
            if pygame.time.get_ticks() - projectile.creation_time >= 1000:  # 1000 milisegundos = 1 segundo
                projectiles.remove(projectile)
            
        if player.lives <= 0:
            show_game_over_screen = show_game_over()
            return show_game_over_screen 

        pygame.display.flip()     
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not player_can_shoot and pygame.time.get_ticks() - projectile_timer >= projectile_cooldown:
                 player_can_shoot = True
            if pygame.sprite.spritecollide(player, paredes, False):
                player.move("idle",paredes)
            elif event.type == pygame.KEYDOWN:
                # Iniciar el movimiento del jugador en las cuatro direcciones
                if event.key == pygame.K_UP:
                    player.moving_up = True
                elif event.key == pygame.K_DOWN:
                    player.moving_down = True
                elif event.key == pygame.K_LEFT:
                    player.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    player.moving_right = True
                elif event.key == pygame.K_ESCAPE:  # Detectar si se presiona la tecla "ESC"
                    return "menu"  # Regresar al menú principal
                elif event.key == pygame.K_e:  # Detectar si se presiona la tecla 'E'
                    for obj in interactive_objects.sprites():
                        if obj.interactable:
                            obj.interact(player)              
                if event.key == pygame.K_f:
                    for door in doors:
                        if door.rect.colliderect(player.rect):
                            door.interact(player)
                            break
                        
                if event.key == pygame.K_SPACE and player_can_shoot and player_passed_super_door:
                    new_projectile = Projectile(player.rect.centerx, player.rect.centery)
                    projectiles.add(new_projectile)
                    player_can_shoot = False
                    projectile_timer = pygame.time.get_ticks()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.moving_up = False
                elif event.key == pygame.K_DOWN:
                    player.moving_down = False
                elif event.key == pygame.K_LEFT:
                    player.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    player.moving_right = False

        if player.moving_up:
            player.move("up", paredes)
        elif player.moving_down:
            player.move("down", paredes)
        elif player.moving_left:
            player.move("left", paredes)
        elif player.moving_right:
            player.move("right", paredes)
            
        else:
            player.move("idle", paredes)
   
def show_game_over():
    for count in range(5, 0, -1):
        fonti = pygame.font.Font(normal, 80)
        font = pygame.font.Font(normal,50)
        game_over_text = fonti.render("¡Has Perdido!", True, WHITE)
        screen.blit(background_img, (0, 0))  # Dibujar el fondo
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 180))  # Dibujar el texto
        count_text = font.render(f"Volverás en {count} ...", True, WHITE)
        screen.blit(count_text, (SCREEN_WIDTH // 2 - count_text.get_width() // 2, 320))
        pygame.display.flip()
        pygame.time.wait(1000)  

    pygame.time.wait(1000) 
    
    return "menu"
def main():
    current_screen = "menu"   
    clock = pygame.time.Clock()

    while True:
        if current_screen == "menu":
            current_screen = show_menu()
        elif current_screen == "game":
            current_screen = show_game()
        elif current_screen == "info":
            current_screen = show_info()
        elif current_screen == "controls":
            current_screen = show_controls()
        else:
            pygame.quit()
            sys.exit()
        clock.tick(60)
        if not in_game:
            sound_fondo.stop()
        if current_screen == "game":  
            current_screen = show_dialogue()

if __name__ == "__main__":
    main()