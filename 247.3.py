import itertools, heapq, bisect
from sortedcontainers import SortedList
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
new_cands = solve((1,0))[1]
new_indices = [ (1,0), (0,1) ]

largest_33_found = None
largest_index_found = None

TO_FIND = 3

for n in itertools.count(2):

	### openingi = 0
	### for opening, opening_index in zip(openings, openings_indices):
	### 	solved = solve(opening)
	### 	if new_selection is None or solved[0] > new_selection:
	### 		new_selection = solved[0]
	### 		best_new_xdev_index = openingi
	### 		new_cands = solved[1]
	### 		new_indices = (( (opening_index[0] + 1, opening_index[1] + 0), (opening_index[0] + 0, opening_index[1] + 1) ))

	### 	openingi += 1

	### opening_replaced = openings.pop(best_new_xdev_index)
	### opening_value_replaced = openings_values.pop(best_new_xdev_index)
	### index_replaced = openings_indices.pop(best_new_xdev_index)



	### if 0:
	### 	openings += new_cands
	### 	openings_indices += new_indices

	openings.pop()
	openings_values.pop()
	openings_indices.pop()

	for new_opening, new_opening_index in zip(new_cands, new_indices):
		value = solve(new_opening)[0]

		insertion_point = bisect.bisect_left(openings_values, value)

		openings.insert(insertion_point, new_opening)
		openings_values.insert(insertion_point, value)
		openings_indices.insert(insertion_point, new_opening_index)

	opening = openings[-1]
	solved = solve(opening)
	new_selection = solved[0]
	new_cands = solved[1]
	new_indices = (( (openings_indices[-1][0] + 1, openings_indices[-1][1] + 0), (openings_indices[-1][0] + 0, openings_indices[-1][1] + 1) ))



	## if largest_index_found is None or index_replaced > largest_index_found:
	## 	largest_index_found = index_replaced

	if openings_indices[-1] == (TO_FIND, TO_FIND):
		largest_33_found = n

	## if openings_indices[-1] == (TO_FIND + 1, TO_FIND + 1):
	## 	break

	if openings_indices[-1][0] >= 3 and openings_indices[-1][1] >= 3:
		if openings_indices[-1][0] == openings_indices[-1][1]:
			print n, openings_indices[-1], openings[-1], largest_33_found

	if n >= 100 and 0:
		break


print largest_33_found

	

