from collections import defaultdict
from pprint import pprint
from math import factorial

def fastpow(b, e, prec):
	if e <= 10:
		return (b**e)%prec
	ek = int(e**.5)
	r = e - ek**2
	assert r >= 0
	return ( fastpow(fastpow(b, ek, prec), ek, prec) * fastpow(b, r, prec) ) % prec

def rfact(n, prec):
	if n <= 1: return 1
	r = 1
	for ni in xrange(1, n+1):
		r *= ni
	return r

def slowfactnz1(n, prec):
	# print 'Starting slowfactnz1 with n,prec:', n, prec

	if n == 0:
		return 1

	ni = 1
	r = 1
	n5removed = 0


	while 1:
		nw = ni
		if nw%10 in (0,5):
			while nw%5 == 0:
				nw /= 5
				n5removed += 1
		elif nw%10 in (2,6):
			nw = 1
		else:
			pass
		r = (r * nw) % 10**prec
		if ni == n:
			break
		ni += 1
	
	ni = 1
	while 1:
		nw = ni
		if nw%10 in (2,6):
			while n5removed and nw%2 == 0:
				nw /= 2
				n5removed -= 1
			r = (r * nw) % 10**prec
		if ni == n:
			break
		ni += 1

	return r % 10**prec

def removez(n):
	while n%10 == 0:
		n /= 10
	return n

def slowfactnz2(n, prec):
	f = factorial(n)
	f = removez(f)
	return f % 10**prec

def fastfactnz(n, prec):

# assume n=25834

	tenprec = 10**prec
	if n <= tenprec:
		return slowfactnz1(n, prec)

	ocs = {}
	for s in xrange(0, tenprec):
		ocs[s] = 0
	
# part with 00 in the end
	maxn00 = n / tenprec - 1 # if n=258xx this will give 257
	for s in ocs:
		if s != 0:
			ocs[s] = maxn00+1 # +1 to account for the zero prefix
		elif s == 0:
			ocs[s] = maxn00
	
# we have accounted for 1 ... 25799

	rest = n - (maxn00+1)*tenprec

# "rest" is equal to 25834 - 25800 = 34

	for s in xrange(0, rest+1):
		ocs[s] += 1

# we have accounted for 1 ... 25834

	#pprint(ocs)

	n5s = n/5

	print n5s

	def add_accordingly():
		to_add = defaultdict(int)
		nmoved = 0
		for s in ocs:
			if s%10 in (2,6):
				noc = ocs[s]
				if noc:
					if nmoved+noc > n5s:
						noc = n5s-nmoved
					to_add[s/2] += noc/2
					to_add[s/2 + tenprec/2] += noc-noc/2
					to_add[s] -= noc
					nmoved += noc
		
		for s,a in to_add.iteritems():
			ocs[s] += a

	add_accordingly()

	#pprint(ocs)


	# for s, noc in ocs.iteritems():
	# 	if s%10 not in (0,5):
	# 		r = r * fastpow(s, noc, tenprec)
	# 		r %= tenprec

	ocs = dict( (s,noc) for s,noc in ocs.iteritems() if s%10 not in (0,5) and noc )

	def mult(ocs):
		r = 1
		while 1:
			# ocs = dict( (s,noc) for s,noc in ocs.iteritems() if noc )
			min_ = min(ocs.itervalues())
			ss = set(ocs.keys())
			# for s in bc-ss:
			# 	b /= s
			# bc = ss
			bc = set()
			b = 1
			for s in ocs:
				b = (b * s) % tenprec
				bc.add(s)
			for s in ss:
				ocs[s] -= min_
				assert ocs[s] >= 0
				if ocs[s] == 0:
					del ocs[s]
			ra = fastpow(b, min_, tenprec)
			r = (r * ra) % tenprec
			if not ocs:
				break

		return r

	r = mult(ocs)

	r *= fastfactnz(n5s, prec)

	return r % tenprec

	
for n in xrange(1, 500, 3):
	assert slowfactnz1(n, 5) == slowfactnz2(n, 5)

assert fastfactnz(10**7, 4) == 4688

assert fastfactnz(10**12, 5) == 16576

