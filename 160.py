from pprint import pprint
from math import factorial

def fastpow(b, e, prec):
	if e == 0:
		return 1%prec
	elif e == 1:
		return b%prec
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
	tenprec = 10**prec
	if n <= tenprec:
		return slowfactnz1(n, prec)

	ocs = {}
	for s in xrange(0, tenprec):
		ocs[s] = 0
	
	pprint(ocs)

# part with 00 in the end
	maxn00 = n / tenprec - 1 # if n=258xx this will give 257
	for s in ocs:
		if s != 0:
			ocs[s] = maxn00+1 # +1 to account for the zero prefix
		elif s == 0:
			ocs[s] = maxn00
	
	r = 1

	ni = (maxn00+1) * tenprec
	while ni <= n:
		r = r*ni
		r = removez(r)
		r %= tenprec
		ni += 1

	return r % tenprec
	
for n in xrange(1, 500, 3):
	assert slowfactnz1(n, 5) == slowfactnz2(n, 5)

print fastfactnz(25834, 2)

