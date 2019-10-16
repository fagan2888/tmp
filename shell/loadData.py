# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:15:26 2019

@author: 赵利渊
"""
import numpy as np
import pandas as pd
from pymysql import connect
import sqlalchemy as sql
from util.xdebug import dd
from sqlhelper import batch
from time import strftime
from datetime import datetime,timedelta
from optparse import OptionParser
from ipdb import set_trace

class load:
    
    def __init__(self, suid, euid):
        self.suid=suid
        self.euid=euid
    
    def data(self):
        suid = self.suid
        euid = self.euid

        # 连接到现在的数据库
        db = batch.connection('prophet')
        metadata = sql.MetaData(bind=db)
        t = sql.Table('prophet_cash_cycle', metadata, autoload=True)
        columns = [
            t.c.cc_uid,
            t.c.cc_age,
            t.c.cc_investable_asset,
            t.c.cc_expenditure_asset,
            t.c.created_at,
        ]
        s = sql.select(columns)
        baseDf = pd.read_sql(s,db)
        baseDf.sort_values(by = ['created_at'], ascending = False, inplace = True)
        baseDf.drop_duplicates(subset = ['cc_uid','cc_age'],keep = 'first', inplace = True)
        baseDf.sort_values(by = ['cc_age'], ascending = True, inplace = True)
        
        # 每个用户求和
        #single.sort_values(by = ['cc_investable_asset'], ascending = True, inplace = True)

        # 找数据方便计算收入和开支的关系
        db = batch.connection('prophet')
        metadata = sql.MetaData(bind=db)
        t = sql.Table('prophet_cash_cycle', metadata, autoload=True)
        columns = [
            t.c.cc_uid,
            t.c.cc_age,
            t.c.cc_expenditure_asset,
            t.c.created_at,
        ]
        s = sql.select(columns)
        df1 = pd.read_sql(s,db)
        df1.sort_values(by = ['created_at'], ascending = False, inplace = True)
        df1.columns = ['uid','age','expenditure','created_at']
        df1.drop_duplicates(subset = ['uid','age'],keep = 'first', inplace = True)
        df1.drop('created_at', axis = 1,  inplace = True)
        df1.set_index(['uid', 'age'], inplace = True)
        
        db = batch.connection('prophet')
        metadata = sql.MetaData(bind=db)
        t = sql.Table('prophet_family_income_detail', metadata, autoload=True)
        columns = [
            t.c.fi_uid,
            t.c.fi_age,
            t.c.fi_income_asset,
            t.c.created_at,
        ]
        s = sql.select(columns)
        df2 = pd.read_sql(s,db)
        df2.sort_values(by = ['created_at'], ascending = False, inplace = True)
        df2.columns = ['uid','age','income','created_at']
        income = df2.copy().groupby(['uid','age'])['income'].sum()
        df2.drop('income', axis = 1, inplace = True)
        df2.drop_duplicates(subset = ['uid','age'],keep = 'first', inplace = True)
        df2.set_index(['uid', 'age'], inplace = True)
        df2['income'] = income
        df2.drop('created_at', axis = 1, inplace = True)
        
        df = pd.merge(df1, df2, left_index = True, right_index = True)
        
        print(baseDf)
        set_trace()
        print(df)
        set_trace()
        
        excel = pd.ExcelWriter('output.xlsx')
        baseDf.to_excel(excel,'年开支和年龄的关系')
        df.to_excel(excel, '年收入和年支出的关系')
        excel.save()        


if __name__ == '__main__':
    optParser = OptionParser(usage='usage: %prog [options]')
    startId = '0000000000'
    endId = '9999999999'
    optParser.add_option('-s', '--suid', help='start uid', dest='suid', type='string', default=startId)
    optParser.add_option('-e', '--euid', help='end uid', dest='euid', type='string', default=endId)
    options,args = optParser.parse_args()
    load = load(options.suid, options.euid)
    load.data()
