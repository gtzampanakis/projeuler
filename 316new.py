import itertools


d = 3

exp = 0.

for a in itertools.count(1):

	p = 10**(-3) - (a-3 if a-3 >= 0 else 0)*10**-6

	exp += a * p
	print a, exp

