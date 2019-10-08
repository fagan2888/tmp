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

class load:
    
    def __init__(self, suid, euid):
        self.suid=suid
        self.euid=euid
    
    def data(self):
        suid = self.suid
        euid = self.euid

        #连接到现在的数据库
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
        
#        baseDf.sort_values(by = ['cc_age'], ascending = True, inplace = True )
#        baseDf.drop_duplicates(subset = ['cc_uid'], keep = 'first', inplace = True)
        
        baseDf.to_csv('./data.csv')
        
        
if __name__ == '__main__':
    optParser = OptionParser(usage='usage: %prog [options]')
    startId = '0000000000'
    endId = '9999999999'
    optParser.add_option('-s', '--suid', help='start uid', dest='suid', type='string', default=startId)
    optParser.add_option('-e', '--euid', help='end uid', dest='euid', type='string', default=endId)
    options,args = optParser.parse_args()
    load = load(options.suid, options.euid)
    load.data()
