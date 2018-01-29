# Snake Game Code Begins

import pygame
import sys
import random
import time

errors = pygame.init()

if errors[1]>0:
	print("(!) Had {0} initializing errors, exiting...".format(errors))
	sys.exit()
else:
	print("(+) PyGame successfully initialized")


playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake Game!')


red = pygame.Color(255,0,0)