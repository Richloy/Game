'''Adding player movement'''

import pygame, os, MySQLdb
from pyConnect import *
from tklogin import *

#Colours (R, G, B)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
dataB = pyConnect()

class Game:

    def main(self):
        
        clock = pygame.time.Clock()
        zoom_img = pygame.image.load(".\images\\zoom_in.png")
        bg = pygame.image.load(".\images\\bgnd.png")
        bdr = pygame.image.load(".\images\\border.png")
        lvl = pygame.image.load(".\images\\cpark1.png")
        lvl_x = 80
        lvl_y = 180
        zoom = False
        #menu state variables
        opening_menu = False
        closing_menu = False
        menu_open = False
        login = True
        image = pygame.image.load(".\images\\menu_arrow.png")
        l_menu = Menu()
        player = Player()
        running = True
        #Create Sprite Groups
        b_group = pygame.sprite.Group()
        p_group = pygame.sprite.Group()
        p_group.add(player)
        
        
        #Game Loop
        while running:
            clock.tick(60) #Refresh screen
            screen.blit(bg, (0, 0))
            screen.blit(lvl, (lvl_x, lvl_y))
            screen.blit(bdr, (0, 0))
            screen.blit(zoom_img, (775, 25))
            
            #Open/Close menu
            if opening_menu:
                if (l_menu.menu_x < 0):
                    l_menu.open_l_menu()
                    menu_open = True
                    image = pygame.image.load(".\images\\menu_arrow2.png")
            if closing_menu:
                if (l_menu.menu_x > -200):
                    l_menu.close_l_menu()
                    menu_open = False
                    image = pygame.image.load(".\images\\menu_arrow.png")
            l_menu.show_l_menu()
            screen.blit(image, (0, 280))
            
            p_group.draw(screen)
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
                    move_x, move_y = pygame.mouse.get_rel()
                    print (move_x)
                    print (move_y)
                    if (800 < x < 850 and 50 < y < 100):
                        if not zoom:
                            zoom = True
                            lvl = pygame.transform.scale(lvl, (1544, 650))
                            zoom_img = pygame.image.load(".\images\\zoom_out.png")
                            lvl_x = -80
                            lvl_y = -80
                        else:
                            zoom = False
                            lvl = pygame.transform.scale(lvl, (772, 325))
                            zoom_img = pygame.image.load(".\images\\zoom_in.png")
                            lvl_x = 80
                            lvl_y = 180
                    if not menu_open:
                        if (x < 55 and 335 > y > 280):
                            opening_menu = True
                            closing_menu = False
                    if menu_open:
                        if (x < 55 and 335 > y > 280):
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
            if zoom:
                if pygame.mouse.get_pressed()[0]:
                    if (812 < x < 837 and 25 < y < 50):
                        lvl_y += 10 #Move up
                    if (812 < x < 837 and 100 < y < 125):
                        lvl_y -= 10 #Move down
                    if (775 < x < 800 and 62 < y < 87):
                        lvl_x += 10 #Move left
                    if (850 < x < 875 and 62 < y < 87):
                        lvl_x -= 10 #Move right
                            
    
class Menu:

    def __init__(self):
        self.menu_bgnd = pygame.image.load(".\images\\menu_bgnd2.png")
        self.left_menu = pygame.Surface((200, 600))
        self.image2 = pygame.image.load(".\images\\menu_arrow2.png")
        self.left_menu.blit(self.menu_bgnd, (0, 0))
        #self.left_menu.blit(self.image2, (0, 280))
        self.menu_x = -200
        self.menu_y = 0
        self.goals = pygame.image.load(".\images\\goals2.png")
        self.left_menu.blit(self.goals, (30, 20))
        
    def open_l_menu(self):
        self.menu_x += 4

    def close_l_menu(self):
        self.menu_x -= 4
    
    def show_l_menu(self):
        screen.blit(self.left_menu, (self.menu_x, self.menu_y))
        #screen.blit(self.image2, (0, 280))

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.player = dataB.get_player()
        #Create the player image
        self.image = pygame.image.load(".\images\\"+self.player)
        self.rect = self.image.get_rect()
        self.rect.x = 565 #Start Position for Ball on x-axis
        self.rect.y = 205 #Start Position for Ball on y-axis

        print(self.rect.x, self.rect.y, self.player)
        
if __name__ == '__main__':
    os.environ["SDL_VIDEO_CENTERED"] = "3" #Sets up for center of OS display
    pygame.init() #Initalise Pygame
    screen = pygame.display.set_mode((900, 600), pygame.NOFRAME) #Create a screen for game
    Game().main() #Create game and run main
