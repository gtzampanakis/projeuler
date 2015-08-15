import cmath, math, scipy, random
from pprint import pprint

X = 0
U = 1

PI = math.pi

TS = .0005

UP = 99.08340778978892
AREA = 7952.259911637154

widths = scipy.linspace(0, 100., 10000)
max_height_per_width = [-100. for width in widths]

SQ_WIDTH = widths[1] - widths[0]

G = -9.81j

angles = scipy.linspace(PI/2, 0., 500)

parts = [[100j, cmath.rect(20., phi)] for phi in angles]

argmaxs_t = [ part[U].imag / -G.imag for part in parts ]

t = 0.

INDS_TO_PLOT = range(0, len(parts), 20)

parts_xy_to_plot = [list() for ind_to_plot in INDS_TO_PLOT]

while True:
	done_mod = False
	for parti, part in enumerate(parts):
		if part[X].imag <= 0:
			if len(part) == 2:
				part.append(t)
			continue

		width_quant = int(part[X].real / SQ_WIDTH)
		max_height_so_far = max_height_per_width[width_quant]

		current_height = part[X].imag

		if current_height > max_height_so_far:
			max_height_per_width[width_quant] = current_height

		part[X] += part[U] * TS
		part[U] += G * TS

		if parti in INDS_TO_PLOT:
			if int(t / .05) > len(parts_xy_to_plot[INDS_TO_PLOT.index(parti)]):
				# if t > argmaxs_t[parti]:
					parts_xy_to_plot[INDS_TO_PLOT.index(parti)].append((part[X].real, part[X].imag))

		done_mod = True
	if not done_mod:
		break
	t += TS

	# print parts[-1]

xy = [o for o in zip(widths, max_height_per_width) if o[1] != -100.]

area = 0.
for x, y in xy:
	area += y * SQ_WIDTH

print area


sample = random.sample(xy, 2000)	

import pylab

pars = [[p[0] for p in sample], [p[1] for p in sample], 'k.']

for ind_to_plot, series in zip(INDS_TO_PLOT, parts_xy_to_plot):
	print angles[ind_to_plot], argmaxs_t[ind_to_plot]
	pars += [
		[p[0] for p in series], [p[1] for p in series], 'g.',
	]

def exact(sx):
	### result = 20.**2/-G.imag  -  (-G.imag * sx**2) / (2*20.**2 * (math.cos(math.atan(20.**2/(-G.imag*sx))))**2)
	### result = 20.**2/-G.imag  -  (-G.imag * sx**2) / (2*20.**2 * (1./(1 + 20. ** 4 / (G.imag**2 * sx**2))))
	g = -G.imag
	uor2 = 20. ** 2
	### result = uor2/g  -  (g * sx**2) / (2*uor2 * (1./(1 + uor2 ** 2 / (g**2 * sx**2))))
	### result = uor2/g  -  (g * sx**2) / (2*uor2/(1 + uor2 ** 2 / (g**2 * sx**2)))
	### result = uor2/g  -  (g * sx**2) / ( 2*uor2 * g**2 * sx**2 / (uor2 ** 2 + g**2 * sx**2) )
	### result = uor2 / g - uor2 / 2 - (g**2 * sx**2) / (2 * uor2)
	result = uor2 / g   -   uor2 / (2*g)    -    g*sx**2 / (2*uor2)
	result = uor2 / (2*g)    -    g*sx**2 / (2*uor2)
	return result + 100.

xs = [p[0] for p in sample]
pars += [
	xs, [exact(x) for x in xs], 'y+'
]

pylab.plot(*pars)
			
			
pylab.show()

previous_height = None
volume = 0.
for width, height in xy:

	if previous_height is not None:
		hdiff = previous_height - height
		volume += PI * width ** 2 * hdiff

	previous_height = height

print
print t

print 'volume:', volume

