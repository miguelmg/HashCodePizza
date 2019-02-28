#
# pizza = []
#
# def readHeader(fileInput):
#
# 	line = fileInput.readline()
# 	line = line.split(' ')
# 	rowsPizza = line[0]
# 	colsPizza = line[1]
# 	minIngredientsPerSlice = line[2]
# 	maxSizeSlice = line[3]
#
# 	print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(rowsPizza,colsPizza,minIngredientsPerSlice,maxSizeSlice))
#
# 	header = {'rowsPizza':int(rowsPizza), 'colsPizza':int(colsPizza), 'minIngredientsPerSlice':int(minIngredientsPerSlice), 'maxSizeSlice':int(maxSizeSlice) }
# 	print(header)
# 	return header
#
# def readData(fileInput,header):
#
# 	print("header: ", header)
# 	print("Rows: ",header['rowsPizza'])
# 	row=[]
# 	#print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(header.rowsPizza,header.colsPizza,header.minIngredientsPerSlice,header.maxSizeSlice))
# 	for rowIndex in range(0, header['rowsPizza']):
# 		for colIndex in range(0, header['colsPizza']):
# 			ingredient=fileInput.read(1)
# 			row.append(ingredient)
# 		fileInput.read(1) #Line carry return
# 		pizza.append(row)
# 		row=[]
#
#
# 	print (pizza)
# 	return pizza
#
#
# def inputData(fileName="a_example.in"):
# 	fileInput = open(fileName,"r")
# 	header=readHeader(fileInput)
# 	dataset = readData(fileInput,header)
#
#
#
#
# inputData("a_example.in")

pizza = []


def readHeader(fileInput):
	line = fileInput.readline()
	line = line.split(' ')
	rowsPizza = line[0]
	colsPizza = line[1]
	minIngredientsPerSlice = line[2]
	maxSizeSlice = line[3]

	print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(rowsPizza, colsPizza, minIngredientsPerSlice, maxSizeSlice))

	header = {'rowsPizza': int(rowsPizza), 'colsPizza': int(colsPizza), 'minIngredientsPerSlice': int(minIngredientsPerSlice), 'maxSizeSlice': int(maxSizeSlice)}
	print(header)
	return header


def readData(fileInput, header):
	print("header: ", header)
	print("Rows: ", header['rowsPizza'])
	row = []
	# print("Size pizza({} ,{}) and the slices with min {} ingredients and max slice size {}".format(header.rowsPizza,header.colsPizza,header.minIngredientsPerSlice,header.maxSizeSlice))
	for rowIndex in range(0, header['rowsPizza']):
		for colIndex in range(0, header['colsPizza']):
			ingredient = fileInput.read(1)
			row.append(ingredient)
		fileInput.read(1)  # Line carry return
		pizza.append(row)
		row = []

	print pizza
	return pizza


def factorize(maxSizeSlice, columns, rows):
	result = []
	for i in range(1, maxSizeSlice + 1):
		if maxSizeSlice % i == 0 and i <= rows and (maxSizeSlice / i) <= columns:
			result.append([i, (maxSizeSlice / i)])

	return result


def checkSlice(slice, minIngredients):
	mushroom = 0
	tomatoe = 0

	for row in slice:
		for column in row:
			if column == 'T':
				tomatoe += 1
			elif column == 'M':
				mushroom += 1

	if mushroom >= minIngredients and tomatoe >= minIngredients:
		return True

	return False


def findAllValidSlices(row, column, maxRow, maxColumn, pizza, minIngredients):
	print "Searching for slices " + str(row) + "x" + str(column)
	cachos = []
	coordinates = []
	for i in range(0, maxRow):
		for j in range(0, maxColumn):
			if i + row < maxRow and j + column < maxColumn:
				print "Cutting between rows (" + str(i) + "," + str(i + row - 1) + ")"
				print "and columns (" + str(j) + "," + str(j + column - 1) + ")"

				slice = []
				for k in range(i, i + row):
					subslice = []
					for z in range(j, j + column):
						subslice.append(pizza[k][z])
					slice.append(subslice)

				if checkSlice(slice, minIngredients):
					print "Appending Slice"
					cachos.append(slice)
					coordinates.append([i, i + row - 1, j, j + column - 1])
					i = i + row
					j = j + column
					# return [i, i + row - 1, j, j + column - 1]

	return [coordinates, cachos]


def inputData(fileName="a_example.in"):
	fileInput = open(fileName + ".in", "r")
	header = readHeader(fileInput)
	pizza = readData(fileInput, header)
	possibleCombinations = factorize(header['maxSizeSlice'], header['colsPizza'], header['rowsPizza'])
	print possibleCombinations

	for possibleCombination in possibleCombinations:
		validSlices = findAllValidSlices(possibleCombination[0], possibleCombination[1], header['rowsPizza'],
										header['colsPizza'], pizza, header['minIngredientsPerSlice'])
		i = 1
		output = open(fileName + ".out", "w")
		# if validSlice :
		for validSlice in validSlices[0]:
			# output = open(fileName + ".out", "w")
			output.write(str(i))
			output.write("\n")
			output.write(
				str(validSlice[0]) + " " + str(validSlice[2]) + " " + str(validSlice[1]) + " " + str(validSlice[3]))
			output.write("\n")
			i += 1
			# break


inputData("a_example")
inputData("b_small")
inputData("c_medium")
inputData("d_big")

