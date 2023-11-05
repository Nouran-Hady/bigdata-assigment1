import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Load the credit card dataset
data = pd.read_csv('CCGENERAL.csv')

# Create a histogram to visualize the distribution of the 'BALANCE' variable
plt.figure(figsize=(10, 6))
plt.hist(data['BALANCE'], bins=20, color='blue', alpha=0.7)

# Customize the chart labels and title
plt.xlabel('Balance Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Account Balances')

# Save the visualization as vis.png
plt.savefig('vis.png')

# Show the chart (optional)
plt.show()
