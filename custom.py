import pygame
import numpy as np
import nQueens

pygame.init()

queens = 20
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


def main():
    global CLICKED_ARRAY, text
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
                if CLICKED_ARRAY[column, row] == 1:
                    win.blit(im1, (row*BLOCK_SIZE+row, column*BLOCK_SIZE+column))
                
                #pygame.draw.rect(win, BLACK, (row*BLOCK_SIZE, column*BLOCK_SIZE ,BLOCK_SIZE,BLOCK_SIZE), 1)
                # draw input bar
                pygame.draw.rect(win, GREEN, (0, BLOCK_SIZE*queens+queens ,BLOCK_SIZE*queens+queens,50))
                text = font1.render('Press SPACE BAR to check solution',1,(0,0,0))
                win.blit(text, (0, BLOCK_SIZE*queens+queens+5))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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

                y = int(y)
                x = int(x)
                #update array

                if CLICKED_ARRAY[x][y] == 0:
                    CLICKED_ARRAY[x][y] = 1
                else:
                    CLICKED_ARRAY[x][y] = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    checkSolution(CLICKED_ARRAY)

        pygame.display.update()

    pygame.quit()


def checkSolution(arr):
    max = len(arr)

    for i in range(max):
        for j in range(max):
            if arr[i][j] == 1:
                attacked = nQueens.checkAttack(arr,i,j)
                if attacked:
                    showError(list((i,j)), list(attacked))
                    return
                    
def showError(From, To):
    while True:
        if From[0] == To[0] and  From[1] == To[1]:
            return
        if From[0] > To[0]:
            To[0] += 1
        elif From[0] < To[0]:
            To[0] -= 1

        if From[1] > To[1]:
            To[1] += 1
        elif From[1] < To[1]:
            To[1] -= 1
        row = To[1]
        column = To[0]

        pygame.draw.rect(win, RED, (row*BLOCK_SIZE+row, column*BLOCK_SIZE+column ,BLOCK_SIZE,BLOCK_SIZE))
        

if __name__ == '__main__':
	main()

