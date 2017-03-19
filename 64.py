from itertools import *
import pmemoize
import random

class S:
	def __init__(self, a):
		self.a = a
	def __str__(self):
		return 'sqrt(%s)' % self.a

@pmemoize.MemoizedFunction
def yz(a,b,c,m):
	# assert (a.a - c**2) % b == 0
	newd = (a.a - c**2)/b
	return c-m*newd, newd

@pmemoize.MemoizedFunction
def inf(a):
	a0 = int(a.a**.5)
	b = 1
	c = a0
	ms = cycle([1,1,1,4])
	for _ in xrange(30):
		m = ms.next()
		y,z = yz(a,b,c,m)
		print m,y,z
		a=a
		b=z
		c=-y

def find(a):
	for ms in product(range(1, 9), repeat=6):
		ms = list(ms)
		ms_used = []
		yzs = []
		a0 = int(a.a**.5)
		b = 1
		c = a0
		while ms:
			m = ms.pop()
			y,z = yz(a,b,c,m)
			if yzs and (y,z) == yzs[0]:
				return len(ms_used), ms_used
			yzs.append((y,z))
			ms_used.append(m)
			a=a
			b=z
			c=-y
	
for n in xrange(2, 50):
	if n**.5 == int(n**.5):
		continue
	print n, find(S(n))
