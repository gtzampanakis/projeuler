import itertools, random
import scipy as s
import scipy.ndimage as sn

M = 30
BELLS = 50
MOVEMENTS = [1, 2, 3, 4]



sum_of_empty = 0
rm = range(M)

psi = s.zeros((M, M))
for mc_round in itertools.count():
	positions = [list(p) for p in itertools.product(rm, repeat = 2)]
	for bell in range(BELLS):
		for position in positions:
			direction = random.sample(MOVEMENTS, 1)[0]
			if direction == 1:
				position[0] += 1
			elif direction == 2:
				position[0] -= 1
			elif direction == 3:
				position[1] += 1
			elif direction == 4:
				position[1] -= 1
			if position[0] == -1:
				position[0] = 1
			if position[0] == M:
				position[0] = M - 2
			if position[1] == -1:
				position[1] = 1
			if position[1] == M:
				position[1] = M - 2
	psi[:,:] = 0
	for position in positions:
		psi[position[0], position[1]] += 1
	sum_of_empty += (psi == 0).sum()
	if mc_round % 5 == 0:
		print '{est:.7f}'.format(est = float(sum_of_empty) / float(mc_round + 1))




