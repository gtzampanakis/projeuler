from math import sqrt
from decimal import *

getcontext().prec = 100

ending_length = 5
ending_mod = 10 ** ending_length
endings = set(k % ending_mod for k in xrange(300000))


def y(s):
	return Decimal(1+2*s*(s-1))

c = Decimal(int(y(10**12).sqrt()))

if c % 2 != 1:
	c -= 1

assert c % 2 == 1

two_c2 = 2*c**2

while True:
	should_be_square = (two_c2 - 1)
	if should_be_square % ending_mod in endings and should_be_square.sqrt() % 1 == 0:
		b = (1 + c) / 2
		print c, b
	two_c2 += 8*(c + 1)
	c += 2

