
from config import *
from sqlalchemy import *
import pandas as pd
from ipdb import set_trace

def online_portfolio():


    asset_name = {
            '11110100':'大盘',
            '11110106':'高盈利',
            '11110108':'高财务质量',
            '11110110':'食品饮料',
            '11110112':'医药生物',
            '11110114':'银行',
            '11110116':'非银金融',
            '11110200':'小盘',
            '11120200':'美股',
            '11120201':'美股',
            '11120500':'恒生',
            '11120501':'恒生',
            '11210100':'信用债',
            '11210200':'利率债',
            '11310100':'货币',
            '11310101':'货币',
            '11400100':'沪金',
            '11400300':'原油',
        }


    conn  = create_engine(uris['asset'])

    sql = 'select on_online_id, on_date, on_pool_id, on_fund_ratio from on_online_fund'

    excel = pd.ExcelWriter('10个风险的配置.xlsx')
    df = pd.read_sql(sql, conn, index_col = ['on_online_id', 'on_date', 'on_pool_id'])
    df = df.groupby(level = [0,1,2]).sum()
    df = df.unstack().fillna(0.0)
    df.columns = df.columns.droplevel(0)
    for k , v in df.groupby(df.index.get_level_values(0)):
        v.index = v.index.droplevel(0)
        #print(k)
        dates = pd.date_range(v.index[0], v.index[-1])
        v = v.reindex(dates).fillna(method = 'pad').fillna(0.0)
        v = v[v.index >= '2013-06-15']
        v = v.resample('M').last()
        v = v.rename(columns = asset_name)
        v = v.T
        v = v.groupby(level=[0]).sum()
        v = v.T
        #print(v['大盘']+ v['小盘'])
        #print(v.columns)
        #v[''] = ''
        v['A股'] = v['大盘'] + v['小盘'] 
        v['股基'] = v['大盘'] + v['小盘'] + v['美股'] + v['恒生']
        v['债基'] = v['信用债'] + v['利率债']
        #v['海外'] = v['美股'] + v['恒生'] + v['原油']
        v['国内'] = v['大盘'] + v['小盘'] + v['信用债'] + v['利率债'] + v['货币'] + v['沪金']
        print(v)
        set_trace()
        #v = v[v.index <= '2019-12-30']
        v.to_excel(excel, '风险等级' + str(k)[-1])
    excel.save()

if __name__ == '__main__':
    online_portfolio()
