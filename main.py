import pygame
import time
from World import World
pygame.init()
w=World(20,20)
w.drawrld()
while w.end==0:    
    w.turn()
    w.drawrld()
time.sleep(2)
      
    




