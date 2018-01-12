import lib
import math
import pmemoize

MOD = 1234567891

@pmemoize.MemoizedFunction
def pf(n):
    return list(lib.prime_factors_2(n))

@pmemoize.MemoizedFunction
def sig(n):
    pfs = pf(n)
    print pfs
    result = []
    distinct = set(pfs)
    for di in distinct:
        result.append(sum(1 for ca in pfs if ca == di))
    return sorted(result)

@pmemoize.MemoizedFunction
def bincoeff(n, k):
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
def H(m, n):
    return G(m, n) - G(m-1, n)

@pmemoize.MemoizedFunction
def fastqs(m):
    # return sorted(set(m/i for i in xrange(1, int(m**.5)+1)))
    s = set(m/i for i in xrange(1, int(m**.5)+1))
    l = list(s)
    l.sort()
    return l

@pmemoize.MemoizedFunction
def G(m,n):
    if m <= 1:
        r = 0

    elif n == 1:
        r = m-1

    else:
        qs = fastqs(m)
        r = 0
        if 0:
            z, w = n/2, n-n/2
            for i in xrange(2, m+1):
                r += ( H(i, z) ) * G(m/i, w)
        else:
            if 0:
                for i in xrange(2, m+1):
                    r += G(m/i, n-1)
            else:
                s = m
                q = 1
                qsi = -1
                while True:
                    e = m/(q+1)
                    if s != e:
                        r += ( (s-e) * G(q, n-1) )
                        s = e
                    # if q > m/2:
                    #     q = m
                    # else:
                    #     q += 1
                    if qsi == -1 and q == qs[0]:
                        qsi = 0
                    if qsi > -1:
                        q = qs[qsi]
                        qsi += 1
                    else:
                        q += 1
                    if q==m:
                        break

    return r

@pmemoize.MemoizedFunction
def F(m,n):
    r = 0
    q = int(math.log(m, 2))
    for i in xrange(1, q+1):
        r += G(m, i) * bincoeff(m, i)
    return r

e = 3
print F(10**e, 10**e) % MOD

# print sig(5892325)

