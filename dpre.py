import pandas as pd
import numpy as np
import subprocess

#Task1 Data Cleaning
df.drop('CUST_ID', axis = 1, inplace = True )

#Task2 Data Cleaning
df.isnull().sum()

#Task3 Data Cleaning
df['MINIMUM_PAYMENTS'].fillna(df['MINIMUM_PAYMENTS'].median(), inplace=True)
df['CREDIT_LIMIT'].fillna(df['CREDIT_LIMIT'].median(), inplace= True)

from sklearn.preprocessing import MinMaxScaler

#Task 1 Data Transormation 
# Encode categorical variables using one-hot encoding
df['old_PAYMENTS'] = df['PAYMENTS']
# Scale numerical variables using MinMaxScaler
scaler = MinMaxScaler()
df[['PAYMENTS', 'MINIMUM_PAYMENTS','PRC_FULL_PAYMENT']] = scaler.fit_transform(df[['PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT']])

#Task2 Data Transfomation 
df['Installment_Purchases'] = df['INSTALLMENTS_PURCHASES'] + df["PURCHASES_INSTALLMENTS_FREQUENCY"] +1
df['Cash'] = df['CASH_ADVANCE'] + df['CASH_ADVANCE_FREQUENCY'] + 1
df['Purchases'] = df['PURCHASES'] + df['PURCHASES_FREQUENCY'] + 1
df['Balance'] = df['BALANCE'] + df['BALANCE_FREQUENCY']
df.head()

from sklearn.feature_selection import SelectKBest, chi2

#Task1 Data reduction 
# Use SelectKBest to select the top 4 features
X = df.drop('TENURE', axis=1)
y = df['TENURE']
selector = SelectKBest(chi2, k=6)
X_new = selector.fit_transform(X, y)

#task 2 Data Reduction 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA()  
reduced_data = pca.fit_transform(scaled_data)

explained_variance_ratio = pca.explained_variance_ratio_
explained_variance_ratio

# Task 1: Data Discretization
df['binned_BALANCE'] = pd.cut(df['BALANCE'], bins=3, labels=['low_balance', 'medium_balance', 'high_balance'])


df['binned_CREDIT_LIMIT'] = pd.cut(df['CREDIT_LIMIT'], bins=3, labels=['low_CREDIT_LIMIT', 'medium_CREDIT_LIMIT', 'high_CREDIT_LIMIT'])

# Task 2: Data Discretization
feature_to_discretize = df['PRC_FULL_PAYMENT']
num_bins = 5
df['binned_PRCFULLPAYMENT'] = pd.qcut(feature_to_discretize, q=num_bins, labels=False, duplicates='drop')

df.to_csv('res_dpre.csv', sep='\t', header=False, index=True)

# Invoke the next Python script and pass the data frame path as an argument
subprocess.run(["python3", "eda.py", df], check=True)