
# editor zhaoliyuan
# 2019-10-16
# this file is for analysising the data got from database

import numpy as np
import pandas as pd
from datetime import datetime
from ipdb import set_trace
import statsmodels.api as sm
from sqlhelper import batch
from sqlhelper.tableToDataframe import toSQL, toDf
import loadData
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import logging

logger = logging.getLogger(__name__)

Base = declarative_base()


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

def ratio(df, step, column = 'age'):
    df.sort_values(column, inplace = True, ascending = True)
    ratio = list()
    for i in range(len(df)):
        col = df[column].iloc[i]
        allExpenditure = df[df[column] >= col]['expenditure'].sum()
        dfE = df[df[column] >= col]
        dfE = dfE[dfE[column] < (col + step)]
        expenditure = dfE['expenditure'].sum()
        ratio.append(expenditure / allExpenditure)

    return ratio


#class prophet_family_free(Base):
#    
#    __tablename__  = 'prophet_family_free'
#
#    id = Column(Integer, primary_key = True)
#    ff_uid = Column(String)
#    ff_batch_id = Column(String)
#    ff_type = Column(Integer)
#    ff_risk = Column(Float)
#    ff_is_select = Column(Integer)
#    ff_age = Column(Integer)
#    created_at = Column(DateTime)
#    updates_at = Column(DateTime)
#
## select good users from database
## if all needs of a user can be fullfilled then the user is a good user
## ff_age = -1 means that the need  cannot be realized
#def goodUser():
#    sql = toSQL('prophet')
#    sql = sql.query(prophet_family_free.ff_uid, prophet_family_free.ff_age, prophet_family_free.ff_batch_id, prophet_family_free.created_at).statement
#    df = toDf(key = 'prophet', sql = sql, parse_dates = '')
#    df.sort_values(by = 'created_at', ascending = False, inplace = True)
#    df.drop_duplicates(subset = ['ff_uid','ff_batch_id'], keep = 'first', inplace = True)
#    uids = df[['ff_uid']].drop_duplicates('ff_uid',keep = 'first')
#    goodUser = list()
#    for uid in uids['ff_uid']:
#        tmp = df[df['ff_uid']==uid]
#        if (tmp['ff_age'] != -1).all():    
#            goodUser.append(uid)
#
#    return goodUser
#
#goodID = goodUser()
#
#df = pd.read_excel('output.xlsx', index_col = 0, sheet_name = 1)
#df = df[df.index.isin(goodID)]
#df.to_excel('outputGoodUsers.xlsx')
#

#df = pd.read_excel('outputGoodUsers.xlsx', sheet_name = 0)
#dfAll = df[['age','income','expenditure']]
#dfAdjusted = pd.DataFrame(columns = ['age','income','expenditure'])
#ageMin = dfAll.age.min()
#for age in range(ageMin,86):
#    df = dfAll[dfAll['age'] == age]
#    df = group(df, 'income', 100000).groupby('group').mean()
#    df['age'] = age
#    dfAdjusted = pd.concat([dfAdjusted, df], axis = 0)
#
#ratioOneYear = ratio(dfAdjusted, step = 1)
#ratioTwoYear = ratio(dfAdjusted, step = 2)
#ratioThreeYear = ratio(dfAdjusted, step = 3)
#ratioFourYear = ratio(dfAdjusted, step = 4)
#ratioFiveYear = ratio(dfAdjusted, step = 5)
#ratioSixYear = ratio(dfAdjusted, step = 6)
#ratioSevenYear = ratio(dfAdjusted, step = 7)
#ratioEightYear = ratio(dfAdjusted, step = 8)
#ratioNineYear = ratio(dfAdjusted, step = 9)
#ratioTenYear = ratio(dfAdjusted, step = 10)
#
#dfAdjusted['ratioOneYear'] = ratioOneYear
#dfAdjusted['ratioTwoYear'] = ratioTwoYear
#dfAdjusted['ratioThreeYear'] = ratioThreeYear
#dfAdjusted['ratioFourYear'] = ratioFourYear 
#dfAdjusted['ratioFiveYear'] = ratioFiveYear 
#dfAdjusted['ratioSixYear'] = ratioSixYear
#dfAdjusted['ratioSevenYear'] = ratioSevenYear
#dfAdjusted['ratioEightYear'] = ratioEightYear
#dfAdjusted['ratioNineYear'] = ratioNineYear 
#dfAdjusted['ratioTenYear'] = ratioTenYear
#
#dfAdjusted.to_excel('outputGoodUsersGroupedbyIncome.xlsx')

