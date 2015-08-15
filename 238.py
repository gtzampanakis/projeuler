import scipy

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

imes = 2
digits = scipy.array(list(conc()) * times, dtype = scipy.int8)
cumsum_buffer = scipy.zeros(len(digits), dtype = scipy.int32)
R = digits.sum() / times
pk = scipy.zeros(R + 1, dtype = scipy.int32)

print 'Generated necessary sequence.'

for i, d in enumerate(digits):
	print i,
	ks = digits[i:].cumsum(out = cumsum_buffer[i:])
	ks = ks[ks <= R]
	to_assign = pk[ks]
	eq_to_zero = to_assign == 0
	to_assign[eq_to_zero] = i+1
	pk[ks] = to_assign
	n_done = (pk[1:] != 0).sum()
	print n_done, R
	if n_done == R:
		print 'Done!'
		break
	elif R - n_done <= 10:
		print 'Remaining:', scipy.where(pk[1:] == 0)

def sum_up_to(t):
	q = t / R
	r = t % R
	print 'q:', q, 'r:', r
	result = (pk[1:]).sum() * q + ((pk[1:])[:r]).sum()
	return result
	
print sum_up_to(1*10**3)
print sum_up_to(2*10**15)
