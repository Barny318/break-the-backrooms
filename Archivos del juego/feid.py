import pygame

def fade(surface, width, height):
    # fade = pygame.Surface((width, height))
    # fade.fill((0, 0, 0))
    fade = pygame.image.load("asset/win.png").convert_alpha()
    fade = pygame.transform.scale (fade, (width, height))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redraw_window(surface, width, height)
        surface.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(1)
    for alpha in range(0, 300):
        fade.set_alpha(300-alpha)
        redraw_window(surface, width, height)
        surface.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
        
def redraw_window(surface, width, height):
    surface.fill((0, 0, 0))
    
def set_initial_bg(def_width, def_height, full_screen):
    win = pygame.display.set_mode((def_width, def_height))
    redraw_window(win, def_width, def_height)
    print("starting init animation")
    fade(win, def_width, def_height)
    pygame.display.update  
    print("Ending init animation")
    return