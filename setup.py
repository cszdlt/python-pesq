from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext as _build_ext
import os

includes = ['pypesq']
try:
    import numpy as np
    includes += [os.path.join(np.get_include(), 'numpy')]
except:
    pass

extension = Extension("pesq_core",
                      sources=["pypesq/pesq.c", "pypesq/dsp.c", "pypesq/pesqdsp.c",
                               "pypesq/pesqio.c", "pypesq/pesqmain.c", "pypesq/pesqmod.c"],
                      include_dirs=includes,
                      language='c')


class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        try:
            __builtins__.__NUMPY_SETUP__ = False
        except AttributeError:
            print("Cannot set '__builtins__.__NUMPY_SETUP__ = False' This is not needed if numpy is already installed.")

        import numpy
        self.include_dirs.append(numpy.get_include())


setup(name='pypesq',
    packages=find_packages(),
    ext_modules=[extension],
    cmdclass={'build_ext': build_ext},
)
