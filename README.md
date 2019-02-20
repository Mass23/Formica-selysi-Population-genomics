# Formica Selysi - Signs of selection on the supergene

## Methods

### 1. Reads processing
Script: [reads_preprocessing.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/reads_preprocessing.py)

References:
- Trimmomatic (v0.36): https://academic.oup.com/bioinformatics/article/30/15/2114/2390096
- BWA mem (v0.7.17): https://arxiv.org/abs/1303.3997
- Picard MarkDuplicates (v2.18.11): http://broadinstitute.github.io/picard

### 2. Variants calling
Merge bam files: samtools merge (https://academic.oup.com/bioinformatics/article/25/16/2078/204688)

Script: [variants_calling.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/variants_calling.py)
- Allows the multiprocessing of freebayes using the multiprocessing python module, parallelisation per scaffold/contig.
- No filtering in freebayes leading to large memory usage (approx. 16g per core needed). To reduce memory usage, reducing the number of alleles considered per site and filtering on depth/quality/mapping quality can be added.

Reference:
- Freebayes (v1.2.0):  https://arxiv.org/abs/1207.3907
- Multiprocessing in python (v3.7): https://docs.python.org/3.7/library/multiprocessing.html

### 3. Fst / Tajima's D / Ka/Ks

### 4. McDonald-Kreitman tests
