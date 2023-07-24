import copy

# X-axis
def checkLeft(arr,i,j):
	if j > 0:
		for x in range(j-1, -1, -1):
			if arr[i][x] == 1:
				return (i,x)
	return False
def checkRight(arr,i,j):
	if j < len(arr)-1:
		for x in range(j+1, len(arr)):
			if arr[i][x] == 1:
				return (i,x)
	return False

# Y-axis
def checkAbove(arr,i,j):
	if i > 0:
		for x in range(i-1, -1, -1):
			if arr[x][j] == 1:
				return (x,j)
	return False
def checkBelow(arr,i,j):
	if i < len(arr)-1:
		for x in range(i+1, len(arr)):
			if arr[x][j] == 1:
				return (x,j)
	return False

# Upper Diagonals
def checkUpperLeftDiagonal(arr,i,j):
	x = i-1
	y = j-1
	if i > 0 and j > 0:
		while x >= 0 and y >= 0:
			if arr[x][y] == 1:
				return (x,y)			
			x -= 1
			y -= 1
	return False
def checkUpperRightDiagonal(arr,i,j):
	x = i-1
	y = j+1
	if i > 0 and j < len(arr) - 1:
		while x >= 0 and y < len(arr):
			if arr[x][y] == 1:
				return (x,y)			
			x -= 1
			y += 1
	return False

# Lower Diagonals

def checkLowerLeftDiagonal(arr,i,j):
	x = i+1
	y = j-1
	if j > 0 and i < len(arr) - 1:
		while y >= 0 and x < len(arr):
			if arr[x][y] == 1:
				return (x,y)
			x += 1
			y -= 1
	return False
def checkLowerRightDiagonal(arr,i,j):
	x = i+1
	y = j+1
	if i < len(arr) - 1 and j  < len(arr) - 1:
		while x < len(arr) and y < len(arr):
			if arr[x][y] == 1:
				return (x,y)
			x += 1
			y += 1
	return False

def checkAttack(arr,i, j):
	attackers = list()
	# returns False when not attacked : True otherwise
	if checkLeft(arr, i, j):
		attackers.append(checkLeft(arr, i, j))
	if checkRight(arr, i, j):
		attackers.append(checkRight(arr, i, j))
	if checkAbove(arr, i, j):
		attackers.append(checkAbove(arr, i, j))
	if checkBelow(arr, i, j):
		attackers.append(checkBelow(arr, i, j))
	if checkUpperLeftDiagonal(arr, i, j):
		attackers.append(checkUpperLeftDiagonal(arr, i, j))
	if checkUpperRightDiagonal(arr, i, j):
		attackers.append(checkUpperRightDiagonal(arr, i, j))
	if checkLowerLeftDiagonal(arr, i, j):
		attackers.append(checkLowerLeftDiagonal(arr, i, j))
	if checkLowerRightDiagonal(arr, i, j):
		attackers.append(checkLowerRightDiagonal(arr, i, j))

	if len(attackers) == 0:
		return False
	return attackers

solutions = list()

def solve(arr, row, solutions, columns):
	if row >= len(arr):
		solutions.append(arr)
		return

	for i in range(len(arr)):
		if columns[i] == 1:
			continue
		cpyArr = copy.deepcopy(arr)
		cpyColumns = copy.deepcopy(columns)
		cpyArr[row][i] = 1
		
		#print(cpyArr)
		attacked = checkAttack(cpyArr,row, i)
		if attacked:
			continue
		cpyColumns[i] = 1
		solve(cpyArr, row+1, solutions, cpyColumns)


