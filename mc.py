from random import random as rnd

MC_REPS = 80000
y_wins = 0

for repi in xrange(MC_REPS):
	s = 0
	x_set = False
	while True:
		u = rnd()
		s += u
		if not x_set and s > 1:
			x = u
			x_set = True
		if x_set and s > 2:
			y = u
			if y > x:
				y_wins += 1
			break


print float(y_wins) / MC_REPS