df = pd.read_excel('outputGoodUsersGroupedbyIncome.xlsx', sheet_name = 0, index_col = 0)
df = df[df['income']<10000000]
df = df[df['expenditure']<2000000]
df.sort_values('age', ascending = True, inplace = True)
oneThree = []
threeTen = []
for i in range(len(df)):
    oneThree.append(df['ratioOneYear'].iloc[i]/df['ratioThreeYear'].iloc[i])
    threeTen.append(df['ratioThreeYear'].iloc[i]/df['ratioTenYear'].iloc[i])

df['one/three'] = oneThree
df['three/ten'] = threeTen

wellDf = df[['age', 'income', 'expenditure', 'one/three', 'three/ten']]
wellDf = wellDf.reset_index(drop = True)

wellDf.to_excel('well_done.xlsx')

#df = pd.read_excel('output.xlsx',index_col = 0, sheet_name = 0)
#df0 = df.copy()
#df = pd.read_excel('output.xlsx',sheet_name = 1)
#df1 = df.copy()
#
## make a new dataframe
#df0.columns = ['uid','age','asset','expenditure','created_at']
#df0.drop(['uid','expenditure','created_at'], inplace = True, axis = 1)
#df1.drop('uid', inplace = True, axis = 1)
## firstly use mean value to calculate see people in the same age as one single person
#df0 = df0.groupby('age').mean()
#df0.reset_index(inplace = True)
#df1 = df1.groupby('age').mean()
#df1.reset_index(inplace = True)

#ratioOneYear = ratio(df1, step = 1)
#ratioTwoYear = ratio(df1, step = 2)
#ratioThreeYear = ratio(df1, step = 3)
#ratioFourYear = ratio(df1, step = 4)
#ratioFiveYear = ratio(df1, step = 5)
#ratioSixYear = ratio(df1, step = 6)
#ratioSevenYear = ratio(df1, step = 7)
#ratioEightYear = ratio(df1, step = 8)
#ratioNineYear = ratio(df1, step = 9)
#ratioTenYear = ratio(df1, step = 10)
#
#df0.sort_values('age', inplace = True, ascending = True)
#df1.sort_values('age', inplace = True, ascending = True)
#df0.set_index('age', inplace = True)
#df1.set_index('age', inplace = True)
#newDf = pd.merge(df0, df1, left_index = True, right_index = True)
#expenditure = newDf['expenditure']
#newDf.drop('expenditure', axis = 1, inplace = True)
#newDf['expenditure'] = expenditure
#newDf['ratioOneYear'] = ratioOneYear
#newDf['ratioTwoYear'] = ratioTwoYear
#newDf['ratioThreeYear'] = ratioThreeYear
#newDf['ratioFourYear'] = ratioFourYear 
#newDf['ratioFiveYear'] = ratioFiveYear 
#newDf['ratioSixYear'] = ratioSixYear
#newDf['ratioSevenYear'] = ratioSevenYear
#newDf['ratioEightYear'] = ratioEightYear
#newDf['ratioNineYear'] = ratioNineYear 
#newDf['ratioTenYear'] = ratioTenYear
#
#newDf.to_excel('analysisGrouped.xlsx')

## analysis relation between expenditure and age
#age_expenditure = pd.DataFrame()
#age_expenditure['age'] = df.cc_age
#age_expenditure['expenditure'] = df.cc_expenditure_asset
#
## use mean value to calculate 
#age_expenditure = age_expenditure.groupby('age')['expenditure'].mean()
#age_expenditure.to_excel('ageExpenditure.xlsx')

## analysis relation between expenditure and investable asset
#ie = df.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie.columns = ['asset','expenditure']
#
#ie30 = df[df['cc_age']<30]
#ie30 = ie30.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie30.columns = ['asset','expenditure']
#
#ie40 = df[df['cc_age']>=30]
#ie40 = ie40[ie40['cc_age']<40]
#ie40 = ie40.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie40.columns = ['asset','expenditure']
#
#ie50 = df[df['cc_age']>=40]
#ie50 = ie50[ie50['cc_age']<50]
#ie50 = ie50.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie50.columns = ['asset','expenditure']
#
#ie60 = df[df['cc_age']>=50]
#ie60 = ie60[ie60['cc_age']<60]
#ie60 = ie60.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie60.columns = ['asset','expenditure']
#
#ie70 = df[df['cc_age']>=60]
#ie70 = ie70[ie70['cc_age']<70]
#ie70 = ie70.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie70.columns = ['asset','expenditure']
#
#ie86 = df[df['cc_age']>=70]
#ie86 = ie86[ie86['cc_age']<86]
#ie86 = ie86.loc[:,['cc_investable_asset','cc_expenditure_asset']]
#ie86.columns = ['asset','expenditure']

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

