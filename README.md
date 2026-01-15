# deBatchSeq
Python utilities for correcting batch effects in RNA-seq datasets

**deBatchSeq** is a lightweight Python toolkit for correcting batch effects in RNA-seq data, based on pycombat.  
It is designed to be simple and easy to integrate.

## Features
- Correct batch effects in bulk or single-cell RNA-seq datas
- Lightweight and easy to use

## Dependencies
This project uses the following Python libraries:
**NumPy** – for numerical operations
**pandas** – for data manipulation and reading/writing CSV files
**pyComBat** – for batch effect correction

## lib_normalization.py
- **Purpose**: Reads raw RNA-seq counts from a CSV file, normalizes by library size, applies log2 transformation, and outputs a normalized CSV.
- **Input**: Replace raw_counts.csv with your raw count file.
- **Output**: expression_logCPM.csv

## debatch.py
- **Purpose**: Reads normalized RNA-seq data and associated metadata to perform batch effect correction.
- **Inputs**:
Normalized expression file: **expression_logCPM.csv** (output of lib_normalization.py)
Metadata file: **metadata.csv** a CSV containing batch information and sample annotations (created by the user). Must include a column specifying the batch assignment for each sample.
    Example structure:
        Header: sample,batch
        name_sample,number_batch
        name_sample,number_batch
        name_sample,number_batch
        ...
- **Output**: **expression_batch_corrected.csv** – batch-corrected expression matrix ready for downstream analysis.