import itertools

def solve(x0y0):
	x0, y0 = x0y0
	D = (x0 - y0)**2 + 4.
	xdev = (D**.5 - x0 - y0) / 2.
	new = ((x0 + xdev, y0), (x0, y0 + xdev))

	return xdev, new

seq = [ (1, 0) ]


selection = (1, 0)
openings = [ (1, 0) ]
openings_indices = [ (0, 0) ]

squares = [ ]

for n in itertools.count(1):
	# print new_xdev, candidates

	cand_new_xdevs = [ ]
	cand_cands = [ ]
	cand_indices = [ ]
	for opening in openings:
		solved = solve(opening)
		cand_new_xdevs.append(solved[0])
		cand_cands.append(solved[1])

	new_selection = max(cand_new_xdevs)
	best_new_xdev_index = cand_new_xdevs.index(new_selection)
	new_cands = cand_cands[best_new_xdev_index]
	opening_replaced = openings.pop(best_new_xdev_index)
	openings += new_cands

	# new_square = ((opening[0] + new_selection), (opening[1]))

	print n, opening_replaced

	squares.append(opening_replaced)

	if n == 100:
		break


	

