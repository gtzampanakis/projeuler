import scipy, itertools, random, pylab, time, collections

st = 2534198

T = 18886117
R = 80846691
d = int(2e15) / T
r = int(2e15) % T

def rg():
	s0 = 14025256
	s = s0
	while True:
		yield s
		s = (s**2) % 20300713
		if s == s0:
			break

def conc():
	for n in rg():
		for c in str(n):
			yield int(c)

#def conc():
#	r = range(10)
#	for i in xrange(10000):
#		yield random.sample(r, 1)[0]

def p(k):
	start = 0
	while True:
		s = 0
		for ni, n in enumerate(conc()):
			if ni >= start:
				s += n
				if s == k:
					return start + 1
				elif s > k:
					start += 1
					break

digits = list(conc())
digits = scipy.array(digits)
R = digits.sum()
pk = scipy.zeros(R+1, dtype = digits.dtype)

print 'Period calculated'

t1 = time.time()

for i, d in enumerate(digits):
	try:
		print i,
		cs = digits[i:].cumsum()
		if 0:
			for k in cs:
				if pk[k] == 0:
					pk[k] = i+1
		if 1:
			to_assign = pk[cs]
			to_assign[to_assign == 0] = i+1
			pk[cs] = to_assign
			n_done = (pk != 0).sum()
			print n_done, R
			if n_done == R:
				print 'Done!'
				break
			elif R - n_done <= 10:
				print 'Remaining:', scipy.where(pk == 0)
	except KeyboardInterrupt:
		break

def sum_up_to(t):
	q = t / R
	r = t % R
	print 'q:', q, 'r:', r
	result = (pk[1:]).sum() * q + ((pk[1:])[:r]).sum()
	return result
	
print sum_up_to(1*10**3)
print sum_up_to(2*10**15)
