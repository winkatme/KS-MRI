import scipy
from scipy import stats
import scipy.cluster.hierarchy as sch
import seaborn as sns
import numpy as np
import pandas as pd
from tabulate import tabulate
import os

path_to_concatenated_files_folder='Y:\concatenated_files'
file_to_save_to='Y:\KS_concat_all_011223.csv'
heatmap_to_save_to='Y:\sorted_heatmap_011323.png'

# Set working directory
os.chdir(path_to_concatenated_files_folder)

# create matrix of KS values
# matrix code is nested list comprehension calculating ks of all files in listdir to each other
matrix = [[(scipy.stats.ks_2samp(pd.read_csv(os.listdir()[i], header=None)[1], pd.read_csv(os.listdir()[j], header=None)[1], alternative='two-sided', mode='auto'))[0] for i in range(len(os.listdir()))] for j in range(len(os.listdir()))]
matrix=np.round(matrix,4)

# Use list of shortened file names for csv col and row names
file_names_shortened = [i.replace('df_', '').replace('_concat','').replace('.csv','') for i in os.listdir()]
file_names_shortened

# create table
#tabulated_table = tabulate(matrix_test, headers=file_names_shortened, showindex=file_names_shortened)

# To export table as a csv
df= pd.DataFrame(matrix, index=file_names_shortened, columns=file_names_shortened)
#df.to_csv(file_to_save_to)


# cluster heat map

# Source:  https://wil.yegelwel.com/cluster-correlation-matrix/

def cluster_corr(corr_array, inplace=False):
    """
    Rearranges the correlation matrix, corr_array, so that groups of highly 
    correlated variables are next to eachother 
    
    Parameters
    ----------
    corr_array : pandas.DataFrame or numpy.ndarray
        a NxN correlation matrix 
        
    Returns
    -------
    pandas.DataFrame or numpy.ndarray
        a NxN correlation matrix with the columns and rows rearranged
    """
    pairwise_distances = sch.distance.pdist(corr_array)
    linkage = sch.linkage(pairwise_distances, method='complete')
    cluster_distance_threshold = pairwise_distances.max()/2
    idx_to_cluster_array = sch.fcluster(linkage, cluster_distance_threshold, 
                                        criterion='distance')
    idx = np.argsort(idx_to_cluster_array)
    
    if not inplace:
        corr_array = corr_array.copy()
    
    if isinstance(corr_array, pd.DataFrame):
        return corr_array.iloc[idx, :].T.iloc[idx, :]
    return corr_array[idx, :][:, idx]


# create and save heatmap
sns.set(rc={'figure.figsize':(11,10)})
sorted_heatmap=sns.heatmap(cluster_corr(df))
sorted_heatmap
#sorted_heatmap.figure.savefig(heatmap_to_save_to)
