from itertools import *

def n1(n): return n*(n+1)/2
def n2(n): return n**2
def n3(n): return n*(3*n-1)/2
def n4(n): return n*(2*n-1)
def n5(n): return n*(5*n-3)/2
def n6(n): return n*(3*n-2)

def ch(n1, n2):
	return n1%100 == n2/100

fns = [n1, n2, n3, n4, n5, n6]

cs = []

for fn in fns:
	nas = []
	for n in count(1):
		na = fn(n)
		if len(str(na)) == 4:
			nas.append(na)
		elif len(str(na)) > 4:
			break
	cs.append(nas)

def validseq(order, r):
	if r == 1:
		for c in cs[order[0]]:
			yield [c]
	else:
		clefts = validseq(order, r-1)
		if r-1 < len(order):
			crights = cs[order[r-1]]
		elif r-1 == len(order):
			crights = clefts
		for cleft, cright in product(clefts, crights):
			if ch(cleft[-1], cright):
				yield cleft + [cright]

def solve():
	for order in permutations(range(6), r=6):
		for s in validseq(order, 6):
			if ch(s[-1], s[0]):
				print order, s, sum(s)
				return

solve()

