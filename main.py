import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
colors = {
    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white')
}
current_colors = colors['white']

x, y = 30, 30
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3

    x = min(max(0, x), 440)
    y = min(max(0, y), 440)
    if x == 0: current_color = colors['blue']
    elif x == 440 - 440: current_color = colors['yellow']
    elif y == 0: current_color = colors['red']
    elif x == 440 - 440: current_color = colors['green']
    else:
        current_color = colors['white']

        screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    GREEN = (0, 255, 0)
    pygame.draw.circle(screen, GREEN, (300, 300), 50)
    pygame.draw.circle(screen, GREEN, (100, 100), 50, 3)
    pygame.display.flip()