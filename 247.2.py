import itertools, heapq
import memoize

@memoize.MemoizedFunction
def solve(x0y0):
	x0, y0 = x0y0
	D = (x0 - y0)**2 + 4.
	xdev = (D**.5 - x0 - y0) / 2.
	new = ((x0 + xdev, y0), (x0, y0 + xdev))

	return xdev, new

openings = [ (1, 0) ]
openings_indices = [ (0, 0) ]

largest_33_found = None
largest_index_found = None

TO_FIND = 3

for n in itertools.count(1):

	new_selection = None
	new_cands = None

	openingi = 0
	for opening, opening_index in zip(openings, openings_indices):
		solved = solve(opening)
		if new_selection is None or solved[0] > new_selection:
			new_selection = solved[0]
			best_new_xdev_index = openingi
			new_cands = solved[1]
			new_indices = (( (opening_index[0] + 1, opening_index[1] + 0), (opening_index[0] + 0, opening_index[1] + 1) ))

		openingi += 1

	opening_replaced = openings.pop(best_new_xdev_index)
	index_replaced = openings_indices.pop(best_new_xdev_index)



	openings += new_cands
	openings_indices += new_indices

	## for new_opening, new_opening_index in zip(new_cands, new_indices):
	## 	heapq.heappush(openings, new_opening)




	if largest_index_found is None or index_replaced > largest_index_found:
		largest_index_found = index_replaced

	if index_replaced == (TO_FIND, TO_FIND):
		largest_33_found = n

	if index_replaced == (TO_FIND + 1, TO_FIND + 1):
		break

	if n % 1 == 0:
		if index_replaced[0] >= 2 and index_replaced[1] >= 2:
			print n, index_replaced, opening_replaced

	if n >= 500000:
		break


print largest_33_found

	

