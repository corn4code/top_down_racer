import pygame

# get the speed in both ways with circle --> x+y only <= 3 
# like wheel for movement in mobile games

def draw_car():
    pygame.draw.rect(screen, (0, 0, 255), (car_x, car_y, 50, 50))


acceleration_x = 0
speed_x = 0 + acceleration_x
acceleration_y = 0
speed_y = 0 + acceleration_y
car_x = 50
car_y = 40
car_movement_x = speed_x + car_x
car_movement_y = speed_y + car_y
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
        

    screen.blit(bg_surface, (0, 0))

    draw_car()
    pygame.display.update()
    clock.tick(144)

pygame.quit()
