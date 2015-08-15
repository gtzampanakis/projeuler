def pentag():
	n = 3
	while True:
		yield n, 3*n-2, n*(3*n-1)/2
		n += 1

pentagonals_encountered = set()
sums_encountered = { }
for n, dn, Pn in pentag():
	if Pn in sums_encountered:
		print sums_encountered[Pn]
		print sums_encountered[Pn][0] - sums_encountered[Pn][1]
		break
	for pp in pentagonals_encountered:
		Pm_cand = Pn - pp
		if Pm_cand in pentagonals_encountered:
			Pj = Pn
			Pk = pp
			Pm = Pj - Pk
			s = Pj + Pk
			sums_encountered[s] = (Pj, Pk)

	pentagonals_encountered.add(Pn)




