import scipy as s

M = 30
N = 30
B = 50

R1 = s.array(( 0,+1))
R2 = s.array(( 0,-1))
R3 = s.array((+1, 0))
R4 = s.array((-1, 0))

def is_in(point):
    if 0 <= point[0] < M:
        if 0 <= point[1] < N:
            return True
    return False

def ij2k((i,j)):
    return i*M + j

def k2ij(k):
    return (k/M, k%M)

T = s.zeros((M*N, M*N))
P = s.zeros((M*N, M*N))

TEMP1 = s.zeros((M*N, M*N))

for i in xrange(M):
    for j in xrange(N):
# max is 4 neighbors:
        neighs = 0
        ij = s.array((i,j))

        c1 = ij+R1
        c2 = ij+R2
        c3 = ij+R3
        c4 = ij+R4

        if is_in(c1):
            neighs += 1
            T[ij2k(ij), ij2k(c1)] = 1
        if is_in(c2):
            neighs += 1
            T[ij2k(ij), ij2k(c2)] = 1
        if is_in(c3):
            neighs += 1
            T[ij2k(ij), ij2k(c3)] = 1
        if is_in(c4):
            neighs += 1
            T[ij2k(ij), ij2k(c4)] = 1
        
        T[ij2k(ij),:] *= 1./neighs

assert s.all(s.sum(T, 1) == s.ones(M*N))

for k1 in xrange(M*N):
    L = s.zeros(M*N)
    L[k1] = 1
    for b in xrange(B):
        L[:] = s.sum(s.multiply(L[:, s.newaxis], T, out=TEMP1), 0)
    P[k1,:] = L

print P
print
P = 1-P
print P

print 

D = s.product(P, 0)

print D

print s.sum(D)

