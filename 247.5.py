import itertools, heapq, bisect
from sortedcontainers import SortedListWithKey
import bst
import memoize

@memoize.MemoizedFunction
def solve(x0y0):
	x0, y0 = x0y0
	D = (x0 - y0)**2 + 4.
	xdev = (D**.5 - x0 - y0) / 2.
	new = ((x0 + xdev, y0), (x0, y0 + xdev))

	return xdev, new

openings = [ (1, 0) ]
openings_values = [ solve((1,0))[0] ]
openings_indices = [ (0, 0) ]
combined = SortedListWithKey([ [openings[-1], openings_values[-1], openings_indices[-1]] ],
									key = lambda r: solve(r[0])[0])
new_cands = solve((1,0))[1]
new_indices = [ (1,0), (0,1) ]

largest_33_found = None
largest_index_found = None

TO_FIND = 3

for n in itertools.count(2):

	## openings.pop()
	## openings_values.pop()
	## openings_indices.pop()
	combined.pop()

	for new_opening, new_opening_index in zip(new_cands, new_indices):
		combined.add([new_opening, solve(new_opening)[0], new_opening_index])
		### value = solve(new_opening)[0]

		### insertion_point = bisect.bisect_left(openings_values, value)
		### insertion_point = combined.bisect_left(value)

		### openings.insert(insertion_point, new_opening)
		### openings_values.insert(insertion_point, value)
		### openings_indices.insert(insertion_point, new_opening_index)

	# opening = openings[-1]
	opening = combined[-1][0]
	ind = combined[-1][2]
	solved = solve(opening)
	new_selection = solved[0]
	new_cands = solved[1]
	new_indices = (( (ind[0] + 1, ind[1] + 0), (ind[0] + 0, ind[1] + 1) ))


	if ind == (TO_FIND, TO_FIND):
		largest_33_found = n

	if ind[0] >= 3 and ind[1] >= 3:
		if ind[0] == ind[1]:
			print n, ind, opening, largest_33_found

	if n >= 100 and 0:
		break


print largest_33_found

	

