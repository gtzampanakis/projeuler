from itertools import *

class S:
	def __init__(self, a):
		self.a = a
	def __str__(self):
		return 'sqrt(%s)' % self.a

def xyz(a,b,c,m):
	assert (a.a - c**2) % b == 0
	newd = (a.a - c**2)/b
	return m*newd/newd, c-m*newd, newd

def inf(a):
	a0 = int(a.a**.5)
	b = 1
	c = a0
	ms = cycle([1,3,1,8])
	for _ in xrange(30):
		m = ms.next()
		x,y,z = xyz(a,b,c,m)
		print x,y,z
		a=a
		b=z
		c=-y
	
inf(S(23))
