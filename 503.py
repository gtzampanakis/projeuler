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

DO_STRATEGY= 0

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

strategy = []

@pmemoize.MemoizedFunction
def calc_s_move(m):
	return F(1,m+1) * sum(
			exp2(ii,m+1) for ii in xrange(m+1)
	)

@pmemoize.MemoizedFunction
def calc_exp_curr(i,m):
	return F( (N+1) * (m-i) , m+1 )

@pmemoize.MemoizedFunction
def exp2(i, m):

	assert 0 <= i <= m-1
	assert 1 <= m <= N

	s_move = None

	if 0:
		s_stay = None
		c_stay = None
		# x = tc / su(m)
		# x = factorial(N+1)/(m*(m+1))
		x = calc_x(m)
		s_stay = (m-i)*x
		c_stay = nperms / m

	if m < N:
		s_move = calc_s_move(m)

	if 0:
		print 's_stay(%s,%s):%s' % (i,m, s_stay)
		print 'c_stay(%s,%s):%s' % (i,m, c_stay)
		print 's_move(%s,%s):%s' % (i,m, s_move)
		print

	exp_curr = F( (N+1) * (m-i) , m+1 )
	exp_curr = calc_exp_curr(i,m)

	if s_move is None:
		return exp_curr
	else:
		if DO_STRATEGY:
			if exp_curr < s_move:
				s = 'STAY', i, m
			elif exp_curr > s_move:
				s = 'MOVE', i, m
			else:
				s = 'NOCA', i, m
			strategy.append(s)
		return min((exp_curr, s_move))

print
res = exp2(0, 1)
print N, float(res)

print

if DO_STRATEGY:
	strategy.sort(key = lambda s: (s[1],s[2]))
	for si, s in enumerate(strategy):
		print s[0], s[1], s[2]
		if (si+1)%4 == 0:
			print

