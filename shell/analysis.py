
# editor zhaoliyuan
# 2019-10-16
# this file is for analysising the data got from database

import numpy as np
import pandas as pd
from datetime import datetime
from ipdb import set_trace

df = pd.read_excel('output.xlsx',sheet_name = 0)

## analysis relation between expenditure and age
#age_expenditure = pd.DataFrame()
#age_expenditure['age'] = df.cc_age
#age_expenditure['expenditure'] = df.cc_expenditure_asset
#
## use mean value to calculate 
#age_expenditure = age_expenditure.groupby('age')['expenditure'].mean()
#age_expenditure.to_excel('ageExpenditure.xlsx')

# analysis relation between expenditure and investable asset
ie = df.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie.columns = ['asset','expenditure']

ie30 = df[df['cc_age']<30]
ie30 = ie30.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie30.columns = ['asset','expenditure']

ie40 = df[df['cc_age']>=30]
ie40 = ie40[ie40['cc_age']<40]
ie40 = ie40.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie40.columns = ['asset','expenditure']

ie50 = df[df['cc_age']>=40]
ie50 = ie50[ie50['cc_age']<50]
ie50 = ie50.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie50.columns = ['asset','expenditure']

ie60 = df[df['cc_age']>=50]
ie60 = ie60[ie60['cc_age']<60]
ie60 = ie60.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie60.columns = ['asset','expenditure']

ie70 = df[df['cc_age']>=60]
ie70 = ie70[ie70['cc_age']<70]
ie70 = ie70.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie70.columns = ['asset','expenditure']

ie86 = df[df['cc_age']>=70]
ie86 = ie86[ie86['cc_age']<86]
ie86 = ie86.loc[:,['cc_investable_asset','cc_expenditure_asset']]
ie86.columns = ['asset','expenditure']

## use mean value to calculate
#ie = ie.groupby('asset')['expenditure'].mean()
#ie30 = ie30.groupby('asset')['expenditure'].mean()
#ie40 = ie40.groupby('asset')['expenditure'].mean()
#ie50 = ie50.groupby('asset')['expenditure'].mean()
#ie60 = ie60.groupby('asset')['expenditure'].mean()
#ie70 = ie70.groupby('asset')['expenditure'].mean()
#ie86 = ie86.groupby('asset')['expenditure'].mean()
#
#excel = pd.ExcelWriter('assetExpenditure.xlsx')
#ie.to_excel(excel, 'all')
#ie30.to_excel(excel, '30')
#ie40.to_excel(excel, '40')
#ie50.to_excel(excel, '50')
#ie60.to_excel(excel, '60')
#ie70.to_excel(excel, '70')
#ie86.to_excel(excel, '86')
#excel.save()

# analysis in groups
# diff <= 100000 is considerd in the same group

def group (df, column, step):
    df.sort_values(by = [column], inplace = True, ascending = True)
    df['group'] = 0
    v0 = df[column].iloc[0]
    number = 0
    for i in range(len(df)):
        v = df[column].iloc[i]
        if v > step + v0:
            number += 1
            v0 = df[column].iloc[i]

        df['group'].iloc[i] = number

    df.set_index('group' ,inplace = True)
    
    return df

ie  = group(ie, 'asset', 100000).groupby('group').mean()
ie30  = group(ie30, 'asset', 100000).groupby('group').mean()
ie40  = group(ie40, 'asset', 100000).groupby('group').mean()
ie50  = group(ie50, 'asset', 100000).groupby('group').mean()
ie60  = group(ie60, 'asset', 100000).groupby('group').mean()
ie70  = group(ie70, 'asset', 100000).groupby('group').mean()
ie86  = group(ie86, 'asset', 100000).groupby('group').mean()

excel = pd.ExcelWriter('assetExpenditureGrouped.xlsx')
ie.to_excel(excel, 'all')
ie30.to_excel(excel, '30')
ie40.to_excel(excel, '40')
ie50.to_excel(excel, '50')
ie60.to_excel(excel, '60')
ie70.to_excel(excel, '70')
ie86.to_excel(excel, '86')
excel.save()


