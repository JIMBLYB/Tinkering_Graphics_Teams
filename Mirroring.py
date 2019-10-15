import pygame
pygame.init()

main_window = pygame.display.set_mode((1100, 1400))
picture = pygame.image.load("MyGuy.jpg").convert()


def mirror_horizontal():
    width = picture.get_width()
    height = picture.get_height()
    mirror_point = int(width / 2)
    for y in range(0, height):
        for x in range(0, mirror_point):
            left_pixel = picture.get_at((x, y))
            picture.set_at((width - x - 1, y), left_pixel)


mirror_horizontal()
main_window.blit(picture, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
