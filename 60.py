import sys

import memoize

from sieve import *
from prime import *

seqs = [[2]]

gen = gen_primes()

ps = set()
maxp = None
maxreq = -1

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

def isp(n):
	global maxreq
	if n > maxreq:
		maxreq = n
	return is_prime(n)

best = -1
for pi, p in enumerate(gen_primes(), 1):
	if p <= 2:
		continue
	found_seq = False
	for seq in seqs:
		found = True
		both = []
		for seqp in seq:
			combines = combine(p, seqp)
			if not isp(combines.next()) or not isp(combines.next()):
				found = False
				both.append(0)
			both.append(1)
		if found:
			found_seq = True
			seq.append(p)
			if len(seq) > best:
				best = len(seq)
	if not found_seq:
		seqs.append([p])
	new_seqs = []
	for seq in seqs:
		if len(seq) >= best-1:
			new_seqs.append(seq)
	seqs = new_seqs
	if pi % 25 == 0:
		print p, best, maxreq, len(seqs), seqs[:4]

