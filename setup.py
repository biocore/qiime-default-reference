#!/usr/bin/env python

# Copied and modified from
# https://github.com/biocore/scikit-bio/blob/master/setup.py
# See licenses/scikit-bio.txt for more details.

import sys
import gzip
import os.path
from setuptools import find_packages, setup

# don't preprocess (e.g., decompress) any data if the following modes are
# invoked
preprocess_data = all([e not in sys.argv
                       for e in ('egg_info', 'sdist', 'register')])

__version__ = "0.1.3"

classes = """
    Development Status :: 3 - Alpha
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = 'Default reference data files for use with QIIME.'

with open('README.rst') as f:
    long_description = f.read()


def gunzip(fp):
    out_fp = os.path.splitext(fp)[0]
    sys.stdout.write("    Decompressing %s to %s..." % (fp, out_fp))
    with gzip.open(fp, 'rb') as gzipped_fh:
        with open(out_fp, 'wb') as out_fh:
            for line in gzipped_fh:
                out_fh.write(line)
    sys.stdout.write("done\n")


gg_module_prefix = 'qiime_default_reference.gg_13_8_otus'
gg_path_prefix = gg_module_prefix.replace('.', os.path.sep)

if preprocess_data:
    sys.stdout.write("Decompressing reference data files:\n")
    gunzip(os.path.join(gg_path_prefix, 'rep_set', '97_otus.fasta.gz'))
    gunzip(os.path.join(gg_path_prefix, 'taxonomy', '97_otu_taxonomy.txt.gz'))
    gunzip(os.path.join(gg_path_prefix, 'trees', '97_otus.tree.gz'))
    gunzip(os.path.join(gg_path_prefix, 'rep_set_aligned', '85_otus.pynast.fasta.gz'))

setup(
    name='qiime-default-reference',
    version=__version__,
    license='CC BY-SA 3.0',
    description=description,
    long_description=long_description,
    author="QIIME development team",
    author_email="qiime.help@gmail.com",
    maintainer="QIIME development team",
    maintainer_email="qiime.help@gmail.com",
    url='http://www.qiime.org',
    test_suite='nose.collector',
    packages=find_packages(),
    install_requires=['six'],
    extras_require={'test': ['nose']},
    classifiers=classifiers,
    package_data={
        gg_module_prefix : ['rep_set/*.fasta', 'taxonomy/*.txt', 'trees/*.tree',
                            'rep_set_aligned/*.fasta']
    }
)
