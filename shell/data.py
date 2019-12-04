
import numpy as np
import pandas as pd
from sqlalchemy import *
from config import *
from ipdb  import set_trace

codes_dict = {
        '沪深300价值': '000919.CSI',
        '50AH优选1': '000170.SH',
        '50AH优选2': '950090.SH',
        '上证红利': '000015.SH',
        '中证银行(CSI)': '399986.CSI',
        '中证红利': '399922.SZ',
        '基本面50': '000925.CSI',
        '华安中证500低波动ETF联接A基准': '006129BI.WI',
        '华安中证500低波动ETF联接C基准': '006130BI.WI',
        '建信深证基本面60ETF基准': '159916BI.WI',
        '嘉实深证基本面120ETF基准': '159910BI.WI',
        '华宝标普中国A股红利机会C基准': '005125BI.WI',
        '华宝标普中国A股红利机会A基准': '501029BI.WI',
        '融通红利机会C基准': '005618BI.WI',
        '融通红利机会A基准':'005618BI.WI',
        '嘉实H股指数(QDII-LOF)基准': '160717BI.WI',
        '上证50': '000016.SH',
        '国泰中证申万证券行业基准': '501016BI.WI',
        '中证500': '399905.SZ',
        '上证养老': 'h50043.CSI',
        '医药100': '399978.SZ',
        '医药100':'000978.CSI',
        'MSCI香港中小盘': '661651.MI',
        '央视50': '399550.SZ',
        '上证180': '000010.SH',
        '可选消费指数': '882004.WI',
        '沪深300': '000300.SH',
        '深证100': '399330.SZ',
        '恒生指数': '',
        '深证成指': '399001.SZ',
        '中证消费1':'399932.SZ',
        '中证消费2': '000932.SH',
        '纳斯达克100': '',
        '标普500': '',
        '创业板指':'399006.SZ'
        }

codes = list(codes_dict.values())
names = list(codes_dict.keys())

def data():


    db = create_engine(uris['wind_db'])
    meta = MetaData(bind = db)
    t = Table('aindexvaluation', meta, autoload = True)
    columns = [
            t.c.S_INFO_WINDCODE,
            t.c.TRADE_DT,
           # t.c.PE_LYR,
            t.c.PE_TTM,
           # t.c.EST_PE_Y1,
           # t.c.EST_PE_Y2,
            ]
    sql = select(columns)
    sql = sql.where(t.c.S_INFO_WINDCODE.in_(codes))
    df = pd.read_sql(sql, db)
    df['NAME'] = df['S_INFO_WINDCODE'].apply(lambda x: list(codes_dict.keys())[list(codes_dict.values()).index(x)])
    df.sort_values(by = 'TRADE_DT', inplace = True, ascending = False)
    df.drop('S_INFO_WINDCODE', axis = 1, inplace = True)
    print(df)
    set_trace()
    df = df.set_index(['TRADE_DT', 'NAME']).unstack()['PE_TTM']
    df = df.dropna(how = 'any')
    print(df)
    set_trace()
    df.to_excel('data.xlsx')


if __name__ == '__main__':
    
    data()
