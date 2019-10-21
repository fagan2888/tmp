
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
 

db = batch.connection('asset')
metadata = MetaData(bind = db)
t = Table('ra_pool_fund',metadata, autoload = True)

columns = [
    t.c.ra_fund_code,
        ]

sql = select(columns)

code = pd.read_sql(sql, db) 

code = code.drop_duplicates(inplace = True)


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

print(secode)
set_trace()

db = batch.connection('wind_db')
metadata = MetaData(bind = db)
t = Table('chinamutualfundstockportfolio',metadata, autoload = True)

columns = [
    t.c.S_INFO_WINDCODE,
    t.c.ANN_DATE,
    t.c.S_INFO_STOCKWINDCODE,
    t.c.F_PRT_STKVALUETONAV,
        ]

sql = select(columns).where(t.c.S_INFO_WINDCODE.in_(secode))

df = pd.read_sql(sql,db)

df.to_excel('data.xlsx')
