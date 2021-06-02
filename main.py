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
    # speed_x += acceleration_x
    # speed_y += acceleration_y
    # if speed_x > 3:
    #     speed_x = 3
    # if speed_x < -3:
    #     speed_x = -3
    # if speed_y > 3:
    #     speed_y = 3
    # if speed_y < -3:
    #     speed_y = -3
    # car_x += speed_x
    # car_y += speed_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                # acceleration_y = -0.1
                car_y -= 10
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                # acceleration_y = 0.1
                car_y += 10
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                # acceleration_x = 0.1
                car_x += 10
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                # acceleration_x = -0.1
                car_x -= 10
            # if event.key == pygame.K_SPACE:
                # speed_y = 0
                # speed_x = 0
                # acceleration_y = 0
                # acceleration_x = 0

    screen.blit(bg_surface, (0, 0))

    draw_car()
    pygame.display.update()
    clock.tick(144)
    print(f"Speed x: {speed_x}; speed y: {speed_y}")
pygame.quit()
