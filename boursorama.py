import pandas as pd
import numpy as np
import re
import math
import sys

dict = {
    'S': 'SUPERMARKET',
    'H': 'HEALTH',
    'M': 'MEAL',
    '1': 'ONE-TIME',
    'C': 'CLOTHES',
    'B': 'BEER',
    'G': 'GYM',
    'R': 'REIMBURSEMENT',
    'L': 'LEISURE',
    'T': 'TRANSPORT',
    'V': 'TRAVEL',
    '$': 'BANK',
}

def convert_shorthand(s):
    if s in dict:
        return dict[s]
    return s

def print_dict():
    count = 0;
    for k in dict:
        count += 1
        print(f'{k}: {dict[k]: <16}', end='')
        if count%4 == 0:
            print()

FILENAME = sys.argv[1]
BOURSORAMA_FILENAME = "./" + FILENAME

df = pd.read_csv(BOURSORAMA_FILENAME, sep=';').replace(np.nan, '')
cats = pd.read_csv("/home/guissmo/scripts/finances/cats.csv")

merged = df.merge(cats, how='left', left_on='supplierFound', right_on='Merchant')
unknown_cats = merged[merged['Category'].isnull()]
unknown_cats_unique = unknown_cats['supplierFound'].unique()
new_cats = cats.copy()

for x in unknown_cats_unique:
    arr = cats['Category'].unique()
    print(df[x == df['supplierFound']][['dateOp', 'amount', 'supplierFound', 'category']])
    print()
    count = 0
    for k in dict:
        count += 1
        print(f'{k}: {dict[k]: <16}', end='')
        if count%4 == 0:
            print()
    print()
    n = '?'
    while n == '?':
        n = input().upper()
        if n == 'Q':
            break
        if n == '?':
            print([a for a in arr if 'TRAVEL' not in a and 'TRANSFER' not in a and 'CONFERENCE' not in a])
    if n == 'Q':
        break
    y = convert_shorthand(n)
    new_cats = pd.concat([new_cats, pd.DataFrame({'Merchant': [x], 'Category': [y]})])

new_cats.drop_duplicates(inplace=True, keep='first')
new_merged = df.merge(new_cats, how='left', left_on='supplierFound', right_on='Merchant')

import re

def replace_comma(s):
    if type(s) == float:
        return s
    return float(re.sub(' ','',re.sub(',','.',s)))

new_merged['amount'] = new_merged['amount'].apply(replace_comma)
new_merged['dateOp'] = pd.to_datetime(new_merged['dateOp'].apply(str), format='%d/%m/%Y')

to_export = new_merged[['dateOp', 'amount', 'Merchant', 'Category']].copy()
to_export.rename(columns={'dateOp': 'Date', 'amount': 'Amount'}, inplace=True)
to_export.to_csv('./PROCESSED_' + FILENAME, index=False)
new_cats[['Merchant', 'Category']].to_csv('./new_cats.csv', index=False)