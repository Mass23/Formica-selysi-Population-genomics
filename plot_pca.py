import pandas as pd
import matplotlib.pyplot as plt

data_vec = pd.read_csv('plink.eigenvec', sep = ' ', header = None)
data_eig = pd.read_csv('plink.eigenval', header = None)

data_vec = data_vec.drop(0, axis = 1)
data_vec['Pop'] = ''
print(data_vec)

for index, row in enumerate(data_vec.itertuples()):
    if str(row[1]).startswith('FEM'):
        data_vec.loc[index,'Pop'] = 'grey'

    elif str(row[1]).startswith('FEP'):
        data_vec.loc[index,'Pop'] = 'darkgrey'

    elif str(row[1]).startswith('FcB'):
        data_vec.loc[index,'Pop'] = 'limegreen'

    elif str(row[1]).startswith('FcQ'):
        data_vec.loc[index,'Pop'] = 'darkgreen'

    # M
    elif str(row[1]) in ['701W1','677W1','674W1','700W3','De115W1','De125W1','De172W1','De397W1','De434W1','De44W1','De67W1','De84W1']:
        data_vec.loc[index,'Pop'] = 'blue'

    # P
    elif str(row[1]) in ['De446W2','De299W1','De267W1','De259W2','710W2','716W1','722W1','733W1','748W1','715W2','508W1','706W4','703W4','750W2','713W3']:
        data_vec.loc[index,'Pop'] = 'red'

    else:
        data_vec.loc[index,'Pop'] = 'orange'

import seaborn as sns
fig = plt.figure(figsize = (12,6))

plt.subplot(121)
sns.barplot(y=data_eig[0], x = [i for i in range(1,21)], color = 'darkgrey')
plt.ylabel('Eigenvalues')

plt.subplot(122)

plt.scatter(data_vec[2], data_vec[3], c = data_vec['Pop'])
plt.xlabel('PC1(' + str(data_eig[0][0]) + '%)')
plt.ylabel('PC2(' + str(data_eig[0][1]) + '%)')

plt.tight_layout()
plt.savefig('PCA.pdf', format='pdf', dpi=3000)

plt.show()
plt.close()
