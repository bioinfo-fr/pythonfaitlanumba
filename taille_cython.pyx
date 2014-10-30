
def cython_test_nocdef(taille):
    count = 0
    for i in xrange(taille):
        for j in xrange(taille):
            for k in xrange(taille):
                count += i * j + k
    return count / taille


cpdef double cython_test(long taille):
    cdef long count = 0
    cdef long i,j,k
    for i in xrange(taille):
        for j in xrange(taille):
            for k in xrange(taille):
                count += i * j + k
    return <double> count / <double> taille
