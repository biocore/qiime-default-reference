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

Usage
^^^^^

``qiime-default-reference`` makes it very easy to access the Greengenes 97% OTUs and some other key pieces of Greengenes from within Python. After installing, you can do the following:

.. code-block:: python

    import qiime_default_reference

    # Get the absolute filepath to the reference sequences in fasta format.
    qiime_default_reference.get_reference_sequences()

    # Get the absolute filepath to the PyNAST template alignment in fasta format.
    qiime_default_reference.get_template_alignment()

    # Get the absolute filepath to the reference phylogenetic tree in newick format.
    qiime_default_reference.get_reference_tree()

    # Get the absolute filepath to the reference taxonomy in tab-separated text format.
    qiime_default_reference.get_reference_taxonomy()

    # Get the alignment column mask (currently the Lane mask) as 1s and 0s.
    # This will be str/bytes in Python 2 (they're the same), and bytes in Python 3.
    qiime_default_reference.get_template_alignment_column_mask()

Getting Help
^^^^^^^^^^^^
Please post your questions about this repository/package on the `QIIME Forum <http://forum.qiime.org>`_.

.. |Build Status| image:: https://travis-ci.org/biocore/qiime-default-reference.svg?branch=master
   :target: https://travis-ci.org/biocore/qiime-default-reference
.. |Coverage Status| image:: https://coveralls.io/repos/biocore/qiime-default-reference/badge.png
   :target: https://coveralls.io/r/biocore/qiime-default-reference
