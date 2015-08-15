import random

p = 2

TICKETS = range(0, p)

random.shuffle(TICKETS)

print TICKETS

outs = 0
for pt in xrange(p):
	print pt
	prev = TICKETS[:pt]
	next_ = TICKETS[pt+1:]
	minnext = next_ and min(next_)
	maxprev = prev and max(prev)
	if minnext > maxprev or maxprev == []:
		pass
	else:
		outs += 1
		index_to_remove = TICKETS.index(maxprev)
		TICKETS[index_to_remove] = pt
		TICKETS[pt] = None
	print pt, prev, next_, minnext, maxprev

print outs

