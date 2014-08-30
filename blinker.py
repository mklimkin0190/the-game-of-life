import math

live_cells = [(2, 1), (2, 2), (2, 3)]

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



print neighbour_count((2, 1), live_cells), cell_dies((2, 1), live_cells)
print neighbour_count((2, 2), live_cells), cell_dies((2, 2), live_cells)
print neighbour_count((2, 3), live_cells), cell_dies((2, 3), live_cells)
print neighbour_count((1, 2), live_cells), cell_is_reborn((1, 2), live_cells)
print neighbour_count((3, 2), live_cells), cell_is_reborn((3, 2), live_cells)


draw_cells(round(round(live_cells)))

