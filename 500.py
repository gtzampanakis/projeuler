from itertools import *

from sieve import *

D = 500500507

r = [2,2,2,3,5]

N = len(r)

def prod(s):
	r = 1
	for x in s:
		r *= x
	return r

def fastmod(s):
	r = len(s)/2

	if r<=1:
		return prod(s) % D

	a,b = s[:r], s[r:]
	return (fastmod(a) * fastmod(b))%D

K = prod(r)

def calc_ds(n):
	r = []
	for x in xrange(1, n+1):
		if n%x==0:
			r.append(x)
	return r

ds = set()

for rlen in xrange(0, N+1):
	for comb in combinations(r, rlen):
		print comb, prod(comb)
		ds.add(prod(comb))

a = calc_ds(K)
b = sorted(ds)
diff = sorted((set(b) - set(a)) | (set(a) - set(b)))

print
print K
print a
print b
print len(a)
print len(b)
print diff

ps = []

E = 500500 * 0

# for pi, p in enumerate(gen_primes(), 1):
# 	ps.append(p)
# 	if pi == E:
# 		break
# 
# assert len(ps) == E
# 
# print fastmod(ps)

print fastmod([2 for _ in xrange(E-1)])

def ndcomb(bes, k):
	if k == 1:
		print k, len(bes)
	if k == 2:
		print k

print
ndcomb( [
	[2,2],
	[3,1],
	[5,1],
], 1)
