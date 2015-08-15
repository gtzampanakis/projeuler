import itertools
import memoize

@memoize.MemoizedFunction
def sum_up_to(k):
	if k == 1:
		return p(1)
	return p(k-1) + p(k)

@memoize.MemoizedFunction
def p(k):
	return (
			.001
			*
			(
				1. -
				( 0. if k-3<=0 else sum_up_to(k-3) ) -
				( 0. if k-2<=0 else p(k-2)*10)
			)
	)


running = 0.

for a in itertools.count(1):
	pa = p(a)
	running += a * pa
	if a % 200 == 0 or 1:
		print a, pa, running
	if pa < 0 or a > 100:
		print a, pa, running
		break


