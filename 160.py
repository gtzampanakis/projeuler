def fastpow(b, e, prec):
	if e == 0:
		return 1%prec
	elif e == 1:
		return b%prec
	ek = int(e**.5)
	r = e - ek**2
	assert r >= 0
	return ( fastpow(fastpow(b, ek, prec), ek, prec) * fastpow(b, r, prec) ) % prec

def rfact(n):
	if n <= 1: return 1
	r = 1
	for ni in xrange(1, n+1):
		r *= ni
	return r

print rfact(6)
