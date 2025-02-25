import pandas as pd

# Path RES file
file_path = 'output.res'

# Read the RES file
try:
    df = pd.read_csv(file_path, sep= ',', header=0,comment='#', on_bad_lines='warn')
    print('File read successfully')
    print(df.head())
except Exception as e:
    print('Error reading file:', e)