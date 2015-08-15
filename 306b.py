import copy, logging, itertools, collections
import memoize

WON = 1
LOST = -1

PRINT = 1
BREAK_EARLY = 0

def treat(ns):
	ns = [n for n in ns if n != 1 and n != 0]
	ns.sort()
	ns = tuple(ns)
	return ns

@memoize.MemoizedFunction
def wonlost2_in(ns):
	ns = list(ns)
	result = LOST
	winning_moves = None
	losing_moves = None
	if ns == [ ]:
		result = LOST
	elif ns == [0]:
		result = LOST
	elif ns == [1]:
		result = LOST

def splits(le):
	for sp in xrange(0, (le-1) / 2 + (1 if le % 2 == 0 else 0) ):
		yield (sp, le-sp-2)

length_to_lost_islands = collections.defaultdict(set)
length_to_lost_islands[1].add((1,))

def tree():
	fro = [  [1]   ]
	# for le in xrange(1, 10, 2):
	# 	for split in splits(le):
	# 		pass
	for le in xrange(3, 12, 2):
		print 'Handling le:', le

			

# end = 1
# print sum(1 for n in xrange(1, end + 1) if wonlost2_in((n,)) == WON)

tree()

