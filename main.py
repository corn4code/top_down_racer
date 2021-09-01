import pygame

# get the speed in both ways with circle --> x+y only <= 3 
# like wheel for movement in mobile games

def draw_car(new_car_image, rotation_angle):
    # pygame.draw.rect(screen, (0, 0, 255), (car_x, car_y, 50, 50))
    new_car_image = pygame.transform.rotate(new_car_image, rotation_angle).convert_alpha()
    rect = new_car_image.get_rect()
    rect.center = (car_x, car_y)
    screen.blit(new_car_image, rect)


# def draw_rotation_car(new_car_image):
#     new_car_image = pygame.transform.rotate(new_car_image, 60)
#     rect = car_image.get_rect()
#     return rect, new_car_image


car_x = 960
car_y = 585
window_width = 1920
window_height = 1030
size = [window_width, window_height]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_surface = pygame.image.load("track1.png").convert()
car_image = pygame.transform.rotozoom(pygame.image.load("car-white.png"), 0, 0.15).convert_alpha()
running = True
new_car_image = car_image
rotation_angle = 0

while running:

    # start movement of car
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        car_x += 1.25
        car_y -= 1.25
        if rotation_angle < 90:
            rotation_angle += 0.3
        else:
            pass
        # draw_rotation_car(car_image)
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        car_x -= 1.25
        car_y -= 1.25
        # draw_rotation_car(car_image)
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        car_x += 1.25
        car_y += 1.25
        # draw_rotation_car(car_image)
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        car_x -= 1.25
        car_y += 1.25
        # draw_rotation_car(car_image)
    elif keys[pygame.K_UP]:
        car_y -= 2.5
    elif keys[pygame.K_DOWN]:
        car_y += 2.5
    elif keys[pygame.K_RIGHT]:
        car_x += 2.5
        if rotation_angle != 0:
            if rotation_angle > -0.1:
                rotation_angle -= 0.3
            if rotation_angle < 0.1:
                 rotation_angle += 0.3
    elif keys[pygame.K_LEFT]:
        car_x -= 2.5
        
    # end movement of car
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                running = False
            if event.key == pygame.K_SPACE:
                print(f"car x: {car_x} car y: {car_y}")


        

    screen.blit(bg_surface, (0, 0))

    draw_car(new_car_image, rotation_angle)
    pygame.display.update()
    clock.tick(144)

pygame.quit()
