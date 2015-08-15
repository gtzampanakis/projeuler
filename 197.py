import itertools
import scipy as s

def f(x):
	c = 1e-9
	expon = 30.403243784 - x**2
	infloor = 2 ** expon
	return s.floor(infloor) * c

def u():
	arg = -1
	while True:
		yield arg
		arg = f(arg)


for i, ui in enumerate(u()):
	if i % 2000 in (0, 1):
		print i, ui
