import pandas as pd
import numpy as np

# Read in targets
df = pd.read_csv('mir2gene.csv')
targets = df[['ID', 'Target']].to_numpy().astype(str)

# Read in up, down, and unchanged
df = pd.read_csv('proteins_2.csv')

up = df[['upregulated']].to_numpy().astype(str)
down = df[['downregulated']].to_numpy().astype(str)
unchanged = df[['unchanged']].to_numpy().astype(str)


# Find up in target list
up_targets = targets[np.in1d(targets[:,1], up)]
# Find down in target list
down_targets = targets[np.in1d(targets[:,1], down)]
# Find unchanged in target list
unchanged_targets = targets[np.in1d(targets[:,1], unchanged)]
# Find the target proteins that are not present in all
all = df[['all']].to_numpy().astype(str)
all_targets = targets[np.in1d(targets[:,1], all, invert=True)]


# Send all of this to excel file
writer = pd.ExcelWriter('task2.xlsx', engine='xlsxwriter')
pd.DataFrame(up_targets).to_excel(writer, sheet_name='Upregulated', index=False, header=['ID', 'Target'])
pd.DataFrame(down_targets).to_excel(writer, sheet_name='Downregulated', index=False, header=['ID', 'Target'])
pd.DataFrame(unchanged_targets).to_excel(writer, sheet_name='Unchanged', index=False, header=['ID', 'Target'])
pd.DataFrame(all_targets).to_excel(writer, sheet_name='Other', index=False, header=['ID', 'Target'])
writer.save()
