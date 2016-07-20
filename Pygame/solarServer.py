import pygame
import sys
import socket
import threading
from Tkinter import *

s = socket.socket()
# SO_REUSEADDR is used to make the port reusable
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = socket.gethostname()
port = 5007

s.bind((host, port))
s.listen(5)

c, addr = s.accept()
print("connection from:", addr)

#while True:
data = c.recv(1024)

##########
pygame.init()

# RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
dsblue = (0, 191, 255)
hyellow = (255, 255, 102)

# surface
gameDisplay = pygame.display.set_mode((800, 600))

# Title of the window
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit = False

# GameLoop
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            #sys.exit()
        # prints all events like mouseclick,scroll etc.
        #print(event)

    # fill bg with white
    gameDisplay.fill(dsblue)

    if(data == '1'):
        pygame.draw.circle(gameDisplay, white, [400,300], 100)
    if(data == '2'):
        pygame.draw.ellipse(gameDisplay, white, [400, 300, 100, 100])
        pygame.draw.ellipse(gameDisplay, black, [400, 300, 95, 100])
    if(data == '3'):
        pygame.draw.ellipse(gameDisplay, hyellow, [400, 300, 100, 100])
        pygame.draw.ellipse(gameDisplay, black, [400, 300, 97, 100])


    #pygame.draw.rect(gameDisplay, red, [400, 300, 10, 100])
    #gameDisplay.fill(red, rect=[200, 200, 50, 50])

    pygame.display.update()


pygame.quit()
quit()
