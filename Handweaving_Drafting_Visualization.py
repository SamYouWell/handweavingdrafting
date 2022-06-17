from re import S
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
light_blue_white = (204, 255, 255)
dark_gray = (128,128,128)


#Creaing Title: images are just place holders for now! I'm gonna make my own images.
pygame.display.set_caption("Drafting_Visualization")
icon = pygame.image.load("hand.PNG")
pygame.display.set_icon(icon)
#loading or declaring the background:
background = pygame.image.load("image0.PNG")
screen_width = 3400
screen_height = 2025
screen  = pygame.display.set_mode((screen_width,screen_height))
window = pygame.display.get_surface()
area = window.get_rect()

class Warp(pygame.sprite.Sprite):
    def __init__(self,x, width, length) -> None:
        super().__init__()
        self.image = pygame.image.load("square.PNG")
        self.image = pygame.transform.scale(self.image, (4,4))
        self.rect = self.image.get_rect()
        self.thread_num = width
        self.length = length
        self.rect.topleft = (x,0)
        self.spacing = x
        self.threads = []
        for i in range(self.thread_num):
            warp_thread = pygame.Rect(self.spacing, 0, 5, self.length)
            self.spacing += 10
            self.threads.append(warp_thread)
    
    #Drawing warp pattern:        
    def warping(self):
        for i, thread in enumerate(self.threads):
            if i % 1 == 0:                  #LOOK DOWN ON THE WEFT CLASS TO GET THE IDEA.
                pygame.draw.rect(screen, red, thread)
            else: pygame.draw.rect(screen, black, thread)
        
    def update(self):
        self.warping()
        
class Weft(pygame.sprite.Sprite):
    def __init__(self,x, width, length) -> None:
        super().__init__()
        self.image = pygame.image.load("square.PNG")
        self.image = pygame.transform.scale(self.image, (4,4))
        self.rect = self.image.get_rect()
        self.thread_num = width
        self.color = white
        self.length = length
        self.rect.topleft = (x,6)
        self.row = 6    #This is the sett value
        self.spacing = x
        self.plain_thread = []
            
    def plain_weave(self):
    
        for i in range(self.length):
            if i%2 == 0:
              self.spacing += 5
            else:
                start = pygame.Rect(self.spacing, self.row*i, 10, 5)
                self.plain_thread.append(start)
                self.spacing += 15
        
            for j in range(self.thread_num):
                weft_over = pygame.Rect(self.spacing, self.row*i, 15, 5)
                self.plain_thread.append(weft_over)
                self.spacing += 20
            
            if i%2 == 0:
                end = pygame.Rect(self.spacing, self.row*i, 10, 5)
                self.plain_thread.append(end)
    
            #Starting new row:    
            self.spacing = 10
        
        #Drawing pattern out:    
        for i, thread in enumerate(self.plain_thread):
            if thread.top % 6==0:     #Keep in mind that thread.top % 6 == 0 is ALWAYS True for every row. Note: these values change with every sett: e.g. if sett value is 5 rather than 6, then 5==0 would always be True 
                self.color = black                              #  8==2               ,   5==0(-4) or 16==4 , 4==0 (inverted 4==2)    , replacing % with & yeilds double stripes
            else: self.color = red                              #  8==4 (shifted ^^^) ,   5==0(-4) or 34==8 , 5==0 (shift up to 5==4) ,   e.g. thread.top & 4 == 0

            pygame.draw.rect(screen, self.color, thread)
        
    def update(self):
        self.plain_weave()

        
warp_threads = Warp(10,242, 820)
weft_thread = Weft(10, 120, 137)

warp_ends = pygame.sprite.Group()
weft_ends = pygame.sprite.Group()

warp_ends.add(warp_threads)
weft_ends.add(weft_thread)

#Running App:
running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    #Keyboard controlling AKA event handling:
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    warp_ends.update()
    weft_ends.update()
    weft_ends.draw(screen)
    warp_ends.draw(screen)         
    pygame.display.flip()   #another way to refresh screen sort of like pygame.display.update()
    clock.tick(60)  #frame rate
    
    
    #Todo list:
    #Make inputs more user friendly and automatic (user not having to directly change code and using more familar patterns (e.g. I want this color in tiger tooth pattern))
    #Find ways to include weave structure and not change color patterns
