from fractions import *
from itertools import *
from pprint import pprint

import pmemoize

F = Fraction

N = 4

R = range(1, N+1)

def mprint(*args, **kwargs):
	if 0:
		pprint(*args, **kwargs)

def p_to_seq(p):
	seq = []
	for i, pi in enumerate(p):
		seq.append(sum(1 for el in p[:i] if el > pi))
	return tuple(seq)

pairs = []
decks = []
infos = []
for p in permutations(R, N):
	decks.append(p)
	infos.append(p_to_seq(p))
	pairs.append((decks[-1], infos[-1]))

pairs.sort(key = lambda p: p[1])

if 0:
	for pairi, pair in enumerate(pairs):
		print pair[0], '  ', pair[1] 
		if pairi % 4 == N-1:
			print

strategy = []

@pmemoize.MemoizedFunction
def exp(info):

	s_move = float('inf')

	assert info
	r = len(info)
	s_stay = 0
	c = 0
	cis = []
	cds = []
	sums = []
	counts = []
	for cd, ci in zip(decks, infos):
		if ci[:r] == info:
			cis.append(ci)
			cds.append(cd)
			s_stay += cd[r-1]
			c += 1

	s_prev = sum(sum(cd[:r-1]) for cd in cds)
	s_curr = sum(cd[r-1] for cd in cds)
	s_next = sum(sum(cd[r:]) for cd in cds)

	c_prev = sum(len(cd[:r-1]) for cd in cds)
	c_curr = sum(1 for cd in cds)
	c_next = sum(len(cd[r:]) for cd in cds)

	sums = [s_prev, s_curr, s_next]
	counts = [c_prev, c_curr, c_next]
	avgs = [ (su/float(co) if co else 0) for su,co in zip(sums, counts) ]

	if r == N:
		mprint(info, s_stay, 'N/A')

	else:
		s_move = sum(
				exp(ci[:r+1]) for ci in cis
		)
	
	if 1:

		side = ' '
		if avgs[1] > avgs[2]:
			side = '>'
		elif avgs[1] == avgs[2]:
			side = '='
		elif avgs[1] < avgs[2]:
			side = '<'

		if r == N:
			pass
		elif s_stay < s_move:
			strategy.append(( 'STAY', side, ('%1.3f %1.3f %1.3f   ' % (tuple(avgs))), info ))
		elif s_stay > s_move:
			strategy.append(( 'MOVE', side, ('%1.3f %1.3f %1.3f   ' % (tuple(avgs))), info ))
		else:
			strategy.append(( 'NOCA', side, ('%1.3f %1.3f %1.3f   ' % (tuple(avgs))), info ))

	return F(min((
			s_stay, s_move
	)), c)

print
print
mprint()
exp(tuple([0]))

strategy.sort(key = lambda s: len(s[3]), reverse = False)

for si, s in enumerate(strategy):
	print s[0], s[1], s[2], s[3]
	if si % 4 == N-1:
		print
