import pygame

# get the speed in both ways with circle --> x+y only <= 3 
# like wheel for movement in mobile games

def draw_car():
    pygame.draw.rect(screen, (0, 0, 255), (car_x, car_y, 90, 50))

def draw_rotation_car():
    
    pass


car_x = 50
car_y = 40
window_width = 1920
window_height = 1030
size = [window_width, window_height]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_surface = pygame.transform.scale2x(pygame.image.load("bg.png").convert())
running = True
while running:

    # start movement of car
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        car_x += 1.5
        car_y -= 1.5
        draw_rotation_car()
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        car_x -= 1.5
        car_y -= 1.5
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        car_x += 1.5
        car_y += 1.5
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        car_x -= 1.5
        car_y += 1.5
    elif keys[pygame.K_UP]:
        car_y -= 3
    elif keys[pygame.K_DOWN]:
        car_y += 3
    elif keys[pygame.K_RIGHT]:
        car_x += 3
    elif keys[pygame.K_LEFT]:
        car_x -= 3
    # end movement of car
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                running = False


        

    screen.blit(bg_surface, (0, 0))

    draw_car()
    pygame.display.update()
    clock.tick(144)

pygame.quit()
