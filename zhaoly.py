import string
import os
import sys
sys.path.append('shell')
import click
import pandas as pd
import numpy as np
import os
import time
import logging
import re
import util_numpy as npu
import MySQLdb
import config
from ipdb import set_trace


from datetime import datetime, timedelta
from dateutil.parser import parse
from Const import datapath
from sqlalchemy import MetaData, Table, select, func, literal_column
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from tabulate import tabulate
from db import database, base_exchange_rate_index, base_ra_index, asset_ra_pool_fund, base_ra_fund, asset_ra_pool, asset_on_online_nav, asset_ra_portfolio_nav, asset_on_online_fund, asset_mz_markowitz_nav, base_ra_index_nav, asset_ra_composite_asset_nav, base_exchange_rate_index_nav, base_ra_fund_nav, asset_mz_highlow_pos, asset_ra_pool_nav, asset_ra_portfolio_pos, asset_allocate
from util import xdict
from trade_date import ATradeDate
from asset import Asset
from monetary_fund_filter import MonetaryFundFilter

import pymysql
import pandas as pd
from ipdb import set_trace
from dateutil.parser import parse
from datetime import timedelta

import criteria_ct

import traceback, code


def allocate_benchmark_comp():

    index_ids = ['120000016', '120000010']
    data = {}
    for _id in index_ids:
        data[_id] = base_ra_index_nav.load_series(_id)
    df = pd.DataFrame(data)

    composite_asset_ids = ['20201','20202', '20203', '20204', '20205', '20206', '20207', '20208']

    data = {}

    for _id in composite_asset_ids:
        nav = asset_ra_composite_asset_nav.load_nav(_id)
        nav = nav.reset_index()
        nav = nav[['ra_date', 'ra_nav']]
        nav = nav.set_index(['ra_date'])
        data[_id] = nav.ra_nav

    bench_df = pd.DataFrame(data)
    benchmark_df = pd.concat([bench_df,df],axis = 1, join_axes = [bench_df.index])

    conn  = MySQLdb.connect(**config.db_asset)
    conn.autocommit(True)

    dfs = []
    for i in range(0, 10):
        sql = 'select on_date as date, on_nav as nav from on_online_nav where on_online_id = 80000%d and on_type = 8' % i
        df = pd.read_sql(sql, conn, index_col = ['date'], parse_dates = ['date'])
        df.columns = ['risk_' + str(i)]
        dfs.append(df)

    df = pd.concat(dfs, axis = 1)

    conn.close()

    df = pd.concat([df, benchmark_df], axis = 1, join_axes = [df.index])
    df = df.fillna(method='pad')
    df = df.rename(columns = {'risk_0':'风险10','risk_1':'风险1','risk_2':'风险2','risk_3':'风险3','risk_4':'风险4','risk_5':'风险5',
                            'risk_6':'风险6','risk_7':'风险7','risk_8':'风险8','risk_9':'风险9',
                            '20201':'风险2比较基准','20202':'风险3比较基准', '20203':'风险4比较基准', '20204':'风险5比较基准', 
                            '20205':'风险6比较基准', '20206':'风险7比较基准', '20207':'风险8比较基准', '20208':'风险9比较基准',
                            '120000016':'风险10比较基准','120000010':'风险1比较基准'})
    cols = ['风险1', '风险2', '风险3', '风险4', '风险5', '风险6', '风险7', '风险8', '风险9', '风险10','风险1比较基准','风险2比较基准', '风险3比较基准', '风险4比较基准', '风险5比较基准', '风险6比较基准', '风险7比较基准', '风险8比较基准', '风险9比较基准', '风险10比较基准']
    df = df[cols]


    result_df = pd.DataFrame(columns = df.columns)
    last_day = df.index[-1]
    print(last_day)
    first_day =df.index[0]
    print(first_day)
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 当日'] = df.pct_change().iloc[-1]
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一周'] = df.loc[last_day] / df.loc[last_day - timedelta(weeks = 1)] - 1
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 31)] - 1
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去三个月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 91)] - 1
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去六个月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 182)] - 1
    #result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一年'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 365)] - 1
    
