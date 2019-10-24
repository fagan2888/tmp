# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:57:10 2019

@author: 86156
"""

import statsmodels.api as sm
import pandas as pd

df1 = pd.read_excel('nicedata.xlsx',index_col =0 , sheet_name = 0)
df2 = pd.read_excel('nicedata.xlsx', index_col = 0, sheet_name = 1)

# 分析年龄，收入和支出
X1 = df1[['age','income']].values
y1 = df1['expenditure'].values
model1 = sm.OLS(y1,sm.add_constant(X1))
result1 = model1.fit()
print(result1.params)
print(result1.summary())

X2 = df1[['age^5*0.01','ln(income)*100000']].values
y2 = df1['expenditure'].values
model2 = sm.OLS(y2,sm.add_constant(X2))
result2 = model2.fit()
print(result2.params)
print(result2.summary())

# 分析年龄，收入和支出比例

X2_1 = df2[['age','income']].values
y2_1 = df2['one/three'].values
model2_1 = sm.OLS(y2_1,sm.add_constant(X2_1))
result2_1 = model2_1.fit()
print(result2_1.params)
print(result2_1.summary())

X2_2 = df2[['age','income']].values
y2_2 = df2['three/ten'].values
model2_2 = sm.OLS(y2_2,sm.add_constant(X2_2))
result2_2 = model2_2.fit()
print(result2_2.params)
print(result2_2.summary())


df = pd.read_excel('niceDataAdjusted.xlsx',index_col =0 , sheet_name = 0)

df = pd.read_excel('niceDataAdjustedNoNoise.xlsx',index_col =0 , sheet_name = 0)

df = pd.read_excel('niceDataAdjustedNoNoise100.xlsx',index_col =0 , sheet_name = 0)

# 分析年龄，收入和支出
X1 = df[['age','income']].values
y1 = df['expenditure'].values
model1 = sm.OLS(y1,sm.add_constant(X1))
result1 = model1.fit()
print(result1.params)
print(result1.summary())

X2 = df[['age^5*0.01','ln(income)*100000']].values
y2 = df['expenditure'].values
model2 = sm.OLS(y2,sm.add_constant(X2))
result2 = model2.fit()
print(result2.params)
print(result2.summary())

# 分析年龄，收入和支出比例

X2_1 = df[['age','income']].values
y2_1 = df['one/three'].values
model2_1 = sm.OLS(y2_1,sm.add_constant(X2_1))
result2_1 = model2_1.fit()
print(result2_1.params)
print(result2_1.summary())

X2_2 = df[['age'，'income']].values

df = df[df['age']>=55]
X2_2 = df[['age']].values

y2_2 = df['three/ten'].values
model2_2 = sm.OLS(y2_2,sm.add_constant(X2_2))
result2_2 = model2_2.fit()
print(result2_2.params)
print(result2_2.summary())


# 分年龄讨论
df30 = pd.read_excel('niceDataAdjustedGrouped.xlsx', index_col = 0, sheet_name = 0)
df40 = pd.read_excel('niceDataAdjustedGrouped.xlsx', index_col = 0, sheet_name = 1)
df50 = pd.read_excel('niceDataAdjustedGrouped.xlsx', index_col = 0, sheet_name = 2)
df60 = pd.read_excel('niceDataAdjustedGrouped.xlsx', index_col = 0, sheet_name = 3)
df86 = pd.read_excel('niceDataAdjustedGrouped.xlsx', index_col = 0, sheet_name = 4)

# 分析一年/三年

df30['one/three'].max()


min40 = df40['one/three'].min()
max40 = df40['one/three'].max()
mean30 

min50 = df50['one/three'].min()
max50 = df50['one/three'].max()

min60 = df60['one/three'].min()
max60 = df60['one/three'].max()

min86 = df86['one/three'].min()
max86 = df86['one/three'].max()

#分析三年/十年



