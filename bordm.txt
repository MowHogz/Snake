def convert(height,width,snake,food):#Converts height width snake and food into the brd matrix
	matrix = []
	for row in range(height):
		matrix.append([])
		for column in range(width):
			matrix[row].append(" ")

	for unit in snake[:len(snake)-1]:
		matrix[unit[1]][unit[0]] = unit[2]
	unit = snake[len(snake)-1]
	matrix[unit[1]][unit[0]] = "O"
	for f in food:
		matrix[f[1]][f[0]] = "X"
	return matrix