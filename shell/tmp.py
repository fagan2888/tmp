
import numpy as np
import pandas as pd
from sqlalchemy import *
from datetime import datetime
from sqlhelper import batch
from ipdb import set_trace
##连接到现在的数据库
#db = database.connection('wind_sync')
#metadata = sql.MetaData(bind=db)
#t = sql.Table('caihui_exchange_rate', metadata, autoload=True)
#columns = [
#    t.c.cer_tradedate,
#    t.c.cer_exchangeprice,
#    t.c.cer_pcur,
#    t.c.cer_excur,
#    t.c.cer_pricetype,
#    t.c.cer_datasource,
#]
#s = sql.select(columns)
#baseDf = pd.read_sql(s,db)
#baseDf = baseDf.set_index(['cer_tradedate','cer_pcur'])

# 基金池基金
db = batch.connection('asset')
metadata = MetaData(bind = db)
t = Table('ra_pool_fund',metadata, autoload = True)

columns = [
    t.c.ra_pool,
    t.c.ra_fund_code,
    t.c.ra_date,
        ]

sql = select(columns).where(t.c.ra_pool.in_([
'11110100',
'11110106',
'11110108',
'11110110',
'11110112',
'11110114',
'11110116',
'11110200']))

pools = [
'11110100',
'11110106',
'11110108',
'11110110',
'11110112',
'11110114',
'11110116',
'11110200']

code = pd.read_sql(sql, db)
new = pd.DataFrame(columns = ['ra_pool','ra_fund_code','ra_date'])
for pool in pools:
    newCode = code[code['ra_pool']== pool]
    date = newCode['ra_date'].max()
    newCode = newCode[newCode['ra_pool'].isin(pools)]
    newCode = newCode[newCode['ra_date'] == date]
    new = pd.concat([new, newCode], axis = 0)

code = list(new['ra_fund_code'])

print(code)
set_trace()

db = batch.connection('wind_db')
metadata = MetaData(bind = db)
t = Table('chinamutualfunddescription',metadata, autoload = True)

columns = [
    t.c.F_INFO_WINDCODE,
    t.c.F_INFO_FRONT_CODE,
        ]

sql = select(columns).where(t.c.F_INFO_FRONT_CODE.in_(code))

df = pd.read_sql(sql, db)

secode = df['F_INFO_WINDCODE']

secode = list(secode)

# 基金池持股情况
db = batch.connection('wind_db')
metadata = MetaData(bind = db)
t = Table('chinamutualfundstockportfolio',metadata, autoload = True)

columns = [
    t.c.S_INFO_WINDCODE,
    t.c.ANN_DATE,
    t.c.S_INFO_STOCKWINDCODE, # 持有股票
    t.c.F_PRT_STKVALUE, # 持股市值

        ]

sql = select(columns).where(t.c.S_INFO_WINDCODE.in_(secode))

df = pd.read_sql(sql,db)

fundCode = df.copy().drop_duplicates('S_INFO_WINDCODE', keep = 'first').S_INFO_WINDCODE

fundStock = pd.DataFrame(columns = ['S_INFO_WINDCODE','ANN_DATE','S_INFO_STOCKWINDCODE','F_PRT_STKVALUE'])

for fund in fundCode:
    funddf = df[df.S_INFO_WINDCODE == fund]
    funddf.sort_values('ANN_DATE', ascending = False, inplace = True)
    date = funddf['ANN_DATE'].iloc[0]
    funddf = funddf[funddf['ANN_DATE'] == date]

    funddf.sort_values('F_PRT_STKVALUE', ascending = False, inplace = True)

    if len(funddf) < 10:
        fundStock = pd.concat([fundStock,funddf], axis = 0)
    else:
        funddata = funddf.head(10)
        fundStock = pd.concat([fundStock,funddata], axis = 0)



# beijing code
db = batch.connection('wind_db')
metadata = MetaData(bind = db)
t = Table('ashareintroduction',metadata, autoload = True)

columns = [
    t.c.S_INFO_WINDCODE,
        ]

sql = select(columns).where(t.c.S_INFO_CITY == '北京市')

beijingCode = pd.read_sql(sql, db)

beijingCode = list(beijingCode.S_INFO_WINDCODE)

# 对于每个基金，计算北京的占比，计算北京的总市值占比

bdf = fundStock[fundStock.S_INFO_STOCKWINDCODE.isin(beijingCode)]

allnum = len(fundStock)
print(allnum)
bjnum = len(bdf)
print(bjnum)
bjnumR = bjnum / allnum
print(bjnumR)
allvalue = fundStock.F_PRT_STKVALUE.sum()
print(allvalue)
bjvalue = bdf.F_PRT_STKVALUE.sum()
print(bjvalue)
bjvalueR = bjvalue / allvalue
print(bjvalueR)


