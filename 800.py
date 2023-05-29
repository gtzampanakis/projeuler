from math import ceil, log, e

B = 800800
E = 800800

E = log(B) * E
B = e

primes = [2, 3]

def p(i):
    if i < len(primes):
        return primes[i]
    c = primes[-1] + 2
    while 1:
        found_divisor = False
        stop_point = c**.5
        for p in primes:
            if p > stop_point:
                break
            if c % p == 0:
                found_divisor = True
                break
        if not found_divisor:
            primes.append(c)
            return c
        else:
            c += 2

def main():
    i = 0
    while 1:
        p1 = p(i)
        logp1 = log(p1)
        p2 = p(i+1)
        logp2 = log(p2)
        if p1*logp2 + p2*logp1 > E:
            break
        i += 1
    i = i
    j = i+1
    r = 0
    print('Found starting point:', i)
    while 1:
        if i < 0:
            break
        p1 = p(i)
        p2 = p(j)
        logp1 = log(p1)
        logp2 = log(p2)
        q = p1*logp2 + p2*logp1
        if q < E:
            j += 1
        else:
            j -= 1
            r += (j-i)
            print('new i:', i)
            i -= 1
    print(r)

main()
