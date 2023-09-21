# What Is This

These are my scripts to keep a CSV of all my expenses.

The files `accumulated.csv` and `cats.csv` are not included since I would like to keep my expenses private but I added `accumulated_sample.csv` and `cats_sample.csv` to let you know how they should look in the off-chance you are interested in adapting this code.

I'm documenting and maintaining this for myself. Feel free to study the code and learn if you think it's useful for you.

# Requirements

Looking at the imports, I'm using import `pandas`, `numpy`, `re`, `math` and `sys`.

# Usage

## Boursorama

1. Paste Boursorama CSV on this directory.
2. Run `python3 boursorama.py [filename]`.
3. Run `script.sh PROCESSED_[filename]`.
4. Run `script2.sh` to clean up accumulated.csv and cats.csv.

## LCL

1. Paste LCL CSV on this directory.
2. Run `python3 lcl.py [filename]`.
3. Run `script.sh PROCESSED_[filename]`.
4. Run `script2.sh` to clean up accumulated.csv and cats.csv.