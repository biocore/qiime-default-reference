# qiime-default-reference changelog

## Version 0.1.3-dev (changes since 0.1.3 release go here)

## Version 0.1.3

### Features
* ``qiime-default-reference`` is now Python 2/3 compatible.

## Version 0.1.2

### Bug fixes
* [Issue #14](https://github.com/biocore/qiime-default-reference/issues/14) was fixed. The reference alignment was updated to be the PyNAST-aligned 13_5 alignment rather than the SSU-aligned 13_8 alignment. There were no changes in the sequences between Greengenes 13_5 and 13_8, but the SSU alignment is positionally filtered, such that if you remove the gaps from the SSU alignment, the sequences are missing many positions relative to the unaligned representative sequences. This causes problems for searching sequences against the unaligned sequences, as is done by PyNAST.

 The new file was generated by downloading the Greengenes 13_5 PyNAST alignment from Second Genome. This was then filtered to contain only the sequences in the Greengenes 13_8 85% OTUs with the following QIIME 1.9.0 command:

    ```
    filter_fasta.py -f gg_13_5_pynast.fasta -o 85_otus.pynast.fasta -a 85_otus.fasta
    ```
 The md5 sums of those files are:
  * ``gg_13_5_pynast.fasta.gz`` : ``24720085027c35132de0588fee518065``
  * ``85_otus.pynast.fasta`` : ``1de2e593b38041c5b3012220325b76fa``
  * ``85_otus.fasta`` : ``6c571af57ab0f72af9288b72f6c50206``

 We announced this bug to our users on the QIIME blog [here](https://qiime.wordpress.com/2015/04/15/qiime-1-9-0-bug-affecting-pynast-alignment-of-16s-amplicons-generated-with-non-515f806r-primers/).

## Version 0.1.1

### Features
* Added a default reference tree ([#10](https://github.com/biocore/qiime-default-reference/issues/10)).

## Version 0.1.0

Initial alpha release.
