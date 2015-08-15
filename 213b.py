import scipy as s
import scipy.ndimage as sn

M = 5

kernel = s.ones((3, 3))
kernel[0,0] = 0
kernel[0,2] = 0
kernel[1,1] = 0
kernel[0,2] = 0
kernel[2,0] = 0
kernel[2,2] = 0
kernel /= 4.

A = s.zeros((M, M))
A[0,0] = 1
Ainside = A[1:-1,1:-1]

print kernel
print A

Ainside = sn.convolve(Ainside, kernel, mode = 'nearest')

print A
