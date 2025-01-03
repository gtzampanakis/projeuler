print()

def digits(n):
    d = n//10
    m = n%10
    return (digits(d) if d else []) + [m]

def digit_join(ds):
    if not ds:
        return 0
    else:
        return ds[-1] + digit_join(ds[:-1]) * 10

def e(ds, s):
    if s == 0 and not ds:
        return True
    else:
        i = 1
        while 1:
            h = ds[:i]
            t = ds[i:]
            l = digit_join(h)
            if not t:
                return l == s
            else:
                if e(t, s-l):
                    return True
            i += 1

a = 0
for s in [1, 9]:
    for n in range(s, 10**6+1, 9):
        nn = n*n
        ds = digits(nn)
        if len(ds) > 1 and e(ds, n):
            print(n, nn)
            a += nn

print(a)
