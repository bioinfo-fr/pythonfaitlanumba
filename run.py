# coding: utf-8

import random
import timeit
import matplotlib.pyplot as plt
from numba import autojit
from taille_cython import cython_test, cython_test_nocdef


####################
## TEST FUNCTIONS ##
####################

### TRIPLE FOR

def triplefor(taille):
    count = 0
    for i in xrange(taille):
        for j in xrange(taille):
            for k in xrange(taille):
                count += i * j + k
    return count / taille


tripleforN = autojit(triplefor)


#######################
## TIMINGS FUNCTIONS ##
#######################


def timings(nb_tries, start=1, stop=200, step=10):

    values = range(start, stop, step)

    setup = {
        'triplefor': ('triplefor(%s)', 'from __main__ import triplefor'),
        'tripleforN': ('tripleforN(%s)', 'from __main__ import tripleforN'),
        'tripleforC': ('cython_test(%s)', 'from __main__ import cython_test'),
        'tripleforCnocdef': ('cython_test_nocdef(%s)', 'from __main__ import cython_test_nocdef'),
    }

    def do(setup):
        result = {}
        for k, v in setup.iteritems():
            print k, v
            result[k] = [timeit.timeit(v[0] % x, number=nb_tries, setup=v[1]) for x in values]
        return result

    return do(setup), values




####################
## PLOT FUNCTIONS ##
####################


def plot(timings, title, ranked_labels, labels, orders_n):
    plt.rcParams.update({'font.size': 12})
    plt.figure(figsize=(11, 10))
    for lb in ranked_labels:
        plt.plot(orders_n, timings[lb], alpha=0.5, label=labels[lb], marker='o', lw=3)
    plt.xlabel('sample size n (items in the list)')
    plt.ylabel('time per computation')
    plt.xlim([min(orders_n) / 10, max(orders_n) * 10])
    plt.legend(loc=2)
    plt.grid()
    plt.xscale('log')
    plt.yscale('log')
    plt.title(title)
    plt.savefig('myfilename.png')

##########
## MAIN ##
##########

if __name__ == '__main__':
    N = 5  # nombre d'essais
    t, values = timings(5, start=10, stop=2000, step=10)

    labels = {
        'triplefor': 'For loop',
        'tripleforN': 'For loop (numba)',
        'tripleforC': 'For loop (cython)',
        'tripleforCnocdef': 'For loop (cython_nocdef)',
    }

    plot(t, 'Title', [
        #'triplefor',
        'tripleforN', 'tripleforC',
        #'tripleforCnocdef'
        ], labels, values)
