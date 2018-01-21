import pmemoize
import sieve

def large_xrange(start, end):
	val = start
	while True:
		yield val
		val += 1
		if val == end:
			break

def primes_less_than(n):
	for i in large_xrange(2, n):
		if isprime(i):
			yield i

def prime_factors(n):
	for p in primes_less_than(n+1):
		while n % p == 0:
			yield p
			n /= p
			if n == 1: return

def prime_factors_2(n):
        for p in sieve.gen_primes():
		while n % p == 0:
			yield p
			n /= p
			if n == 1: return
def isprime(n):
	if n == 2: return True
	return all(n % i != 0 for i in large_xrange(2, n))

def prod(seq):
	found = False
	p = 1
	for n in seq:
		found = True
		p *= n
	if found:
		return p
	else:
		raise IndexError, 'empty sequence passed'

def divisors(n, proper = False):
	result = [1]
	if not proper: result.append(n)
	for pd in xrange(2, n):
		pds = pd * pd
		if pds > n:
			break
		if n % pd == 0:
			result.append(pd)
			if pds != n:
				result.append(n / pd)
	return result

def triangle_number(i):
	return i * (i+1) / 2

def is_abundant(n):
	if sum(divisors(n, proper = True)) > n:
		return True
	return False

def fib():
	prev = [1,1]
	yield prev[0]
	yield prev[1]
	while True:
		s = sum(prev)
		yield s
		prev[0] = prev[1]
		prev[1] = s

def primes_less_than_by_sieve(n):
	from primes import primes
	sieve = set(xrange(2, n))

	for prime in primes:
		if prime*prime > n:
			break
		for multiple in xrange(prime + prime, n, prime):
			if multiple in sieve:
				sieve.remove(multiple) 

	return sieve

def thue_morse():
	i = 0
	values = [0]
	yield values[-1]
	while True:
		i += 1
		if i % 2 == 0:
			values.append(values[i/2])
		else:
			values.append(1 - values[(i-1)/2])
		yield values[-1]


def denominations(total, coins_available):
	import itertools
	check_coins_available(coins_available)
	if coins_available == []:
		return [total]
	coin = coins_available[0]
	coins_left = coins_available[1:]
	starting_value = total / coin
	numbers_of_coins = xrange(starting_value, -1, -1)
	result = []
	for number_of_coins in numbers_of_coins:
		rem_sum_to_pass = total - number_of_coins * coin
		from_subcall = denominations(rem_sum_to_pass, coins_left)
		for l in itertools.product([number_of_coins], from_subcall):
			result.append(l)
	return result

def denominations_count_only(total, coins_available):
	import itertools
	check_coins_available(coins_available)
	if coins_available == []:
		return 1
	coin = coins_available[0]
	coins_left = coins_available[1:]
	starting_value = total / coin
	numbers_of_coins = xrange(starting_value, -1, -1)
	result = 0
	for number_of_coins in numbers_of_coins:
		rem_sum_to_pass = total - number_of_coins * coin
		from_subcall = denominations_count_only(rem_sum_to_pass, coins_left)
		result += from_subcall
	return result

def denominations_count_only2(total, coins_available):
	import itertools
	check_coins_available(coins_available)
	if coins_available == []:
		return 1
	coin = coins_available[0]
	coins_left = coins_available[1:]
	starting_value = total % coin
	ending_value = total + coin
	rem_sums_to_pass = xrange(starting_value, ending_value, coin)
	result = 0
	for rem_sum_to_pass in rem_sums_to_pass:
		from_subcall = denominations_count_only2(rem_sum_to_pass, coins_left)
		result += from_subcall
	return result

def flatten_tuple(t):
	result = []
	working_on = t
	while True:
		head = working_on[0]
		tail = working_on[1]
		result.append(head)
		if isinstance(tail, tuple):
			working_on = tail
		else:
			result.append(tail)
			return result

def check_coins_available(coins_available):
	if 1 in coins_available:
		raise ValueError("coins_available should not include the number 1," \
											"but it will be used anyway by the function")

def denominations_flat(total, coins_available):
	check_coins_available(coins_available)
	combs = denominations(total, coins_available)
	for comb in combs:
		yield flatten_tuple(comb)
	
def pandigitals(n, descending = False):
	""" Returns the sorted n-digit pandigitals """
	import itertools
	if not (n >= 1 and n <= 9):
		raise ValueError("n should be between 1 and 9 inclusive")
	if not descending:
		r = range(1, n+1)
	else:
		r = range(n, 0, -1)
	return (int(''.join(str(d) for d in comb)) for comb in itertools.permutations(r, n))

@pmemoize.MemoizedFunction
def bincoeff(n, k):
    """ Binomial coefficient. """
    if k == 0:
        return 1
    elif 2*k > n:
        return bincoeff(n,n-k)
    else:
        e = n-k+1
        for i in range(2,k+1):
            e *= (n-k+i)
            e /= i
        return e

@pmemoize.MemoizedFunction
def compsum(m, n):
    """ Count of n-tuples of positive integers (order is important) with sum
    equal to m. """
    return bincoeff(m-1, n-1)
