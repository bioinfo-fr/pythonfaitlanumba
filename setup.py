"""Transform into a .pyx Cython file"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

import numpy as np

prefix = "taille_cython"


extensions = [
    Extension(prefix, [prefix+".pyx"],
              include_dirs=[np.get_include()],
              )
]
setup(
    name=prefix,
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(extensions),
)
