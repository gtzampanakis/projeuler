from itertools import *
from collections import *
from pprint import pprint
import pmemoize
import random

class S:
	def __init__(self, a):
		self.a = a
	def __str__(self):
		return 'sqrt(%s)' % self.a

# @pmemoize.MemoizedFunction
def yz(a,b,c,m):
	# assert (a.a - c**2) % b == 0
	newd = (a.a - c**2)/b
	return c-m*newd, newd

class N:
	def __init__(self, *args):
		for k,v in zip(['parent', 'checknode', 'm', 'y', 'z', 'm0'], args):
			setattr(self, k, v)
	def lineage(self):
		lineage = []
		cn = self
		while True:
			lineage.append(cn.m)
			cn = cn.parent
			if cn == 'H':
				break
		return list(reversed(lineage))
	def __unicode__(self):
		return unicode(self.__dict__)
	def __repr__(self):
		return unicode(self.__dict__)

def approve_node(n, maxm):
	if n.y < 0 and n.z > 0 and abs(n.y) < maxm and abs(n.z) < maxm:
		return True
	return False

def bfslike(a, maxm):

	frontier = ['H']
	for _ in xrange(2):
		for fni, fn in enumerate(frontier):
			if fn == 'H':
				a0 = int(a.a**.5)
				b = 1
				c = a0
				new_frontier = []
				for m in chain([maxm], xrange(1, maxm)):
					y,z = yz(a,b,c,m)
					new_node = N(fn, None, m, y, z, m)
					new_node.checknode = new_node
					if approve_node(new_node, maxm):
						new_frontier.append(new_node)
				frontier = new_frontier
			else:
				for m in chain([maxm], xrange(1, maxm)):
					b =  fn.z
					c = -fn.y
					y,z = yz(a,b,c,m)
					if m == fn.m0:
						if fn.checknode.y == y and fn.checknode.z == z:
							return fn.lineage()
					new_node = N(fn, fn.checknode, m, y, z, fn.m0)
					if approve_node(new_node, maxm):
						new_frontier.append(new_node)
				frontier = new_frontier
	
if 0:
	for n in xrange(2, 50):
		if n**.5 == int(n**.5):
			continue
		print n, find(S(n))

if 1:
	nodds = 0
	maxm = 10
	for n in xrange(2, 10000+1):
		if n**.5 == int(n**.5):
			continue
		res = bfslike(S(n), maxm)
		if maxm <= max(res):
			maxm += 2
		if not res:
			print 'Failed'
			break
		if len(res) % 2 == 1:
			nodds += 1
		print n, res

print nodds
