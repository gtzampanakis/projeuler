from itertools import *

import sys
import pmemoize

from sieve import *
from prime import *

isp = pmemoize.MemoizedFunction(is_prime)

PS = []
for p in gen_primes():
	if p >= 3:
		PS.append(p)
	if p > 100:
		break

def combine(p1, p2):
	strp1 = str(p1)
	strp2 = str(p2)
	return [int(strp1 + strp2), int(strp2 + strp1)]

def v2(seq1, seq2):
	for p1, p2 in product(seq1, seq2):
		c1, c2 = combine(p1, p2)
		if not isp(c1) or not isp(c2):
			return False
	return True

def twos():
	for p1, p2 in combinations(PS, r=2):
		if v2([p1], [p2]):
			yield set([p1, p2])

def threes():
	for p1, p2, p3 in combinations(PS, r=3):
		if v2([p1, p2], [p3]):
			yield [p1, p2, p3]

def fours():
	for seq1, seq2 in combinations(twos(), r=2):
		if v2(seq1, seq2):
			yield set(seq1) | set (seq2)

def fives():
	for p, seq in product(PS, fours()):
		if v2([p], seq):
			print sorted(set([p]) | seq)

print threes()

