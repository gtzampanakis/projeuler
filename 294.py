import collections, sys, fractions, copy, itertools
from pprint import pprint
from memoize import MemoizedFunction
import scipy

DIV = 10**9
M = 23
# n = 42
EXH = 0

def ld(n):
	return sum(int(c) for c in str(n))


def accelAsc(n):
	a = [0 for i in range(n + 1)]
	k = 1
	y = n - 1
	while k != 0:
		x = a[k - 1] + 1
		k -= 1
		while 2*x <= y:
			a[k] = x
			y -= x
			k += 1
		l = k + 1
		while x <= y:
			a[k] = x
			a[l] = y
			yield a[:k + 2]
			x += 1
			y -= 1
		a[k] = x + y
		y = x + y - 1
		yield a[:k + 1]


def compositions(t, s):
	"""knuth 7.2.1.3"""
	q = [0] * (t+1)
	r = None
	q[0] = s
	while True:
		yield q[:]
		if q[0] == 0:
			if r==t:
				break
			else:
				q[0] = q[r] - 1
				q[r] = 0
				r = r + 1
		else:
			q[0] = q[0] - 1
			r = 1
		q[r] = q[r] + 1

### for k in xrange(1,24):
### 	for i, comp in enumerate(compositions(10,k), 1):
### 		pass
### 		### if 0 and i % 100000 == 0:
### 		### 	print i, comp
### 	print k, i
### 
### sys.exit()

INDICES = range(0,10)

def partitions(n):
	arr = scipy.zeros(11)
	yielded = set()
	for part in accelAsc(n):
		print part
		for perm in itertools.permutations(part):
			print perm
			if perm not in yielded:
				lenperm = len(perm)
				for comb in itertools.combinations(INDICES, lenperm):
					arr.fill(0)
					arr[list(comb)] = perm
					yield arr
				yielded.add(perm)

### for i, part in enumerate(partitions(M)):
### 	if i % 1000 == 0:
### 		print i, part
### print i
### 
### sys.exit()


@MemoizedFunction
def modp10(psi):
	if psi == 0:
		return 10**0 % M
	return (10*modp10(psi-1)) % M


MODS = [ modp10(psi) for psi in xrange(0, 22) ]

def modp10_2(psi):
	return MODS[psi%22]

def old_key_to_new_key(keyold, x, psi):
	dold, mold = keyold
	if dold == M:
		return None
	d = dold + x
	if d > M:
		return None
	m = (mold + (x*modp10(psi-1)))%M
	return (d, m)

def gcd(li):
	return reduce(
			fractions.gcd,
			li,
	)

@MemoizedFunction
def distr(n):

	Told = {
		(0, 0) : 1,
	}

	found = 0
	for psi in xrange(1, n+1):
		T = collections.defaultdict(int)
		T.update(Told)
		found_for_psi = 0

		for x in xrange(1, 10):
			for keyold, count in Told.iteritems():
				key = old_key_to_new_key(keyold, x, psi)

				if key is not None:

					if x != 0 and key[0]==M and key[1]==0:
						found_for_psi += count

					T[key] += count
					T[key] %= DIV

		if 0 and psi % 100 == 0:
			print psi, len(T)
		found += found_for_psi
		Told = T

	return T

## pprint(distr(10))


class hashabledict(dict):
	def __key(self):
		return tuple((k,self[k]) for k in sorted(self))
	def __hash__(self):
		return hash(self.__key())
	def __eq__(self, other):
		return self.__key() == other.__key()

@MemoizedFunction
def distr2(Ds, n, t):
	""" Pass n as the last D's digits. """
	T = collections.defaultdict(int)

	for current_M in xrange(1, M+1):
		for comp in compositions(t-1,current_M):
			keys_found = [ ]
			for dtofind, D in zip(comp, Ds):
				keys_found.append([ ])
				for key, count in D.iteritems():
					d,m = key
					if d == dtofind:
						keys_found[-1].append(key)
			for key_comb in itertools.product(*keys_found):
				# print key_comb
				newd = 0
				newm = 0
				newcount = 1
				for key, psi, D in zip(key_comb, itertools.count(n*(t-1), -n), Ds):
					d,m = key
					newm += ( modp10_2(psi) * m ) % M
					newd += d
					newcount *= D[key]
				newm %= M
				new_key = (newd, newm)
				T[new_key] += newcount
				T[new_key] %= DIV

	T[(0,0)] = 1
	return hashabledict(T)

def compT(T1, T2):
	return all(T1[key] == T2[key] for key in T1)


### T1 = distr(40)
### T2 = distr2([distr2([distr2([distr(5)]*2, 5, 2)]*2, 10, 2)]*2, 20, 2)
### 
### T1 = distr(20)
### T2 = distr2([distr(17), distr(3)], 3, 2)
### 
### print compT(T1, T2)
### 
### 1/0

Ds = [ ]
bs = [ ]
target = 11**12
final_target = target
while True:
	b = 1
	k = 2
	T = distr(b)
	for p in itertools.count(1):
		if b*k > target:
			Ds.append(T)
			bs.append(b)
			break
		to_pass = hashabledict(T)
		T = distr2((to_pass,to_pass), b, k)
		b *= k
		print b, target, len(T)
		if 0 and b < 1000:
			print compT(T, distr(b))
	target = target - b
	if target < 0:
		print target
		sys.exit()
	print 'new target:', target
	if sum(bs) >= final_target:
		break
	
def r(t1n1, t2n2):
	t1, n1 = t1n1
	t2, n2 = t2n2
	return distr2((hashabledict(t1),hashabledict(t2)), n2, 2), n1+n2

### print 'Checking...'
### 
### ex = distr(final_target)
my = reduce(r, list(zip(Ds, bs)))
print my[0][(23,0)]
### 
### print compT(ex, my[0])


if EXH:
	print
	found = 0
	for i in xrange(1, 10**n):
		if i % M == 0 and ld(i) == M:
			# print i
			found += 1
	print n, found

