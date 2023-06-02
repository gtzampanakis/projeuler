from prime import is_prime, prime
from pmemoize import MemoizedFunction

digits = (1,2,3,4,5,6,7,8,9)

def sumdigits(n):
    return sum(map(int, str(n)))

@MemoizedFunction
def nw(sd, nd, d1s):
    """
    Number of integers with nd digits whose digit sum is equal to sd and start
    with a digit in d1s.
    """
    r = 0
    if sd > 0 and nd > 0:
        if (1 <= sd <= 9) and (sd in d1s):
            r += 1
        for d1 in d1s:
            for ndi in range(nd-1, 0, -1):
                r += nw(sd-d1, ndi, digits)
    return r

def digits_lt(din):
    return tuple([d for d in digits if d < din])

@MemoizedFunction
def ny(sd, m):
    """
    Number of integers less than or equal to m whose digit sum is equal to sd.
    """
    strm = str(m)
    lenstrm = len(strm)
    if sd == 0:
        return 1
    elif lenstrm == 1:
        if 1 <= sd <= m:
            return 1
        else:
            return 0
    else:
        d1 = int(strm[0])
        r = 0
        for ndi, nd in enumerate(range(lenstrm, 0, -1)):
            r += nw(sd, nd, digits_lt(d1) if ndi==0 else digits)
        r += ny(sd-d1, int(strm[1:]))
        return r

def nz(m):
    """
    Number of integers less than m whose digit sum is equal to a prime.
    """
    r = 0
    pri = 0
    limit = 9 * len(str(m))
    while 1:
        pr = prime(pri)
        if pr > limit:
            break
        r += ny(pr, m)
        pri += 1
    return r

def main():
    t = 10**16
    m0 = 1
    while 1:
        if nz(m0*10) > t:
            break
        m0 *= 10
    m = m0
    while 1:
        if m0 < 1:
            break
        while 1:
            c = nz(m+m0)
            if c > t:
                m0 = int(m0/10)
                break
            else:
                m += m0
                if c == t:
                    m0 = 0
                    break
    print(m)

main()
