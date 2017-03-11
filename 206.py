import sys
import re

dis = [11, 9, 7, 5, 3]
dts = [ 5, 6, 7, 8, 9]

dis = [11, 9, 7, 5, 3]
dts = [ 5, 6, 7, 8, 9]

cands = [0]
prev_di = 1
for di, dt in reversed(zip(dis, dts)):
	print di, dt
	new_cands = []
	for cand in cands:
		for i in xrange(1, 100):
			z = i * 10**(prev_di) + cand
			z2 = z**2
			strz2 = str(z2)
			if strz2[-di] == str(dt):
				if re.match(r'1.2.3.4.5.6.7.8.9.0', strz2):
					print 'solution:', z
					sys.exit()
				new_cands.append(z)
	cands = new_cands
	prev_di = di


