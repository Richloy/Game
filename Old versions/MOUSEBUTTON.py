import pygame

def main():
    pygame.init()

    size = width, height = 800,700
    backgroundColor = [0, 0, 255]


    screen = pygame.display.set_mode(size)

    screen.fill(backgroundColor)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if pygame.mouse.get_pressed()[0]:
                try:
                    print (event.pos)
                except AttributeError:
                    pass
main()
