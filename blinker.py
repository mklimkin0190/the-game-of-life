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
	x, y = cell
	neighbour_count = 0
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if (i, j) in cells and not (i == x and j == y):
				neighbour_count += 1
	return neighbour_count

def cell_dies(neighbour_count):
	return neighbour_count < 2 or neighbour_count > 3

def cell_is_reborn(neighbour_count):
	return neighbour_count == 3

def meaningfull_cells(cells):
	xlist = list(cell[0] for cell in cells)
	ylist = list(cell[1] for cell in cells)
	return (range(min(xlist) - 1, max(xlist) + 2), range(min(ylist) - 1, max(ylist) + 2))

def round(cells):
	end_state = []
	xboundaries, yboundaries = meaningfull_cells(cells)
	for i in xboundaries:
		for j in yboundaries:
			count = neighbour_count((i, j), cells)
			if (i, j) in cells:
				if not cell_dies(count):
					end_state.append((i, j))
			elif cell_is_reborn(count):
				end_state.append((i, j))
	return end_state

def test():
	seed = [(0, 0), (0, 1), (1, 0), (1, 1)]
	blinker = [(2, 1), (2, 2), (2, 3)]
	toad = [(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)]
	draw_cells(seed)
	for cell in seed:
		count = neighbour_count(cell,            seed)
		assert count == 3
		assert not cell_dies(count)
	for i in range(0, size):
		for j in range(0, size):
			count = neighbour_count((i, j), seed)
			assert (i, j) in seed or not cell_is_reborn(count)

	assert round(seed) == seed
	assert round(round(blinker)) == blinker
	assert round(round(toad)) == toad

test()



