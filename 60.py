import sys

import memoize

from sieve import *

seqs = [[2]]

gen = gen_primes()

ps = set()
maxp = None

def combine(p1, p2):
	strp1 = str(p1)
	strp2 = str(p2)
	yield int(strp1 + strp2)
	yield int(strp2 + strp1)

@memoize.MemoizedFunction
def isp(n):
	global maxp, ps
	while maxp < n:
		nextp = gen.next()
		ps.add(nextp)
		maxp = nextp
	return n in ps


for p in gen_primes():
	if p <= 2:
		continue
	found_seq = False
	for seq in seqs:
		found = True
		for seqp in seq:
			combines = combine(p, seqp)
			if not isp(combines.next()) or not isp(combines.next()):
				found = False
				break
		if found:
			found_seq = True
			seq.append(p)
	if not found_seq:
		seqs.append([p])
	print p, len(seqs), max(len(seq) for seq in seqs)

