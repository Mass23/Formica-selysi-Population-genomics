# Formica Selysi - Signs of selection on the supergene

## 1 - Preprocessing

### 1.1 - Reads processing
Script: [reads_preprocessing.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/reads_preprocessing.py)

References:
- Trimmomatic (v0.36): https://academic.oup.com/bioinformatics/article/30/15/2114/2390096
- BWA mem (v0.7.17): https://arxiv.org/abs/1303.3997
- Picard MarkDuplicates (v2.18.11): http://broadinstitute.github.io/picard

### 1.2 - Variants calling
Merge bam files: samtools merge (https://academic.oup.com/bioinformatics/article/25/16/2078/204688, v1.8)

Script: [variants_calling.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/variants_calling.py)
- Allows the multiprocessing of freebayes using the multiprocessing python module, parallelisation per scaffold/contig.
- No filtering in freebayes leading to large memory usage (approx. 16g per core needed). To reduce memory usage, reducing the number of alleles considered per site and filtering on depth/quality/mapping quality can be added.

- Picard CreateSequenceDictionary:
```java -jar picard.jar CreateSequenceDictionary R=reference.fasta O=reference.dict```

- Picard SortVcf:
```java -jar picard.jar SortVcf I=raw_variants.vcf SEQUENCE_DICTIONARY=reference.dict O=sorted_variants.vcf```

References:
- Freebayes (v1.2.0):  https://arxiv.org/abs/1207.3907
- Multiprocessing in python (v3.7): https://docs.python.org/3.7/library/multiprocessing.html

### 1.3 - Variants filtering
1 - Keep only SNPs

2 - Depth and quality:
- QD < 5.0

3 - Filtering on mapping quality (Not too stringent as Sp haplotype of the supergene largely differs from the Sm one):
- MQ < 20

4 - Filtering on strand bias:
- FS > 60.0
- MQRankSum < -12.5
- ReadPosRankSum < -8.0

Reference:
- BCFtools filter (Samtools v1.8): https://academic.oup.com/bioinformatics/article/25/16/2078/204688

### 1.4 - Social-form PCA
Plink command (v1.9): 
```plink --vcf file.vcf --pca```

Plot: [plot_pca.py](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/plot_pca.py)
- To change colors according to results

Reference:
- http://pngu.mgh.harvard.edu/purcell/plink/

## 2 - Analysis

### 2.1 - Region-based analysis

### 2.1.1 - Fst and Tajima's D analysis

Genome-wide scans (20kbp):
- Tajima's D as a measure of balancing selection
```vcftools --vcf VCF_FILE.vcf --TajimaD 20000 --out Sm_Sp_20kbp```

- Fst as a measure of divergence between Sm and Sp
```vcftools --vcf VCF_FILE.vcf --weir-fst-pop Sm.txt --weir-fst-pop Sp.txt --fst-window-size 20000 --out Sm_Sp_20kbp```

- Fst as a measure of conservation within Sm
```vcftools --vcf VCF_FILE.vcf --weir-fst-pop Sm.txt --fst-window-size 20000 --out Sm_20kbp```

- Fst as a measure of conservation within sp
```vcftools --vcf VCF_FILE.vcf --weir-fst-pop Sp.txt --fst-window-size 20000 --out Sp_20kbp```

**Output:**

- Manhattan plot of the Scaffold03 with Scaffold01 as comparison 
      - A: Tajima's D
      - B: Fst 
            - (1) Sm and Sp divergence 
            - (2) Conservation within Sm 
            - (3) Conservation within Sp
      
- Stats file with summary statistice for the following regions:
      - Inversion A
      - Inversion B
      - Inversion C
      - Inversion D
      - Centromere
      - Inversion breakpoints
      - Pseudo-autosomal regions
      - Rest of the genome
      
Script: [manhattan_plot.py]()

### 2.1.2 - Site-frequency spectrum

### 2.2 - Gene-based analysis

### 2.2.1 - McDonald-Kreitman tests
Script to get Tsil and Trep: python?
Script to SnIPRE: [pop_genome.R](https://github.com/Mass23/FormicaSelysiBalSel/blob/master/pop_genome.R)

References:
- https://academic.oup.com/mbe/article/31/7/1929/2925788
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002806

### 2.2.2 Hyphy on genes under positive selection?
