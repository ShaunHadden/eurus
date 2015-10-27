'''Eurus
'''

import os
from distutils.core import setup
from setuptools import find_packages
import numpy as np

CLASSIFIERS = [
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Intended Audience :: Science/Research',
'License :: OSI Approved :: MIT License',
'Programming Language :: Python',
'Topic :: Scientific/Engineering',
'Topic :: Scientific/Engineering :: Mathematics',
'Topic :: Scientific/Engineering :: Physics',
'Operating System :: Microsoft :: Windows',
'Operating System :: POSIX',
'Operating System :: Unix',
'Operating System :: MacOS',
'Natural Language :: English',
]

with open('README.md') as fp:
    LONG_DESCRIPTION = ''.join(fp.readlines())

setup(
    name = 'eurus',
    # version = '0.1.1',
    packages = find_packages(),
    install_requires = ['numpy>=1.7',
                        'scipy>=0.13',
                       ],
    author = 'Shaun Hadden',
    author_email = 'shadden2@uwo.ca',
    description = 'Eurus',
    long_description = LONG_DESCRIPTION,
    license = 'MIT',
    keywords = 'full-waveform inversion',
    # url = '',
    download_url = 'http://github.com/ShaunHadden/eurus',
    classifiers = CLASSIFIERS,
    platforms = ['Windows', 'Linux', 'Solaris', 'Mac OS-X', 'Unix'],
    use_2to3 = False,
    include_dirs=[np.get_include()],
)
