import copy, logging
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
	#elif ns == [2]:
	#	result = WON
	#	winning_moves = [0]
	#elif ns[0] in (2,3,4) and wonlost2_in(tuple(ns[1:])) == LOST:
	#	result = WON
	#elif len(ns) == 1 and ns[0] % 2 == 0:
	#	result = WON
	#elif len(ns) == 2 and ns[0] == ns[1]:
	#	result = LOST
	else:
	# Find valid moves.
		for ni, n in enumerate(ns):
			if n >= 2:
				winning_moves = [ ]
				losing_moves = [ ]
				for sp in xrange(0, (n-1) / 2 + (1 if n % 2 == 0 else 0) ):
					nsc = copy.copy(ns)
					nsc.pop(ni)
					nsc.append(sp)
					nsc.append(n-sp-2)
					nsc = treat(nsc)
					if wonlost2_in(nsc) == LOST:
						result = WON
						winning_moves.append([sp, n-sp-2, 
											wonlost2_in((sp,)) * wonlost2_in((n-sp-2,)), 
											])
						if BREAK_EARLY:
							break
					else:
						losing_moves.append([sp, n-sp-2, 
											wonlost2_in((sp,)) * wonlost2_in((n-sp-2,)), 
											])
	if PRINT:
		# print '%s: %s (w: %s), (l: %s)' % (ns, result, winning_moves, losing_moves)
		print '%s: %s (w: %s)' % (ns, result, winning_moves)
	return result
wonlost2_in = memoize.MemoizedFunction(wonlost2_in, 1000 * 1000 * 1000, record_stats = 0)
	
end = 50
print sum(1 for n in xrange(1, end + 1) if wonlost2_in((n,)) == WON)


