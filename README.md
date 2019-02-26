# Formica Selysi - Signs of selection on the supergene

## Methods

### 1. Reads processing
Script: [reads_preprocessing.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/reads_preprocessing.py)

References:
- Trimmomatic (v0.36): https://academic.oup.com/bioinformatics/article/30/15/2114/2390096
- BWA mem (v0.7.17): https://arxiv.org/abs/1303.3997
- Picard MarkDuplicates (v2.18.11): http://broadinstitute.github.io/picard

### 2. Variants calling
Merge bam files: samtools merge (https://academic.oup.com/bioinformatics/article/25/16/2078/204688, v1.8)

Script: [variants_calling.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/variants_calling.py)
- Allows the multiprocessing of freebayes using the multiprocessing python module, parallelisation per scaffold/contig.
- No filtering in freebayes leading to large memory usage (approx. 16g per core needed). To reduce memory usage, reducing the number of alleles considered per site and filtering on depth/quality/mapping quality can be added.

- Picard CreateSequenceDictionary:
java -jar picard.jar CreateSequenceDictionary \ 
      R=reference.fasta \ 
      O=reference.dict

- Picard SortVcf:
java -jar picard.jar SortVcf \
      I=raw_variants.vcf \
      SEQUENCE_DICTIONARY=reference.dict \
      O=sorted_variants.vcf

References:
- Freebayes (v1.2.0):  https://arxiv.org/abs/1207.3907
- Multiprocessing in python (v3.7): https://docs.python.org/3.7/library/multiprocessing.html

### 3. Variants filtering
1 - Keep only SNPs

2 - Depth and quality:
- 5 < DP
- 30 < Qual

3 - Filtering on mapping quality (Not too stringent as Sp haplotype of the supergene largely differs from the Sm one):
- MQ < 30 or 20?

4 - Filtering on strand bias:
- FS > 60.0
- MQRankSum < -12.5
- ReadPosRankSum < -8.0

Reference:
- BCFtools filter (Samtools v1.8): https://academic.oup.com/bioinformatics/article/25/16/2078/204688

### 4. Social-form PCA
Plink command (v1.9): plink --vcf file.vcf --pca

Plot: [plot_pca.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/plot_pca.py)
- To change colors according to results

Reference:
- http://pngu.mgh.harvard.edu/purcell/plink/

### ?. McDonald-Kreitman tests
Script to get Tsil and Trep: python?
Script to SnIPRE: [pop_genome.R](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/pop_genome.R)

References:
- https://academic.oup.com/mbe/article/31/7/1929/2925788
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002806
