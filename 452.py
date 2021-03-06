import lib
import math
import pmemoize
import sieve
import sys
import time

MOD = 1234567891

sys.setrecursionlimit(10**6)

@pmemoize.MemoizedFunction
def pf(n):
    return list(lib.prime_factors_2(n))

@pmemoize.MemoizedFunction
def sig(n):
    pfs = pf(n)
    result = []
    distinct = set(pfs)
    for di in distinct:
        result.append(sum(1 for ca in pfs if ca == di))
    result.sort()
    return result

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

    elif m < 2**n:
        return 0
    
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
        r += G2(m, i) * bincoeff(m, i)
    return r

@pmemoize.MemoizedFunction
def alk(a, l, k):
    return (a+l)**k

primes = set()
ps = [None]
pi_cache = [None, 0, 1]
for p in sieve.gen_primes():
    if p > 2:
        for c in xrange(ps[-1], p):
            pi_cache.append(len(ps)-1)
    ps.append(p)
    primes.add(p)
    if p > 10**5:
        break

cache = { }

@pmemoize.MemoizedFunction
def J(m, n, a):
    """
    Number of n-tuples with product <= m and smallest element >= a.  All
    elements have to be >= 2.
    """
    assert m >= 1
    assert n >= 0
    assert a >= 2

    if m <= 1:
        r = 0
    elif a > m:
        r = 0
    elif a**n > m:
        r = 0
    elif n == 1:
        r = m - a + 1
    elif n > 1:
        s = 0
        l = 0
        z = int(m**(1./n)) + 1
        while a+l <= z:
            k = 1
            while n>=k and m >= alk(a,l,k):
                if n == k:
                    s += 1
                else:
                    recurs = J(m/alk(a,l,k), n-k, a+l+1)
                    if recurs > 0:
                        s += recurs * bincoeff(n, k)
                k += 1
            l += 1

        r = s

    return r

@pmemoize.MemoizedFunction
def PHI(m, n):
    """
    Count of numbers <= m which are divisible by no pi, where i <= n.
    """
    if n == 0:
        r = int(m)
    elif n > 0:
        r = PHI(m, n-1) - PHI(m/ps[n], n-1)
    return r

@pmemoize.MemoizedFunction
def PI(m):
    if m == 1:
        return 0
    if m == 2:
        return 1
    # if m < len(pi_cache):
    #     return pi_cache[m]
    else:
        sq = int(m**.5)
        return PI(sq) + PHI(m, PI(sq)) - 1

@pmemoize.MemoizedFunction
def root(m, n):
    if n == 1:
        return m
    r = int(m**(1./n))
    while 1:
        if r**n > m:
            return r-1
        r += 1
    return r

@pmemoize.MemoizedFunction
def L(m, n, k):
    """
    Signature map of numbers <= m and >= 2 whose integer factorization has
    exactly n distinct primes.  All primes have to be > ps[k].
    """
    r = {}

    if m < ps[k]:
        pass
    
    elif n == 1:
        e = 1
        while 1:
            #thr = int(m**(1./e))
            thr = root(m, e)
            if k == 0:
                recurs = PI(thr)
            else:
                recurs = PI(thr) - PI(ps[k])
            if recurs > 0:
                r[(e,)] = recurs
            else:
                break
            e += 1
    
    elif n > 1:
        thr = int(m**(1./n))
        ki = k+1
        while ki <= PI(thr):
            e = 1
            while ps[ki]**e <= m: # Fix the limit here, if needed for performance
                a = ps[ki]**e
                recurs = L(m/a, n-1, ki)
                for sig, freq in recurs.iteritems():
                    assert freq > 0
                    newsig = tuple(sorted(list(sig) + [e]))
                    if newsig in r:
                        r[newsig] += freq
                    else:
                        r[newsig] = freq
                if a > m: # This limit can be improved a lot
                    break
                e += 1
            ki += 1
    
    return r

@pmemoize.MemoizedFunction
def Lex(m, n):
    r = {}
    for mi in xrange(2, m+1):
        sigi = tuple(sig(mi))
        if len(sigi) == n:
            if sigi in r:
                r[sigi] += 1
            else:
                r[sigi] = 1
    return r

@pmemoize.MemoizedFunction
def G2(m, n):
    return J(m, n, 2)

@pmemoize.MemoizedFunction
def sig2tuples(sig):
    sig = sorted(sig, reverse=True)
    m = lib.prod(a**b for a,b in zip(ps[1:], sig))
    for n in xrange(1, sum(sig)+1):
        print m,n, J(m, n, 2)

def join_sigmaps(sigmaps):
    r = {}
    for sigmap in sigmaps:
        for sig, freq in sigmap.iteritems():
            if sig in r:
                r[sig] += freq
            else:
                r[sig] = freq
    return r

# print F(10**e, 10**e) % MOD

# print L(10**6, 3, 0)

@pmemoize.MemoizedFunction
def compsum(m, n):
    return lib.bincoeff(m-1, n-1)

@pmemoize.MemoizedFunction
def sig2howmany(sig, n):
    """
    How many n-tuples exist that have the given sig and have the same product?
    """
    lensig = len(sig)
    sumsig = sum(sig)

    if lensig >= 1:
        sh = sig[0]
        st = sig[1:]

    if sumsig < n:
        r = 0

    elif lensig == 1 and n == 0:
        r = 0

    elif lensig == 1 and n >= 1:
        r = compsum(sh, n)

    elif lensig > 1:
        r = 0
        for gaps in xrange(0, min([sh,n])+1):
            for complength in xrange(max([1, gaps]), min([sh,n])+1):
                toadd = sig2howmany(st, n-gaps) * lib.bincoeff(n, n-gaps) * compsum(sh, complength) * lib.bincoeff(n-gaps, complength-gaps)
                # tup = (sig2howmany(st, n-gaps) , lib.bincoeff(n, n-gaps) , compsum(sh, complength) , lib.bincoeff(n-gaps, complength-gaps))
                # print 'gaps, complength, tup, toadd', gaps, complength, tup, toadd
                r += toadd
    
    return r


@pmemoize.MemoizedFunction
def do(m):
    # The maximum number of distinct primes is
    maxn = int(math.log(m, 2))
    sigmaps = []
    for n in xrange(1, maxn+1):
        sigmap = L(m, n, 0)
        sigmaps.append(sigmap)
    sigmap = join_sigmaps(sigmaps)

    s = 0
    for sig, freq in sigmap.iteritems():
        for n in xrange(1, sum(sig)+1):
            s += sig2howmany(sig, n) * freq * lib.bincoeff(m, n)

    return s % MOD

# print sig2howmany((1,), 0)
# print sig2howmany((1,1), 1)

# print sig2howmany(
#         (2,3,1,1,1),
#         3
# )
# print J(2**2*3**3*5*7*11, 3, 2) - J(2**2*3**3*5*7*11-1, 3, 2)

for e in xrange(1, 8):
    print e, do(10**e)

# for i in xrange(2, 10**3):
#     s = tuple(sorted(sig(i)))
#     for n in xrange(1, sum(s)+1):
#         quick = sig2howmany(s, n)
#         exact = J(i, n, 2) - J(i-1, n, 2)
#         if quick != exact:
#             print i, quick, exact

# for i in xrange(2, 10**3):
#     s = tuple(sorted(sig(i)))
#     for n in xrange(1, sum(s)+1):
#         quick = L(i, n, 0)
#         exact = Lex(i, n)
#         if quick != exact:
#             for k in quick:
#                 qv = quick[k]
#                 ev = exact[k]
#                 if qv != ev:
#                     print i, k, qv, ev
