import copy

arr  = [[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]
		]

# X-axis
def checkLeft(arr,i,j):
	if j > 0:
		for x in range(j-1, -1, -1):
			if arr[i][x] == 1:
				return False
	return True
def checkRight(arr,i,j):
	if j < len(arr)-1:
		for x in range(j+1, len(arr)):
			if arr[i][x] == 1:
				return False
	return True

# Y-axis
def checkAbove(arr,i,j):
	if i > 0:
		for x in range(i-1, -1, -1):
			if arr[x][j] == 1:
				return False
	return True
def checkBelow(arr,i,j):
	if i < len(arr)-1:
		for x in range(i+1, len(arr)):
			if arr[x][j] == 1:
				return False
	return True

# Upper Diagonals
def checkUpperLeftDiagonal(arr,i,j):
	x = i-1
	y = j-1
	if i > 0 and j > 0:
		while x >= 0 and y >= 0:
			if arr[x][y] == 1:
				return False			
			x -= 1
			y -= 1
	return True
def checkUpperRightDiagonal(arr,i,j):
	x = i-1
	y = j+1
	if i > 0 and j < len(arr) - 1:
		while x >= 0 and y < len(arr):
			if arr[x][y] == 1:
				return False			
			x -= 1
			y += 1
	return True

# Lower Diagonals

def checkLowerLeftDiagonal(arr,i,j):
	x = i+1
	y = j-1
	if j > 0 and i < len(arr) - 1:
		while y >= 0 and x < len(arr):
			if arr[x][y] == 1:
				return False
			x += 1
			y -= 1
	return True
def checkLowerRightDiagonal(arr,i,j):
	x = i+1
	y = j+1
	if i < len(arr) - 1 and j  < len(arr) - 1:
		while x < len(arr) and y < len(arr):
			if arr[x][y] == 1:
				return False
			x += 1
			y += 1
	return True

def checkAttack(arr,i, j):
	# returns True when not attacked : False otherwise
	if not checkLeft(arr, i, j):
		return False
	if not checkRight(arr, i, j):
		return False
	if not checkAbove(arr, i, j):
		return False
	if not checkBelow(arr, i, j):
		return False
	if not checkUpperLeftDiagonal(arr, i, j):
		return False
	if not checkUpperRightDiagonal(arr, i, j):
		return False
	if not checkLowerLeftDiagonal(arr, i, j):
		return False
	if not checkLowerRightDiagonal(arr, i, j):
		return False
	return True

solutions = list()

def solve(arr, row, solutions):
	if row >= len(arr):
		solutions.append(arr)
		return

	for i in range(len(arr)):
		cpyArr = copy.deepcopy(arr)
		cpyArr[row][i] = 1
		#print(cpyArr)
		attacked = not checkAttack(cpyArr,row, i)
		if attacked:
			continue
		solve(cpyArr, row+1, solutions)

#solve(arr, 0)

#print(len(solutions))

