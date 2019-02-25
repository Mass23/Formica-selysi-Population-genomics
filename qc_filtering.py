import allel
import pandas as pd
import matplotlib.pyplot as plt
import argparse

# python3 QC_filtering.py -r RAW_FILE -f FILTERED_FILE
parser = argparse.ArgumentParser()

parser.add_argument('-r', '--RawVCF', help='Raw VCF file', type=str, action = 'store', required = True)
parser.add_argument('-f', '--FilteredVCF', help='Filtered VCF file', type=int, action = 'store', required = True)

args = parser.parse_args()

raw_vcf = args.RawVCF
filtered_vcf = args.FilteredVCF

print("Parsing raw file...")
callset_raw = allel.read_vcf(raw_vcf, fields='*')

print(callset_raw)

print("Parsing filtered file...")
callset_f = allel.read_vcf(filtered_vcf, fields='*')

print(callset_f)

#######################################
print("QD...")

QD_raw = callset_raw['variants/QD']
QD_f = callset_f['variants/QD']

data1 = pd.DataFrame({'QD_raw': list(QD_raw)})
data2 = pd.DataFrame({'QD_f': list(QD_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting QD...")
data.plot.kde(title = 'variants/QD')
plt.show()

#######################################
print("MQ...")

MQ_raw = callset_raw['variants/MQ']
MQ_f = callset_f['variants/MQ']

data1 = pd.DataFrame({'MQ_raw': list(MQ_raw)})
data2 = pd.DataFrame({'MQ_f': list(MQ_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting MQ...")
data.plot.kde(title = 'MQ')
plt.show()

#######################################
print("FS...")

FS_raw = callset_raw['variants/FS']
FS_f = callset_f['variants/FS']

data1 = pd.DataFrame({'FS_raw': list(FS_raw)})
data2 = pd.DataFrame({'FS_f': list(FS_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting FS...")
data.plot.kde(title = 'FS')
plt.show()

#######################################
print("SOR...")

SOR_raw = callset_raw['variants/SOR']
SOR_f = callset_f['variants/SOR']

data1 = pd.DataFrame({'SOR_raw': list(SOR_raw)})
data2 = pd.DataFrame({'SOR_f': list(SOR_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting SOR...")
data.plot.kde(title = 'SOR')
plt.show()

#######################################
print("MQRankSum...")

MQRankSum_raw = callset_raw['variants/MQRankSum']
MQRankSum_f = callset_f['variants/MQRankSum']

data1 = pd.DataFrame({'MQRankSum_raw': list(MQRankSum_raw)})
data2 = pd.DataFrame({'MQRankSum_f': list(MQRankSum_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting MQRankSum...")
data.plot.kde(title = 'MQRankSum')
plt.show()

#######################################
print("ReadPosRankSum...")

ReadPosRankSum_raw = callset_raw['variants/ReadPosRankSum']
ReadPosRankSum_f = callset_f['variants/ReadPosRankSum']

data1 = pd.DataFrame({'ReadPosRankSum_raw': list(ReadPosRankSum_raw)})
data2 = pd.DataFrame({'ReadPosRankSum_f': list(ReadPosRankSum_f)})

data = pd.concat([data1,data2], ignore_index=True, axis=1)

print("Plotting ReadPosRankSum...")
data.plot.kde(title = 'ReadPosRankSum')
plt.show()
