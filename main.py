import pandas as pd
import numpy as np

# Read in CSV
df = pd.read_csv('proteins.csv')

# Convert columns to np arrays
proteomes = df[['proteome']].to_numpy().astype(str)
phosphoproteomes = df[['phosphoproteome']].to_numpy().astype(str)

# Find items that are only proteomes, only phosphoproteomes, then both proteomes and phosphoproteomes
proteomes_only = np.setdiff1d(proteomes, phosphoproteomes)
phosphoproteomes_only = np.setdiff1d(phosphoproteomes, proteomes)
intersection = np.intersect1d(proteomes, phosphoproteomes)

# Put them in a CSV file
pd.concat([pd.DataFrame(proteomes_only), pd.DataFrame(phosphoproteomes_only), pd.DataFrame(intersection)], axis=1).to_csv('savefile.csv', index=False, header=['Proteomes', 'Phosphoroteomes', 'Both']) 