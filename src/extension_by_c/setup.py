from setuptools import setup, Extension
import numpy as np

module = Extension('avx2_power',
                   sources=['avx2_power.c'],
                   include_dirs=[np.get_include()],
                   extra_compile_args=['-mavx2', '-O3'],
                   extra_link_args=[])

setup(name='avx2_power',
      version='1.0',
      description='AVX2 accelerated power function',
      ext_modules=[module])