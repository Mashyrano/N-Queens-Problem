import pygame
import numpy as np
import nQueens

pygame.init()

queens = 10
dimension = 600
BLOCK_SIZE = dimension/queens
win = pygame.display.set_mode((dimension+queens,dimension+60))
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

CLICKED_ARRAY = np.zeros((queens,queens))
columns = np.zeros(queens)
solutions = list()
solution = 0
nQueens.solve(CLICKED_ARRAY, 0, solutions,columns)

CLICKED_ARRAY = solutions[solution]

def main():
	global CLICKED_ARRAY,solution
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
				if CLICKED_ARRAY[column][row] == 1:
					win.blit(im1, (row*BLOCK_SIZE+row, column*BLOCK_SIZE+column))
				
				#pygame.draw.rect(win, BLACK, (row*BLOCK_SIZE, column*BLOCK_SIZE ,BLOCK_SIZE,BLOCK_SIZE), 1)
				# draw input bar
				pygame.draw.rect(win, GREEN, (0, BLOCK_SIZE*queens+queens ,BLOCK_SIZE*queens+queens,50))
				text = font1.render('Press \'N\' and \'P\' to toggle btwn solutions:',1,(0,0,0))
				text2 = font1.render(str(solution + 1) + '\\' + str(len(solutions)),1,(0,0,0))
				win.blit(text, (0, BLOCK_SIZE*queens+queens+5))
				win.blit(text2, (0, BLOCK_SIZE*queens+queens+25))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_n:
					if solution < len(solutions)-1:
						solution += 1
						CLICKED_ARRAY = solutions[solution]
						#print(CLICKED_ARRAY)
				if event.key == pygame.K_p:
					if solution > 0:
						solution -= 1
						CLICKED_ARRAY = solutions[solution]
		pygame.display.update()

	pygame.quit()

if __name__ == '__main__':
	main()

