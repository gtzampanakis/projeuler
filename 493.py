from pprint import pprint
from scipy.special import binom as bin

pdf = [ ]

tot = bin(70, 20)

def cg(k):
	if k == 1:
		return 0.
	return bin(k*10, 20) - sum( cg(m) * bin(k, m) for m in xrange(2, k) ) 

for k in xrange(2, 8):
	c = cg(k) * bin(7, k)
	pdf.append(c)
	

pprint(pdf)

print sum(x*y for x, y in zip(range(2,8), pdf)) / tot



