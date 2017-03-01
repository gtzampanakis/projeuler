from itertools import *

N = 4

R = range(1, N+1)

def p_to_seq(p):
	seq = []
	for i, pi in enumerate(p):
		seq.append(sum(1 for el in p[:i] if el > pi))
	return seq

pairs = []
for p in permutations(R, N):
	pairs.append((p, p_to_seq(p)))

pairs.sort(key = lambda p: p[1])

for pairi, pair in enumerate(pairs):
	print pair[0], '  ', pair[1]
	if pairi % 4 == N-1:
		print

