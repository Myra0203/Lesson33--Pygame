#importing the library
import pygame

#calling the inital function
pygame.init()

#screen size
width = 500
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("blossom")

#event of the game:
run = True #If the user doesn't close the tab or click on the "x" button, the game will continue
while run:
    for i in pygame.event.get(): #get the event of the game
        if i.type == pygame.QUIT: #check the datatype of the event; whether the user clicked on quit
            pygame.quit() #use quit function to close the tab
    pygame.display.update()

