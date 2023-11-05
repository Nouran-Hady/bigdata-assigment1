import pandas as pd
import subprocess

# Load the credit card dataset
data = pd.read_csv('CCGENERAL.csv')

# Insight 1: Calculate basic statistics for 'BALANCE' variable
balance_stats = data['BALANCE'].describe()
insight1 = f"Insight 1: Basic Statistics for 'BALANCE' Variable:\n{balance_stats}\n"

# Insight 2: Determine the average purchase amount
average_purchase_amount = data['PURCHASES'].mean()
insight2 = f"Insight 2: Average Purchase Amount: ${average_purchase_amount:.2f}\n"

# Insight 3: High Credit Limit Customers
# Identify customers with high credit limits
high_credit_limit_customers = data[data['CREDIT_LIMIT'] > 5000]  # Adjust the threshold as needed
insight3 = "Insight 3: High Credit Limit Customers:\n"
insight3 += high_credit_limit_customers[['CUST_ID', 'CREDIT_LIMIT']].to_string(index=False)

# Save insights to text files
with open('eda-insight-1.txt', 'w') as f:
    f.write(insight1)

with open('eda-insight-2.txt', 'w') as f:
    f.write(insight2)

with open('eda-insight-3.txt', 'w') as f:
    f.write(insight3)
