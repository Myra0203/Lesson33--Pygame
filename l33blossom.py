#importing the library
import pygame

#calling the inital function
pygame.init()

#screen size
width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("blossom")
character = pygame.image.load("gaming library/blossom.png") #loading image
#image2 = pygame.image.load("gaming library/spongebob.png")
#event of the game (template for every game):
run = True #If the user doesn't close the tab or click on the "x" button, the game will continue
while run:
    for i in pygame.event.get(): #get the event of the game
        if i.type == pygame.QUIT: #check the datatype of the event; whether the user clicked on quit
            pygame.quit() #use quit function to close the tab
    screen.blit(character, (20,-50))
    #screen.blit(image2,(200,200)) 
    pygame.display.update()
pygame.quit()