#ie  = group(ie, 'asset', 100000).groupby('group').mean()
#ie30  = group(ie30, 'asset', 100000).groupby('group').mean()
#ie40  = group(ie40, 'asset', 100000).groupby('group').mean()
#ie50  = group(ie50, 'asset', 100000).groupby('group').mean()
#ie60  = group(ie60, 'asset', 100000).groupby('group').mean()
#ie70  = group(ie70, 'asset', 100000).groupby('group').mean()
#ie86  = group(ie86, 'asset', 100000).groupby('group').mean()
#
#excel = pd.ExcelWriter('assetExpenditureGrouped.xlsx')
#ie.to_excel(excel, 'all')
#ie30.to_excel(excel, '30')
#ie40.to_excel(excel, '40')
#ie50.to_excel(excel, '50')
#ie60.to_excel(excel, '60')
#ie70.to_excel(excel, '70')
#ie86.to_excel(excel, '86')
#excel.save()


## analysis relation between expenditure and income asset
#ie = df.loc[:,['income','expenditure']]
#
#ie30 = df[df['age']<30]
#ie30 = ie30.loc[:,['income','expenditure']]
#
#ie40 = df[df['age']>=30]
#ie40 = ie40[ie40['age']<40]
#ie40 = ie40.loc[:,['income','expenditure']]
#
#ie50 = df[df['age']>=40]
#ie50 = ie50[ie50['age']<50]
#ie50 = ie50.loc[:,['income','expenditure']]
#
#ie60 = df[df['age']>=50]
#ie60 = ie60[ie60['age']<60]
#ie60 = ie60.loc[:,['income','expenditure']]
#
#ie70 = df[df['age']>=60]
#ie70 = ie70[ie70['age']<70]
#ie70 = ie70.loc[:,['income','expenditure']]
#
#ie86 = df[df['age']>=70]
#ie86 = ie86[ie86['age']<86]
#ie86 = ie86.loc[:,['income','expenditure']]
#
#ie  = group(ie, 'income', 100000).groupby('group').mean()
#ie30  = group(ie30, 'income', 100000).groupby('group').mean()
#ie40  = group(ie40, 'income', 100000).groupby('group').mean()
#ie50  = group(ie50, 'income', 100000).groupby('group').mean()
#ie60  = group(ie60, 'income', 100000).groupby('group').mean()
#ie70  = group(ie70, 'income', 100000).groupby('group').mean()
#ie86  = group(ie86, 'income', 100000).groupby('group').mean()
#
#excel = pd.ExcelWriter('incomeExpenditureGrouped.xlsx')
#ie.to_excel(excel, 'all')
#ie30.to_excel(excel, '30')
#ie40.to_excel(excel, '40')
#ie50.to_excel(excel, '50')
#ie60.to_excel(excel, '60')
#ie70.to_excel(excel, '70')
#ie86.to_excel(excel, '86')
#excel.save()
#
# analysis ratio using grouped income
##df = pd.read_excel('incomeExpenditureGrouped.xlsx')
#dfBasic = pd.read_excel('analysis.xlsx')
#dfBasic.sort_values('uid', inplace = True, ascending = True)
#uid = dfBasic['uid']
#dfBasic = dfBasic.reset_index()
#dfBasic.drop('index', axis = 1, inplace = True)
#uid.drop_duplicates(inplace = True)
#dfAll = pd.DataFrame(columns = ['uid', 'age', 'asset', 'income', 'expenditure', 'ratioOneYear', 'ratioTwoYear', 'ratioThreeYear', 'ratioFourYear', 'ratioFiveYear', 'ratioSixYear', 'ratioSevenYear', 'ratioEightYear', 'ratioNineYear', 'ratioTenYear'])
#for ID in uid:
#    df = dfBasic[dfBasic['uid'] == ID]
#    df['ratioOneYear'] = ratio(df ,step = 1)
#    df['ratioTwoYear'] = ratio(df ,step = 2)
#    df['ratioThreeYear'] = ratio(df ,step = 3)
#    df['ratioFourYear'] = ratio(df ,step = 4)
#    df['ratioFiveYear'] = ratio(df ,step = 5)
#    df['ratioSixYear'] = ratio(df ,step = 6)
#    df['ratioSevenYear'] = ratio(df ,step = 7)
#    df['ratioEightYear'] = ratio(df ,step = 8)
#    df['ratioNineYear'] = ratio(df, step = 9)
#    df['ratioTenYear'] = ratio(df, step = 10)
##    dfBasic[dfBasic['uid'] == ID]['ratioOneYear'] = df['ratioOneYear'] 
##    dfBasic[dfBasic['uid'] == ID]['ratioTwoYear'] = df['ratioTwoYear'] 
##    dfBasic[dfBasic['uid'] == ID]['ratioThreeYear'] = df['ratioThreeYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioFourYear'] = df['ratioFourYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioFiveYear'] = df['ratioFiveYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioSixYear'] = df['ratioSixYear'] 
##    dfBasic[dfBasic['uid'] == ID]['ratioSevenYear'] = df['ratioSevenYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioEightYear'] = df['ratioEightYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioNineYear'] = df['ratioNineYear']  
##    dfBasic[dfBasic['uid'] == ID]['ratioTenYear'] = df['ratioTenYear']  
#    dfAll = pd.concat([dfAll,df], axis = 0)
#
#dfAll.to_excel('fullDataForEveryone.xlsx')

