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

#Colors

red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
brown = pygame.Color(165,42,42)

#FPS Controller (look into detail)
fpsController = pygame.time.Clock()

snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn = True

direction = 'RIGHT'
changeto = direction

#Game over function
score = 0;    

def gameOver():
	myFont = pygame.font.SysFont('monaco', 72)
	GOsurf = myFont.render('Game Over!', True, red)
	GOrect = GOsurf.get_rect()
	GOrect.midtop = (360, 15)
	playSurface.blit(GOsurf,GOrect) ##This too
	pygame.display.flip()  ##Discuss this in detail
	showScore(2)
	time.sleep(1)
	pygame.quit()	#pygame exit
	sys.exit() 	#console exit

def showScore(choice=1):
	sFont = pygame.font.SysFont('monaco', 24)
	Ssurf = sFont.render('Score: {0}'.format(score), True, black)
	Srect = Ssurf.get_rect()
	if choice == 1:
		Srect.midtop = (80, 10)
	else:
		Srect.midtop = (360, 120)

	playSurface.blit(Ssurf, Srect)
	pygame.display.flip()

# Main Logic

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_RIGHT or event.key == ord('a'):
				changeto = 'LEFT'
			if event.key == pygame.K_RIGHT or event.key == ord('s'):
				changeto = 'DOWN'
			if event.key == pygame.K_RIGHT or event.key == ord('w'):
				changeto = 'UP'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(QUIT))
			
			
	if changeto == 'RIGHT' and not direction == 'LEFT':
		direction = 'RIGHT'
	if changeto == 'LEFT' and not direction == 'RIGHT':
		direction = 'LEFT'
	if changeto == 'UP' and not direction == 'DOWN':
		direction = 'UP'
	if changeto == 'DOWN' and not direction == 'UP':
		direction = 'DOWN'


	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] += 10

	#Snake body mech
	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		score += 1
		foodSpawn = False
	else:
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
	foodSpawn = True


	playSurface.fill(white)
	for pos in snakeBody:

		pygame.draw.rect(playSurface, green, 
		pygame.Rect(pos[0],pos[1],10,10) )

		pygame.draw.rect(playSurface, brown	, 
		pygame.Rect(foodPos[0],foodPos[1],10,10) )

		if snakePos[0] > 710 or snakePos[0] < 0:
			gameOver() 
		if snakePos[1] > 450 or snakePos[1] < 0:
			gameOver()

		for block in snakeBody[1:]:
			if snakePos[0] == block[0] and snakePos[1] == block[1]:
				gameOver()
	pygame.display.flip()
	showScore(1)
	fpsController.tick(25)







