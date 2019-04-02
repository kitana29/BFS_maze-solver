import sys

#----------------------------------------------------------------------
#fungsi BFS
def BFS():
	global current, visited, queue, maze, jalur
	koor = []
	solution = []
	current = queue[0]
	if((current[0] != 0) and (maze[current[0]-1][current[1]] == 0)) : #mau ke atas
		koor = [current[0]-1,current[1]]
		if (koor not in visited):
			queue.append(koor)
			solution.append(koor)
	if((current[1] != (len(maze[0]) - 1)) and (maze[current[0]][current[1]+1] == 0)) : #mau ke kanan
		koor = [current[0],current[1]+1]
		if (koor not in visited):
			queue.append(koor)
			solution.append(koor)
	if((current[1] != (len(maze)-1)) and (maze[current[0]+1][current[1]] == 0)) : #mau ke bawah
		koor = [current[0]+1,current[1]]
		if (koor not in visited):
			queue.append(koor)
			solution.append(koor)
	if((current[0] != 0) and (maze[current[0]][current[1]-1] == 0)) : #mau ke kiri
		koor = [current[0],current[1]-1]
		if (koor not in visited):	
			queue.append(koor)
			solution.append(koor)
	
	if (len(solution) > 0) :
		for i in range(len(solution)):
			if (current != solution[i] and solution[i] not in visited):
				jalur.append([current,solution[i]])
		
	queue.pop(0)
	visited.append(current)


#----------------------------------------------------------------------
#fungsi bactracking
def backtrack() :
	global jalur
	global goal
	global start
	global maze
	value = goal
	maze[value[0]][value[1]] = '.'
	while (value != start):
		for i in range(len(jalur)):
			if (value == jalur[i][1]):
				value = jalur[i][0]
				break
		
		maze[value[0]][value[1]] = '.'

#--------------------------------------
#-----------------------------------
#---------- MAIN PROGRAM ------------ 
#--------------------------------------
#-----------------------------------

#menampilkan map (dalam file text) ke layar
with open('input_t.txt','r') as f:
	input_t = f.readlines()

maze = []
for raw_line in input_t:
	split_line = raw_line.strip()
	nums_ls = [int(x) for x in split_line]
	maze.append(nums_ls)

for i in range(len(maze)):
	for j in range(len(maze[i])):
		sys.stdout.write(str(maze[i][j]))
	print()

#----------------------------------------------------------------------
#inisialisasi semua list yang akan dipakai
queue = []		
visited = []	
jalur = []	
start = []	
goal = []		
current = []
solution = []

#----------------------------------------------------------------------
#masukan koordinat start dan goal (dalam bentuk indeks matriks (i,j))
in_start = str(input("Masukkan start: "))
start = [int(x) for x in in_start.split(',')]
while (maze[start[0]][start[1]] == 1):		#start harus benar pada grid 0
	in_start = str(input("Masukkan start: "))
	start = [int(x) for x in in_start.split(',')]
start = [int(x) for x in in_start.split(',')]

in_goal = str(input("Masukkan goal: "))
goal = [int(x) for x in in_goal.split(',')]
while (maze[goal[0]][goal[1]] == 1):		#goal harus benar pada grid 0
	in_goal = str(input("Masukkan goal: "))
	goal = [int(x) for x in in_goal.split(',')]
goal = [int(x) for x in in_goal.split(',')]
print()
print()

#----------------------------------------------------------------------
#koordinat start di-push ke queue
queue.append(start)

#----------------------------------------------------------------------
#algoritma BFS dimulai
while (len(queue) > 0 and (goal not in visited)) :
	BFS()

#----------------------------------------------------------------------
#menemukan path yang dilalui dari start menuju goal
backtrack()
#print solusi path
print("Jalur yang harus dilalui: ")
for i in range(len(maze)):
	for j in range(len(maze[i])):
		sys.stdout.write(str(maze[i][j]))
	print()
