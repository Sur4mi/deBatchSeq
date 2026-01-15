#This script converts raw RNA-seq read counts into log-scaled, library-size-normalized 
# expression values so samples can be compared without being biased by sequencing depth.

import pandas as pd
import numpy as np

# Load raw read counts csv file
counts = pd.read_csv("prova.csv", index_col=0, sep=None, engine='python')

# Calculate library size per sample (total reads per sample)
library_sizes = counts.sum(axis=0)

# CPM (count per million) normalization
cpm = counts.div(library_sizes, axis=1) * 1e6

# Apply log2(CPM + 1) keeping the genes with zero expression
logcpm = np.log2(cpm + 1)

# Save normalized data to a new csv file
logcpm.to_csv("expression_logCPM.csv")

print("Done!")

# Checks that there are no negative values/log of zero
print(logcpm.min().min())