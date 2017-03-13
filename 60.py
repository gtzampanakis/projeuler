import sys

import memoize

from sieve import *
from prime import *

seqs = [[2]]

gen = gen_primes()

ps = set()
maxp = None

def combine(p1, p2):
	strp1 = str(p1)
	strp2 = str(p2)
	yield int(strp1 + strp2)
	yield int(strp2 + strp1)

def isp(n):
	global maxp, ps
	while maxp < n:
		nextp = gen.next()
		ps.add(nextp)
		maxp = nextp
	return n in ps

#@memoize.MemoizedFunction
def isp2(n):
	if n % 2 == 0:
		return False
	for c in xrange(3, int(n**.5)+1, 2):
		if n % c == 0:
			return False
	return True

for p in gen_primes():
	if p <= 2:
		continue
	found_seq = False
	for seq in seqs:
		found = True
		for seqp in seq:
			combines = combine(p, seqp)
			if not is_prime(combines.next()) or not is_prime(combines.next()):
				found = False
				break
		if found:
			found_seq = True
			seq.append(p)
	if not found_seq:
		seqs.append([p])
	new_seqs = []
	best = max(len(seq) for seq in seqs)
	for seq in seqs:
		if len(seq) >= best-2:
			new_seqs.append(seq)
	seqs = new_seqs
	if best == 5:
		print p, best, len(seqs), seqs
		break

