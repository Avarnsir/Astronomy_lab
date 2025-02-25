import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from glob import glob

#file path
input_dir = '/home/dell/Projects/AstroLab/ngc_6397_spectra/spectra'
output_dir = '/home/dell/Projects/AstroLab/ngc_6397_spectra/plots'

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Get all .txt files in the directory
txt_files = glob(os.path.join(input_dir, '*.txt'))

# Function to plot all columns in a file
def plot_all_columns(file_path, output_dir):
    try:
        # Read the file into a DataFrame
        df = pd.read_csv(file_path, sep='\s+', header=None, comment='#')
        
        # Print the file information
        print(f"File: {os.path.basename(file_path)}")
        print(f"Shape: {df.shape}")
        print(df.head()) 
        
        # Plot all columns
        plt.figure(figsize=(10, 6))
        for col in range(df.shape[1]):
            plt.plot(df[col], label=f'Column {col}')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.title(f'Data for {os.path.basename(file_path)}')
        plt.legend()
        plt.grid(True)
        
        # Save the plot
        output_file = os.path.join(output_dir, f'{os.path.basename(file_path)}_plot.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Plot saved to {output_file}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Loop through all .txt files and plot all columns
for file in txt_files:
    print(f"Processing {file}...")
    plot_all_columns(file, output_dir)

print(f"All plots saved to {output_dir}")