import itertools
import scipy as s
import pylab
import scipy.ndimage.filters as f

N = 100
assert N % 2 == 0 and N >= 2

distr = [ ]

corn = 1./36
side = 4./36
self = 1 - 4*corn - 4*side
kernel = s.array([
			[corn, side, corn],
			[side, self, side],
			[corn, side, corn],
		])

mask_to_reset_diagonal = (s.eye(N) == 1)

state = s.zeros((N, N))
state[0, N/2] = 1.
sum_distr = 0.
previous_E = None
for r in itertools.count():
	tr = state.trace()
	new_distr = (1.-sum_distr) * tr
	distr.append(new_distr)
	sum_distr += new_distr
	if r % 250 == 0:
		E = s.dot(s.arange(len(distr)), distr)
		print r, E
		if previous_E is not None and abs(E - previous_E) < 1e-9:
			break
		previous_E = E
	state[mask_to_reset_diagonal] = 0.
	s.multiply(state, (1./(1. - tr)), out = state)

	state = f.convolve(state, kernel, mode = 'wrap')

pylab.bar(s.arange(len(distr)), distr); pylab.show()
