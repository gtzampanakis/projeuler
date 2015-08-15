import random, itertools, collections

f = range(1, 5)
s = range(1, 7)

f_sum_to_p = collections.defaultdict(float)
s_sum_to_p = collections.defaultdict(float)

for rolls in itertools.product(f, repeat = 9):
	f_sum_to_p[sum(rolls)] += .25**9

for rolls in itertools.product(s, repeat = 6):
	s_sum_to_p[sum(rolls)] += (1./6)**6

print sum(f_sum_to_p.values())

print sum(s_sum_to_p.values())

p_win = 0.

for f, s in itertools.product(f_sum_to_p.keys(), s_sum_to_p.keys()):
	if f > s:
		p_win += f_sum_to_p[f] * s_sum_to_p[s]

print p_win


