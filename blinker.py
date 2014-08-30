def draw_cells(cells):
	size = 5
	print '---------'
	for i in range(0, size):
		for j in range(0, size):
			state = 0 if (i, j) not in cells else 1
			print state,
		print
	print '---------'

def neighbour_count(cell, cells):
	neighbour_count = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if (cell[0] + i, cell[1] + j) in cells and not (i == 0 and j == 0):
				neighbour_count = neighbour_count + 1
	return neighbour_count

def cell_dies(cell, cells):
	if neighbour_count(cell, cells) < 2 or neighbour_count(cell, cells) > 3:
		return True
	else:
		return False

def cell_is_reborn(coords, cells):
	if neighbour_count(coords, cells) == 3:
		return True
	else:
		return False

def round(cells):
	size = 5
	end_state = []
	for i in range(0, size):
		for j in range(0, size):
			if (i, j) in cells and not cell_dies((i, j), cells):
				end_state.append((i, j))
			elif (i, j) not in cells and cell_is_reborn((i, j), cells):
				end_state.append((i, j))
	return end_state

def test():
	seed = [(0, 0), (0, 1), (1, 0), (1, 1)]
	size = 5
	draw_cells(seed)
	for cell in seed:
		assert neighbour_count(cell, seed) == 3
		assert not cell_dies(cell, seed)
	for i in range(0, size):
		for j in range(0, size):
			assert (i, j) in seed or not cell_is_reborn((i, j), seed)

	assert round(seed) == seed

	blinker = [(2, 1), (2, 2), (2, 3)]
	assert round(round(blinker)) == blinker

test()



