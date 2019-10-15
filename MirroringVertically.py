import pygame
pygame.init()

main_window = pygame.display.set_mode((550, 700))
picture = pygame.image.load("MyGuy.jpg").convert()


def mirror_vertical():
    width = picture.get_width()
    height = picture.get_height()
    mirror_point = int(height / 2)
    for x in range(0, width):
        for y in range(0, mirror_point):
            top_pixel = picture.get_at((x, height - y - 1))
            picture.set_at((x, y), top_pixel)


mirror_vertical()
pic = pygame.transform.scale(picture, (550, 700))
main_window.blit(pic, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
