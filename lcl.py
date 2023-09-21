import pandas as pd
import numpy as np
import re
import math
import sys

def replace(s):
    t = re.sub(r'\d{2}\/\d{2}/\d{2}', '', s)
    t = re.sub(r'\d{2}\/\d{2}', '', t)
    u = re.sub(r' +', ' ', t)
    return u.strip()

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
LCL_FILENAME = "./" + FILENAME

df = pd.read_csv(LCL_FILENAME, sep=';', header=None, names=["Date", "Amount", "Type", "?", 4, 5, 6, 7]).replace(np.nan, '')[:-1]
cats = pd.read_csv("/home/guissmo/scripts/finances/cats.csv")

df["Merchant"] = df.apply(lambda x: replace(x[4]) or replace(x[5]), axis=1)
merged = df.merge(cats, how='left')
unknown_cats = merged[merged['Category'].isnull()]
unknown_cats_unique = unknown_cats['Merchant'].unique()
new_cats = cats.copy()

for x in unknown_cats_unique:
    arr = cats['Category'].unique()
    if x == '':
    	continue
    print(df[x == df['Merchant']][['Date', 'Amount', 'Merchant']])
    print()
    print_dict()
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
new_merged = df.merge(new_cats, how='left')

import re

def replace_comma(s):
    if type(s) == float:
        return s
    return float(re.sub(' ','',re.sub(',','.',s)))

new_merged['Amount'] = new_merged['Amount'].apply(replace_comma)
new_merged['Date'] = pd.to_datetime(new_merged['Date'].apply(str), format='%d/%m/%Y')

new_merged[['Date', 'Amount', 'Merchant', 'Category']].to_csv('./PROCESSED_' + FILENAME, index=False)
new_cats[['Merchant', 'Category']].to_csv('./new_cats.csv', index=False)