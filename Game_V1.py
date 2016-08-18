import pygame, os

#Colours (R, G, B)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Game:

    def main(self):
        
        clock = pygame.time.Clock()
        bg = pygame.image.load("bgnd.png")
        lvl = pygame.image.load("cpark1.png")
        #menu state variables
        opening_menu = False
        closing_menu = False
        menu_open = False
        image = pygame.image.load("menu_arrow.png")
        l_menu = Menu()
        running = True
        
        #Game Loop
        while running:
            clock.tick(60) #Refresh screen
            screen.blit(bg, (0, 0))
            screen.blit(image, (0, 280))
            screen.blit(lvl, (0, 0))
            #Open/Close menu
            if opening_menu:
                if (l_menu.menu_x < 0):
                    l_menu.open_l_menu()
                    menu_open = True
            if closing_menu:
                if (l_menu.menu_x > -200):
                    l_menu.close_l_menu()
                    menu_open = False
            l_menu.show_l_menu()
            
            pygame.display.flip() #Update(flip) display
            
            
            #Check for events 
            for event in pygame.event.get():
                pause = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #Escape key press
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p: #Pause game
                    pause = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if not menu_open:
                        if (x < 55 and 335 > y > 280):
                            opening_menu = True
                            closing_menu = False
                    else:
                        if x > 200 or (x < 55 and 335 > y > 280):
                            opening_menu = False
                            closing_menu = True
                        
                #Paused Game and event
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pause = False
                            running = False
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            pause = False
                            running = False
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                            pause = False
    
class Menu:

    def __init__(self):
        self.menu_bgnd = pygame.image.load("menu_bgnd.png")
        self.left_menu = pygame.Surface((200, 600))
        self.image2 = pygame.image.load("menu_arrow2.png")
        self.left_menu.blit(self.menu_bgnd, (0, 0))
        self.left_menu.blit(self.image2, (0, 280))
        self.menu_x = -200
        self.menu_y = 0
        self.goals = pygame.image.load("goals2.png")
        self.left_menu.blit(self.goals, (30, 20))
        
    def open_l_menu(self):
        self.menu_x += 4

    def close_l_menu(self):
        self.menu_x -= 4
    
    def show_l_menu(self):
        screen.blit(self.left_menu, (self.menu_x, self.menu_y))
        
if __name__ == '__main__':
    os.environ["SDL_VIDEO_CENTERED"] = "3" #Sets up for center of OS display
    pygame.init() #Initalise Pygame
    screen = pygame.display.set_mode((900, 600), pygame.NOFRAME) #Create a screen for game
    Game().main() #Create game and run main
