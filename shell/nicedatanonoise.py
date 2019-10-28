:# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:52:10 2019

@author: 86156
"""

import pandas as pd

df = pd.read_excel('niceDataAdjusted.xlsx', index_col = 0)

expenditure = df[['expenditure']]

expenditure = expenditure.sort_values('expenditure').reset_index()

expenditure.drop('index', axis = 1, inplace = True)

a = len(expenditure[expenditure['expenditure']>1000000]) / len(expenditure)

df = df[df['expenditure'] <1000000]

df.to_excel('niceDataAdjustedNoNoise100.xlsx')