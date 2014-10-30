

import numpy as np
cimport numpy as cnp
DTYPE = np.int               # fix a datatype for the arrays
ctypedef cnp.int_t DTYPE_t   # assign a corresponding compile-time C type to DTYPE_t



def score_nocdef(a,b):
    if a==b: return 2 # match
    else: return -1 # mismatch

def cython_test_nocdef(seq1="ACACACTA", seq2="AGCACACA"):
    gap = -1
    m = len(seq1); n=len(seq2)
    H = np.zeros((m+1, n+1))
    for i in range(1,m+1):
        for j in range(1,n+1):
            H[i,j] = max([H[i-1,j-1]+score_nocdef(seq1[i-1],seq2[j-1]), H[i,j-1]+gap, H[i-1,j]+gap])
    return H[m,n]



cdef int score(str a,str b):
    if a==b: return 2 # match
    else: return -1 # mismatch

cpdef int cython_test(str seq1="ACACACTA",str seq2="AGCACACA"):
    cdef int m,n,i,j,gap
    cdef cnp.ndarray[DTYPE_t, ndim=2] H
    gap = -1
    m = len(seq1); n=len(seq2)
    H = np.zeros((m+1, n+1), dtype=np.int)
    for i in range(1,m+1):
        for j in range(1,n+1):
            H[i,j] = max([H[i-1,j-1]+score(seq1[i-1],seq2[j-1]), H[i,j-1]+gap, H[i-1,j]+gap])
    return H[m,n]

