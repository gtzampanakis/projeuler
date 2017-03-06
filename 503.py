import sys
sys.setrecursionlimit(10000)

from fractions import *
from itertools import *
from pprint import pprint

import pmemoize

# For the final card it is always c+i=N. This is because all cards have been
# drawn before it so the info given uniquely identifies it.

# Current card distribution depends only on current info and number of cards
# left!

F = Fraction

N = 200

@pmemoize.MemoizedFunction
def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n * factorial(n-1)

@pmemoize.MemoizedFunction
def su(n):
	return n*(n+1)/2

# tc = nperms / N * su(N)
tc = factorial(N+1)/2
nperms = factorial(N)

@pmemoize.MemoizedFunction
def calc_x(m):
	if m == 1:
		return factorial(N+1)/2
	else:
		return calc_x(m-1) * (m-1) / (m+1)

@pmemoize.MemoizedFunction
def exp2(i, m):

	assert 0 <= i <= m-1
	assert 1 <= m <= N

	s_stay = None
	c_stay = None
	s_move = None

	if 0:
		# x = tc / su(m)
		# x = factorial(N+1)/(m*(m+1))
		x = calc_x(m)
		s_stay = (m-i)*x
		c_stay = nperms / m

	if m < N:
		s_move = F(1,m+1) * sum(
				exp2(ii,m+1) for ii in xrange(m+1)
		)

	if 0:
		print 's_stay(%s,%s):%s' % (i,m, s_stay)
		print 'c_stay(%s,%s):%s' % (i,m, c_stay)
		print 's_move(%s,%s):%s' % (i,m, s_move)
		print

	exp_curr = F( (N+1) * (m-i) , m+1 )

	if s_move is None:
		return exp_curr
	else:
		return min((exp_curr, s_move))

res = exp2(0, 1)
print N, float(res)
