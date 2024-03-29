import pygame
pygame.init()

#window size
window = pygame.display.set_mode((900, 720))
clock = pygame.time.Clock()
#credit is needed
pygame.display.set_caption("Entity Generator by Oskar Korpysa")

back_colour = (255,255,255)
window.fill(back_colour)

choice = str(input("Choose your opponent:")).lower()

#Here i list the location of the images
Wizard = pygame.image.load(r'Characters\Wizard.png')
Archer = pygame.image.load(r'Characters\Archer.png')
Healer = pygame.image.load(r'Characters\Healer.png')
Mage = pygame.image.load(r'Characters\Mage.png')
Swordsmaster = pygame.image.load(r'Characters\Swordsmaster.png')
Tank = pygame.image.load(r'Characters\Tank.png')


#this part is to prevent the window from closing instantly
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    if choice == "wizard":
        window.blit(Wizard, (450, 400))
    elif choice == "archer":
        window.blit(Archer, (450, 400))
    elif choice == "mage":
        window.blit(Mage, (450, 400))
    elif choice == "tank":
        window.blit(Tank, (450, 400))
    elif choice == "healer":
        window.blit(Healer, (450, 400))
    pygame.display.update()

pygame.quit()
