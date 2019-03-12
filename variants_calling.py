# python3 genotype_per_chr.py -r reference_genome -b bam_file -n cores_number
from multiprocessing import Pool
import subprocess
import glob
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--ReferenceFasta', help='Reference genome fasta file used for mapping', type=str, action = 'store', required = True)
parser.add_argument('-n', '--NumberCores', help='Number of cores to use', type=int, action = 'store', required = True)
parser.add_argument('-b', '--BamFile', help='Bam file with individuals merged', type=int, action = 'store', required = True)

args = parser.parse_args()

ref_fasta = args.ReferenceFasta
n_cores = args.NumberCores
bam_file = args.BamFile

################################################################################
from Bio import SeqIO
data_inputs = []

with open(ref_fasta, "rU") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        data_inputs.append(record.id)

def process_scaffold(scaffold):
    args_freebayes = ['freebayes', '--region', scaffold, '-f', ref_fasta, bam_file, '>', scaffold + '.vcf']
    subprocess.call(' '.join(args_freebayes), shell = True)
    print(scaffold, 'Done!')

pool = Pool(n_cores)
pool.map(process_scaffold, data_inputs)
pool.close()
pool.join()
