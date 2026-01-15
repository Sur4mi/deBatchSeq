# This script learns how each batch systematically distorts gene measurements and then reverses 
# those distortions so all samples so all samples can be compared without technical batch bias

import pandas as pd
from pycombat import Combat

# Load logCPM gene expression data previously generated
expr = pd.read_csv("expression_logCPM.csv", index_col=0, sep=None, engine='python')

# Load  sample metadata
meta = pd.read_csv("metadata.csv", sep=None, engine='python').set_index("sample")

# Transpose expression data to (samples, genes) for pycombat (inverts columns and rows)
expr_t = expr.T

# Make sure order of samples matches expression rows by aligning metadata
meta = meta.loc[expr_t.index]

# Batch variable: assigna batch value for each sample
batch = meta["batch"].values

# Identify genes with zero variance (constant across all samples, 
# which will not be batch corrected but still included in the analysis)
var_mask = expr_t.var() > 0

# Apply pycombat only to variable genes
if var_mask.sum() > 0:
    expr_t_var = expr_t.loc[:, var_mask]
    combat = Combat()
    
    # Fit and transform the data
    corrected_t_np = combat.fit_transform(expr_t_var.values, batch)
    
    # Convert back to DataFrame and merge with original data to handle NaNs/constants
    corrected_t = expr_t.copy()
    corrected_t.loc[:, var_mask] = corrected_t_np
else:
    corrected_t = expr_t

# Transpose back to the initial data frame (genes, samples)
corrected = corrected_t.T

# Save corrected data to a new csv file
corrected.to_csv("expression_batch_corrected.csv")

print("Done!")

