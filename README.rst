qiime-default-reference
-----------------------

|Build Status| |Coverage Status|

qiime-default-reference, canonically pronounced *chime default reference*, is a
Python package containing default reference data files for use with
`QIIME <http://qiime.org/>`_. The current default reference data is compiled
from the Greengenes 16S rRNA database version
`13_8 <ftp://greengenes.microbio.me/greengenes_release/gg_13_5/gg_13_8_otus.tar.gz>`_.
Please see the **Attribution** section below for more details.

Installation
------------
To install qiime-default-reference::

    pip install qiime-default-reference

Running the tests
-----------------
To run qiime-default-reference's unit tests::

    nosetests --with-doctest qiime_default_reference

Attribution
^^^^^^^^^^^
The reference data distributed in this Python package were copied from the
`Greengenes 16S rRNA database <http://greengenes.secondgenome.com/>`_:

**An improved Greengenes taxonomy with explicit ranks for ecological and
evolutionary analyses of bacteria and archaea.**
McDonald D, Price MN, Goodrich J, Nawrocki EP, DeSantis TZ, Probst A,
Andersen GL, Knight R, Hugenholtz P.
ISME J. 2012 Mar;6(3):610-8. doi: 10.1038/ismej.2011.139.

The Greengenes reference data is licensed under a
`Creative Commons Attribution-ShareAlike 3.0 Unported License <http://creativecommons.org/licenses/by-sa/3.0/deed.en_US>`_.

The default template alignment column mask (i.e., "Lane mask") is derived from:

Lane,D.J. (1991) **16S/23S rRNA sequencing.** In Stackebrandt,E. and
Goodfellow,M. (eds), Nucleic Acid Techniques in Bacterial Systematics.
John Wiley and Sons, New York, pp. 115-175.

Lane mask was originally available in `ARB <http://www.ncbi.nlm.nih.gov/pubmed/14985472>`_.

Lane mask taken from `here <http://greengenes.lbl.gov/Download/Sequence_Data/lanemask_in_1s_and_0s>`_.

Getting Help
^^^^^^^^^^^^
Please post your questions about this repository/package on the `QIIME Forum <http://forum.qiime.org>`_.

.. |Build Status| image:: https://travis-ci.org/biocore/qiime-default-reference.svg?branch=master
   :target: https://travis-ci.org/biocore/qiime-default-reference
.. |Coverage Status| image:: https://coveralls.io/repos/biocore/qiime-default-reference/badge.png
   :target: https://coveralls.io/r/biocore/qiime-default-reference
