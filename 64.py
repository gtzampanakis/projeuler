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

nodds = 0
for n in xrange(2, 10000+1):
	if n**.5 == int(n**.5):
		continue
	res = contfrac(S(n))[1]
	if len(res) % 2 == 1:
		nodds += 1

print nodds
