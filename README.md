# Numba vs Cython

Small benchmark to test the efficiency of Numba comparing to well-known Cpython.

This is material for this [bioinfor-fr article](python-fait-la-numba).


# Prerequisites

* Cython ([doc](http://docs.cython.org/src/quickstart/install.html))
* Numba ([doc](http://numba.pydata.org/numba-doc/dev/install.html))
* Matplotlib ([doc](http://matplotlib.org/users/installing.html)).

# Usage

    python setup.py install  # build Cython extension
    python run.py            # run benchmark
