from scipy.special import binom

p4 = (36.*22*10) / (51.*50*49)

c52_4 = binom(52, 4)

print p4 * c52_4

c5 = binom(52, 5) * ( binom(5,4) * p4 - ( binom(binom(5,4), 2) * ( 36. * 22 * binom(10,2) / ( 51. * 50 * binom(49,2)))) )

print c5

