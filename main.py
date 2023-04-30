import pygame

# инициализация Pygame
pygame.init()

# настройки окна
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fireboy & Watergirl")

# загрузка графических ресурсов
fireboy_image = pygame.image.load("fireboy.png")
watergirl_image = pygame.image.load("watergirl.png")
# background_image = pygame.image.load("background.jpg")

# настройки персонажей
fireboy_x = 50
fireboy_y = 50
watergirl_x = 100
watergirl_y = 50
fireboy_speed = 1
watergirl_speed = 1

# главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # перемещение Fireboy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        fireboy_x -= fireboy_speed
    if keys[pygame.K_RIGHT]:
        fireboy_x += fireboy_speed
    if keys[pygame.K_UP]:
        fireboy_y -= fireboy_speed
    if keys[pygame.K_DOWN]:
        fireboy_y += fireboy_speed

    # перемещение Watergirl
    if keys[pygame.K_a]:
        watergirl_x -= watergirl_speed
    if keys[pygame.K_d]:
        watergirl_x += watergirl_speed
    if keys[pygame.K_w]:
        watergirl_y -= watergirl_speed
    if keys[pygame.K_s]:
        watergirl_y += watergirl_speed

    # отрисовка игровых объектов
    # window.blit(background_image, (0, 0))
    window.blit(fireboy_image, (fireboy_x, fireboy_y))
    window.blit(watergirl_image, (watergirl_x, watergirl_y))

    # обновление экрана
    pygame.display.update()

# выход из Pygame
pygame.quit()
