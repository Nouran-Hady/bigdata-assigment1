import pandas as pd
from sklearn.cluster import KMeans
import subprocess

# Load the credit card dataset
data = pd.read_csv('CCGENERAL.csv')

# Select columns for K-means clustering (choose suitable columns)
selected_columns = data[['BALANCE', 'PURCHASES']]

# Initialize and fit the K-means model with k=3
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(selected_columns)

# Count the number of records in each cluster
cluster_counts = data['cluster'].value_counts().sort_index()

# Save the cluster counts to a text file
cluster_counts.to_csv('k.txt', sep='\t', header=False, index=True)

print("K-means clustering results:")
print(cluster_counts)
