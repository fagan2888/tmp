from sqlalchemy import MetaData, Table, select, func, and_
from sqlalchemy import Column, String, Integer, ForeignKey, Text, Date, DateTime, Float
import numpy as np
import pandas as pd
from sqlhelper import batch
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ipdb import set_trace


Base = declarative_base()

class ra_fund(Base):

    __tablename__ = 'ra_fund'

    globalid = Column(Integer, primary_key=True)
    ra_code = Column(String)
    ra_name = Column(String)
    ra_type = Column(Integer)
    ra_fund_type = Column(Integer)
    ra_mask = Column(Integer)

    updated_at = Column(DateTime)
    created_at = Column(DateTime)


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
