# qiime-default-reference changelog

## Version 0.1.1-dev (changes since 0.1.1 release go here)

### Bug fixes
* Updated the reference alignment to be the PyNAST-aligned 13_5 alignment rather than the SSU-aligned 13_8 alignment. There were no changes in the alignment between Greengenes 13_5 and 13_8, but the SSU alignment filters some positions such that if you remove the gaps from the SSU alignment, the sequences are shorter than in the unaligned representative sequences. This causes problems for searching sequences against the unaligned sequences, as is done by PyNAST. 
