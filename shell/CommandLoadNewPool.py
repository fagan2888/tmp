
# load data of PO.000070

import numpy as np
import pandas as pd
from sqlalchemy import *
from sqlhelper import batch
from config import *
import os
import csv
from ipdb import set_trace

def read():
    df = pd.DataFrame(columns = ['ra_date','ra_fund_code','ra_fund_ratio'])
    filenames = os.listdir('PO.000070allocate/')
    errorfilename = list()
    for filename in filenames: 
        dfTmp = pd.read_table("PO.000070allocate/"+filename, header = None, sep = '\s+')
        
#        with open('PO.000070allocate/'+filename[0:len(filename)-4]+'.csv', 'w+') as csvfile:
#            writer = csv.writer(csvfile, dialect = 'excel')
#            with open('PO.000070allocate/'+filename, 'r', encoding = 'utf-8') as filein:
#                for line in filein:
#                    line_list = line.strip('\n').split('\t')
#                    writer.writerow(line_list)
#        dfTmp = pd.read_csv('PO.000070allocate/'+filename[0:len(filename)-4]+'.csv', header = None)
#
        dfTmp.columns = ['type','ra_fund_code','ra_fund_ratio']
        dfTmp.ra_fund_code = dfTmp.ra_fund_code.apply(lambda x: x[0:6])
        # find ra_fund_id
        db = create_engine(uris['base'])
        meta = MetaData(bind = db)
        t = Table('ra_fund', meta, autoload =True)
        columns = [
            t.c.ra_code.label('ra_fund_code'),
            t.c.globalid.label('ra_fund_id'),
            ]
        sql = select(columns).where(t.c.ra_code.in_(list(dfTmp.ra_fund_code)))
        mofangIds = pd.read_sql(sql, db)
        dfTmp['ra_date'] = filename[-12:-4]
        dfTmp.drop('type', axis = 1, inplace = True)
        dfTmp = pd.merge(dfTmp, mofangIds ,on = 'ra_fund_code', how = 'left')
        # find ra_pool_id
        dfTmp['ra_pool_id'] = dfTmp['ra_fund_code']
        dfTmp.drop_duplicates('ra_fund_code', inplace = True, keep = 'first')
        #print(dfTmp)
        #set_trace()
        sumup = dfTmp['ra_fund_ratio'].sum()
        if sumup < 1.0:
            errorfilename.append(filename)
        df = pd.concat([df, dfTmp], axis = 0)
    
    print(errorfilename)
    with open('errorfilename.txt', 'w+') as f:
        for name in errorfilename:
            f.write(name+'\n')

    set_trace()
    
    df.ra_date = df.ra_date.apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    df['ra_portfolio_id'] = 'PO.000070'
    df = df.fillna(0)
    df['ra_fund_id'] = df['ra_fund_id'].map(lambda x: int(x))
    df.set_index(['ra_pool_id','ra_date','ra_fund_id'], inplace = True)

    return df


def pos(df, sdate = '2019-12-12', edate = '2019-12-17'):

    # connect to asset 
    db = create_engine(uris['asset'])
    meta = MetaData(bind = db)
    t = Table('ra_portfolio_pos', meta, autoload = True)
    columns = [
            t.c.ra_portfolio_id,
            t.c.ra_date,
            t.c.ra_pool_id,
            t.c.ra_fund_id,
            t.c.ra_fund_code,
            #t.c.ra_fund_type,
            t.c.ra_fund_ratio,
            ]
    sql = select(columns)
    sql = sql.where(t.c.ra_portfolio_id == 'PO.000070')
    sql = sql.where(t.c.ra_date >= sdate).where(t.c.ra_date < edate)
    dfBase = pd.read_sql(sql, db)
    dfBase['ra_date'] = dfBase['ra_date'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    dfBase.set_index(['ra_pool_id','ra_date','ra_fund_id'], inplace = True)

    # update
    batch.batch(db, t, df, dfBase)

if __name__ == '__main__':
    df = read()
    print(df)
    set_trace()
    pos(df)
