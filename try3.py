import pygame
import numpy as np
from PIL import Image
import nQueens

pygame.init()

BLOCK_SIZE = 70
dimension = BLOCK_SIZE*8+7
win = pygame.display.set_mode((dimension,dimension+50))
pygame.display.set_caption('N Queens Problem')

BLACK = (181,136,99)
WHITE = (240,217,181)
GREEN = (120,255,99)
RED = (255,0,0)


#Process Queen Image
im1 = pygame.image.load('img/queen2.png')
DEFAULT_IMAGE_SIZE = (BLOCK_SIZE, BLOCK_SIZE)
im1 = pygame.transform.scale(im1, DEFAULT_IMAGE_SIZE)

#font
font1 = pygame.font.SysFont('microsofthimalaya', 25)

CLICKED_ARRAY = np.zeros((8,8))
solutions = list()
solution = 0
nQueens.solve(CLICKED_ARRAY, 0, solutions)

CLICKED_ARRAY = solutions[solution]

run = True
while run:
	win.fill(WHITE)
	for row in range(len(CLICKED_ARRAY)):
		for column in range(len(CLICKED_ARRAY)):
			# checkered boxes
			a = row % 2
			b = column % 2
			if a == 0:
				if b == 0:
					color = BLACK
				else:
					color = WHITE
			else:
				if b == 0:
					color = WHITE
				else:
					color = BLACK

			pygame.draw.rect(win, color, (row*BLOCK_SIZE+row, column*BLOCK_SIZE+column ,BLOCK_SIZE,BLOCK_SIZE))
			if CLICKED_ARRAY[row, column] == 1:
				win.blit(im1, (row*BLOCK_SIZE+row, column*BLOCK_SIZE+column))
			
			#pygame.draw.rect(win, BLACK, (row*BLOCK_SIZE, column*BLOCK_SIZE ,BLOCK_SIZE,BLOCK_SIZE), 1)
			# draw input bar
			pygame.draw.rect(win, GREEN, (0, BLOCK_SIZE*8+7 ,BLOCK_SIZE*8+7,50))
			text = font1.render('Press \'N\' for next solution: ',1,(0,0,0))
			win.blit(text, (0, BLOCK_SIZE*8+10))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_n:
				if solution < 91:
					solution += 1
					CLICKED_ARRAY = solutions[solution]

			
		'''
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# User clicks the mouse. Get the position
			pos = pygame.mouse.get_pos()

			# make sure the box clicked is captured accurately
			n = pos[1]//BLOCK_SIZE
			m = pos[0]//BLOCK_SIZE

			if pos[1] < (BLOCK_SIZE*n) + n:
				x = n-1
			else:
				x = n

			if pos[0] < (BLOCK_SIZE*m) + m:
				y = m-1
			else:
				y = m


			#update array
			if CLICKED_ARRAY[y][x] == 0:
				CLICKED_ARRAY[y][x] = 1
			else:
				CLICKED_ARRAY[y][x] = 0
		'''
	pygame.display.update()

pygame.quit()

