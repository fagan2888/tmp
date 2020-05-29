
import pandas as pd
import numpy as np
from sqlalchemy import *
from ipdb import set_trace
from config import *
from db import database

def r():
    
    sdate = '2014-12-17'
    edate = '2019-12-17'

#    db = create_engine(uris['asset'])
#    meta = MetaData(bind = db)
#    t = Table('on_online_nav', meta, autoload = True)
#    columns = [
#        t.c.on_online_id.label('ID'),
#        t.c.on_date.label('日期'),
#        t.c.on_nav.label('单位净值'),
#    ]
#    sql = select(columns)
#    sql = sql.where(t.c.on_date <= edate).where(t.c.on_date >= sdate).where(t.c.on_type == 8)
# 
#    db = create_engine(uris['wind_db'])
#    meta = MetaData(bind = db)
#    t = Table('chinamutualfundnav', meta, autoload = True)
#    columns = [
#        t.c.F_INFO_WINDCODE.label('ID'),
#        t.c.PRICE_DATE.label('日期'),
#        t.c.F_NAV_UNIT.label('单位净值'),
#    ]
#    sql = select(columns)
#    sql = sql.where(t.c.PRICE_DATE <= edate).where(t.c.PRICE_DATE >= sdate).where(t.c.F_INFO_WINDCODE == '110003.OF')

    db = create_engine(uris['asset'])
    meta = MetaData(bind = db)
    t = Table('ra_composite_asset_nav', meta, autoload = True)
    columns = [
        t.c.ra_asset_id.label('ID'),
        t.c.ra_date.label('日期'),
        t.c.ra_nav.label('单位净值'),
        t.c.ra_inc.label('日涨跌'),
    ]
    sql = select(columns)
    sql = sql.where(t.c.ra_date <= edate).where(t.c.ra_date >= sdate)

    excel = pd.ExcelWriter('标杆表现.xlsx')
    for i in range(1,9):
        sqlTmp = sql.where(t.c.ra_asset_id == 20200+i)
        name = str(100-11*i)+'%中证全债+'+str(11*i)+ '%上证指数'
        df = pd.read_sql(sqlTmp,db)
        df.sort_values(by = '日期', ascending = True, inplace = True)
        df.reset_index(inplace = True, drop = True)
        df.to_excel(excel, sheet_name = name)
    
    sdate = '20141217'
    edate = '20191217'
    db = create_engine(uris['wind_db'])
    meta = MetaData(bind = db)
    t = Table('aindexeodprices', meta, autoload = True)
    columns = [
        t.c.S_INFO_WINDCODE.label('ID'),
        t.c.TRADE_DT.label('日期'),
        t.c.S_DQ_CLOSE.label('收盘点位'),
        t.c.S_DQ_PCTCHANGE.label('日涨跌'),
    ]
    sql = select(columns)
    sql = sql.where(t.c.TRADE_DT <= edate).where(t.c.TRADE_DT >= sdate)
    sql1 = sql.where(t.c.S_INFO_WINDCODE == '000001.SH')
    sql2 = sql.where(t.c.S_INFO_WINDCODE == 'h11006.CSI')
    
    df1 = pd.read_sql(sql1, db)
    df1['日期'] = df1['日期'].map(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    df1.sort_values(by = '日期', ascending = True, inplace = True)
    df1.reset_index(inplace = True, drop = True)
    df1.to_excel(excel, sheet_name = '上证综指')

    df2 = pd.read_sql(sql2, db)
    df2['日期'] = df2['日期'].map(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    df2.sort_values(by = '日期', ascending = True, inplace = True)
    df2.reset_index(inplace = True, drop = True)
    df2.to_excel(excel, sheet_name = '中证国债')

    excel.save()

#    df = pd.read_sql(sql, db)
#    df['名称'] = '易方达上证50指数A'
#    money = 16666.66
#    df['总钱数'] = df['单位净值']*(money/df['单位净值'][0])
#    df.sort_values(by = '日期', ascending = True, inplace = True)
#    df.reset_index(inplace = True, drop = True)
    
#    for j in range (1,len(df)//30):
#        df1 = df.ix[df.index >= j*30]
#        df2 = df.ix[df.index < j*30]
##        for k in range(j*30,len(df)):
##            df['总钱数'][k] = df['总钱数'][k]+ money*df['单位净值'][k]/df['单位净值'][j*30]
#        df1['总钱数'] = df1['总钱数'] + money/df1['单位净值'][j*30]*df1['单位净值']
#        df = pd.concat([df2,df1],axis = 0)
#
##    df['收益率'] = 0
##    df['不定投收益率'] = 0
#
##    for k in range (1,len(df)):
##        df['收益率'][k] = df['总钱数'][k]/df['总钱数'][0] - 1 
##        df['不定投收益率'][k] = df['单位净值'][k]/df['单位净值'][0] - 1
#
#    print(df)
#    set_trace()
#    df.to_excel('易方达上证50指数A定投16666.66.xlsx')
    

if __name__ == '__main__':
    r()
