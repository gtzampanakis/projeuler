import scipy as s

M = 250250
A = [int(str(k)[-3:])**k for k in xrange(1, M+1)]
Ad = [str(n)[-3:] for n in A]

for i, el in enumerate(Ad):
	print i+1, el

print len(set(Ad))
