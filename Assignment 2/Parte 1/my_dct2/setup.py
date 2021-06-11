from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy
import os
os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"
setup( name = 'mydct', # module name to call in python code
ext_modules=[Extension("mydct", # specifies all the files needed
 sources=["dct.pyx","cdct.cpp"],
 language="c++", # tells cython to use C++ instead of C
 include_dirs=[numpy.get_include(),"."])],
cmdclass = {'build_ext': build_ext},
)