import sys
import pandas as pd
import subprocess

if len(sys.argv) != 2:
    print("Usage: python load.py /home/doc-bd-a1/CCGENERAL.csv")
    sys.exit(1)

file_path = sys.argv[1]

try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully")
    
except Exception as e:
    print(f"Error: {e}")
