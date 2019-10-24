
# creared by zhaoliyuan

# help to read data from excel and do some adjustment

import pandas as pd
from datetime import *
from ipdb import set_trace

def defaultDate():
    day = date.today()
    day = day.strftime('%Y/%m/%d')
    return day


def do(filename, day, why):
    df = pd.read_excel(filename, sheet_name = 0)
    df = df[['基金池','操作','基金']].dropna(axis =0, how = 'any')
    df['基金池'] = df['基金池'].apply(lambda x: str(int(x)))
    df['基金'] = df['基金'].apply(lambda x: str(int(x)).zfill(6))
    df = df[df['操作']!='']
    df = df[df['基金']!='']
    dfNew = pd.DataFrame(columns = ['pool','date','op','code','why'])
    dfNew['pool'] = df['基金池']
    dfNew['date'] = day
    dfNew['op'] = df['操作']
    dfNew['code'] = df['基金']
    dfNew['why'] = why
    dfNew.set_index('pool', inplace = True)
    name = 'zhaoliyuan@patch-'+date.today().strftime('%Y-%m-%d')+'.csv'
    dfNew.to_csv(name) 


if __name__ == '__main__':
    day = defaultDate()
    name = '玄元基金池实盘__1022_新增.xlsx'
    why = '"'*3 + '定期更换基金池' + '"'*3
    do(filename = name, day = day, why = why)