# 非滚动战胜概率     
    length = len(df)//7
#    length = len(df)//31
#    length = len(df)//91
#    length = len(df)//182
#    length = len(df)//365
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    k7 = 0
    k8 = 0
    k9 = 0
    k10 = 0
    days = df.index.values
    for i in range(length):
        num = -1 - i*7
#        num = -1 - i*31
#        num = -1 - i*91
#        num = -1 - i*182
#        num = -1 - i*365
        last_day = pd.to_datetime(str(days[num]))
        result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一周'] = df.loc[last_day] / df.loc[last_day - timedelta(weeks = 1)] - 1
 #       result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 31)] - 1
 #       result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去三个月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 91)] - 1
 #       result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去六个月'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 182)] - 1
 #       result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一年'] = df.loc[last_day] / df.loc[last_day - timedelta(days = 365)] - 1
        if result_df['风险1'][0]>result_df['风险1比较基准'][0]:
            k1 +=1
        if result_df['风险2'][0]>result_df['风险2比较基准'][0]:
            k2 +=1
        if result_df['风险3'][0]>result_df['风险3比较基准'][0]:
            k3 +=1
        if result_df['风险4'][0]>result_df['风险4比较基准'][0]:
            k4 +=1
        if result_df['风险5'][0]>result_df['风险5比较基准'][0]:
            k5 +=1
        if result_df['风险6'][0]>result_df['风险6比较基准'][0]:
            k6 +=1
        if result_df['风险7'][0]>result_df['风险7比较基准'][0]:
            k7 +=1
        if result_df['风险8'][0]>result_df['风险8比较基准'][0]:
            k8 +=1
        if result_df['风险9'][0]>result_df['风险9比较基准'][0]:
            k9 +=1
        if result_df['风险10'][0]>result_df['风险10比较基准'][0]:
            k10 +=1

# 滚动战胜概率
#    length = len(df)-7
#    length = len(df)//7
    length = len(df)//30
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0
    k5 = 0
    k6 = 0
    k7 = 0
    k8 = 0
    k9 = 0
    k10 = 0
    days = df.index.values
    for i in range(length):
#        num = -1 - i
#        num = -1 - i*7
#        num = -1 - i*30
        last_day = pd.to_datetime(str(days[num]))
        delta_day = last_day - timedelta(days = 31)
        choose_dates = df[df.index <= delta_day].index.values
        if len(choose_dates) == 0: 
            break
        delta_day = pd.to_datetime(str(choose_dates.max()))
#        result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一周'] = df.loc[last_day] / df.loc[delta_day] - 1
        result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去一月'] = df.loc[last_day] / df.loc[delta_day] - 1
#        result_df.loc[df.index[-1].strftime('%Y-%m-%d') + ' 过去三个月'] = df.loc[last_day] / df.loc[delta_day] - 1
        if result_df['风险1'][0]>result_df['风险1比较基准'][0]:
            k1 +=1
        if result_df['风险2'][0]>result_df['风险2比较基准'][0]:
            k2 +=1
        if result_df['风险3'][0]>result_df['风险3比较基准'][0]:
            k3 +=1
        if result_df['风险4'][0]>result_df['风险4比较基准'][0]:
            k4 +=1
        if result_df['风险5'][0]>result_df['风险5比较基准'][0]:
            k5 +=1
        if result_df['风险6'][0]>result_df['风险6比较基准'][0]:
            k6 +=1
        if result_df['风险7'][0]>result_df['风险7比较基准'][0]:
            k7 +=1
        if result_df['风险8'][0]>result_df['风险8比较基准'][0]:
            k8 +=1
        if result_df['风险9'][0]>result_df['风险9比较基准'][0]:
            k9 +=1
        if result_df['风险10'][0]>result_df['风险10比较基准'][0]:
            k10 +=1

        
    r1 = k1/length
    r2 = k2/length
    r3 = k3/length
    r4 = k4/length
    r5 = k5/length
    r6 = k6/length
    r7 = k7/length
    r8 = k8/length
    r9 = k9/length
    r10 = k10/length

    print([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10])

if __name__ == '__main__':

    allocate_benchmark_comp() 
