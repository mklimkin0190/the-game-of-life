global size
size = 6

def draw_cells(cells):
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
				neighbour_count += 1
	return neighbour_count

def cell_dies(cell, cells):
	return neighbour_count(cell, cells) < 2 or neighbour_count(cell, cells) > 3

def cell_is_reborn(coords, cells):
	return neighbour_count(coords, cells) == 3

def meaningfull_cells(cells):
	xlist = list(cell[0] for cell in cells)
	ylist = list(cell[1] for cell in cells)
	return (range(min(xlist) - 1, max(xlist) + 2), range(min(ylist) - 1, max(ylist) + 2))

def round(cells):
	end_state = []
	xboundaries, yboundaries = meaningfull_cells(cells)
	for i in xboundaries:
		for j in yboundaries:
			if (i, j) in cells and not cell_dies((i, j), cells):
				end_state.append((i, j))
			elif (i, j) not in cells and cell_is_reborn((i, j), cells):
				end_state.append((i, j))
	return end_state

def test():
	seed = [(0, 0), (0, 1), (1, 0), (1, 1)]
	blinker = [(2, 1), (2, 2), (2, 3)]
	toad = [(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)]
	draw_cells(seed)
	for cell in seed:
		assert neighbour_count(cell, seed) == 3
		assert not cell_dies(cell, seed)
	for i in range(0, size):
		for j in range(0, size):
			assert (i, j) in seed or not cell_is_reborn((i, j), seed)

	assert round(seed) == seed
	assert round(round(blinker)) == blinker
	assert round(round(toad)) == toad

test()



