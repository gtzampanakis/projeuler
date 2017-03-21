from itertools import *
from collections import defaultdict
from pprint import pprint

class S:
	def __init__(self, a):
		self.a = a
	def __str__(self):
		return 'sqrt(%s)' % self.a

def yz(a,b,c):
	newd = (a.a - c**2)/b
	m = 1
	while True:
		if ((m+1)*newd-c)**2 > a.a:
			break
		m += 1
	return m, m*newd-c, newd

def contfrac(a):
	f0 = int(a.a**.5)
	f = []
	bcs = []
	b,c = 1,f0
	while True:
		if (b,c) in bcs:
			return f0, f
		fi,y,z = yz(a,b,c)
		f.append(fi)
		bcs.append((b,c))
		b,c = z,y

def conv(a):
	f0, f = contfrac(a)

	yield f0,1

	res = f[0]*f0+1, f[0]
	prev = res
	pprev = f0, 1
	yield res

	cyc = cycle(range(0, len(f)))
	cyc.next()
	for i in cyc:
		res = (
			f[i]*prev[0]+pprev[0],
			f[i]*prev[1]+pprev[1]
		)
		yield res
		pprev = prev
		prev = res

maxx = -1
argmax = -1
for d in xrange(2, 1000+1):
	if d**.5 == int(d**.5):
		continue
	for hi, ki in conv(S(d)):
		if hi**2-1 == d*ki**2:
			if maxx < hi:
				maxx = hi
				argmax = d
			break
	else:
		print d, n2conv[d], "Failed to satisfy Pell's equation"

print maxx
print argmax