#dfAll = pd.read_excel('fullDataForEveryone.xlsx',index_col = 0, sheet_name = 0)
#dfAll = dfAll[['age','income','expenditure']]
#dfAdjusted = pd.DataFrame(columns = ['age','income','expenditure'])
#ageMin = dfAll.age.min()
#for age in range(ageMin,86):
#    df = dfAll[dfAll['age'] == age]
#    df = group(df, 'income', 100000).groupby('group').mean()
#    df['age'] = age
#    dfAdjusted = pd.concat([dfAdjusted, df], axis = 0)
#
#dfAdjusted.to_excel('nicedataforanalysis.xlsx')

#dfTmp = pd.read_excel('nicedataforanalysis.xlsx')
#ratioOneYear = ratio(dfTmp, step = 1)
#ratioTwoYear = ratio(dfTmp, step = 2)
#ratioThreeYear = ratio(dfTmp, step = 3)
#ratioFourYear = ratio(dfTmp, step = 4)
#ratioFiveYear = ratio(dfTmp, step = 5)
#ratioSixYear = ratio(dfTmp, step = 6)
#ratioSevenYear = ratio(dfTmp, step = 7)
#ratioEightYear = ratio(dfTmp, step = 8)
#ratioNineYear = ratio(dfTmp, step = 9)
#ratioTenYear = ratio(dfTmp, step = 10)
#                        
#dfTmp['ratioOneYear'] = ratioOneYear
#dfTmp['ratioTwoYear'] = ratioTwoYear
#dfTmp['ratioThreeYear'] = ratioThreeYear
#dfTmp['ratioFourYear'] = ratioFourYear 
#dfTmp['ratioFiveYear'] = ratioFiveYear 
#dfTmp['ratioSixYear'] = ratioSixYear
#dfTmp['ratioSevenYear'] = ratioSevenYear
#dfTmp['ratioEightYear'] = ratioEightYear
#dfTmp['ratioNineYear'] = ratioNineYear 
#dfTmp['ratioTenYear'] = ratioTenYear
#
#                        
#dfTmp.to_excel('niceDataForRatio.xlsx')

#dfTmp = pd.read_excel('niceDataForRatio.xlsx',index_col = 0, sheet_name = 0)
#dfTmp = dfTmp[dfTmp['age']<70]
#dfTmp = dfTmp[dfTmp['income']<10000000]
#dfTmp.to_excel('niceDataAdjusted.xlsx')

#dfTmp = pd.read_excel('niceDataAdjusted.xlsx')
#dfTmp30 = dfTmp[dfTmp['age']<30]
#dfTmp40 = dfTmp[dfTmp['age']<40]
#dfTmp50 = dfTmp[dfTmp['age']<50]
#dfTmp60 = dfTmp[dfTmp['age']<60]
#dfTmp86 = dfTmp[dfTmp['age']>=60]
#
#excel = pd.ExcelWriter('niceDataAdjustedGrouped.xlsx')
#dfTmp30.to_excel(excel, '30')
#dfTmp40.to_excel(excel, '40')
#dfTmp50.to_excel(excel, '50')
#dfTmp60.to_excel(excel, '60')
#dfTmp86.to_excel(excel, '86')
#
#excel.save()

#X = df[['age', 'income']].values
#y = df['expenditure'].values
#ols = sm.OLS(y,sm.add_constant(X).fit())

