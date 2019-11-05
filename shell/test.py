
# test database

import pandas as pd
from ipdb import set_trace

def test():
#    df1 = pd.read_csv('index_value.csv')
#    df2 = pd.read_csv('ra_portfolio_nav.csv')
#    index = df1.iloc[:,2]
#    time = df1.iloc[:,4]
#    value = df1.iloc[:,5]
#    df1 = pd.DataFrame(columns= ['沪深300','交易日期','沪深300净值'])
#    df1['沪深300'] = '000300.SH'
#    df1['交易日期'] = time
#    df1['沪深300净值'] = value
#    df1['交易日期'] = df1['交易日期'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
#    print(df1)
#    set_trace()
#    
#    index = df2.iloc[:,0]
#    time = df2.iloc[:,2]
#    value = df2.iloc[:,3]
#    df2 = pd.DataFrame(columns= ['稳稳的幸福','交易日期','稳稳的幸福净值'])
#    df2['稳稳的幸福'] = 'PO.QM0010'
#    df2['交易日期'] = time
#    df2['稳稳的幸福净值'] = value
#    df2['交易日期'] = df2['交易日期'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
#    print(df2)
#    set_trace()
#    
#    df1.set_index('交易日期',inplace = True)
#    df2.set_index('交易日期', inplace= True)
#    df = pd.merge(df1,df2,left_index = True, right_index = True)
#    print(df)
#    set_trace()
#    df.to_excel('沪深300+稳稳的幸福.xlsx')
#
    df = pd.read_excel('沪深300+稳稳的幸福.xlsx', index_col = 0)
    df['交易日期'] = list(df.index)
    df.reset_index(inplace = True, drop = True)
    df['交易日期'] = df['交易日期'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    print(df)
    set_trace()
    df3 = pd.read_csv('on_online_nav.csv')
    time = df3.iloc[:,2]
    value = df3.iloc[:,3]
    df3 = pd.DataFrame(columns= ['风险10','交易日期','风险10净值'])
    df3['风险10'] = '800009'
    df3['交易日期'] = time
    df3['风险10净值'] = value
    df3['交易日期'] = df3['交易日期'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
    print(df3)
    set_trace()

    df = df.set_index('交易日期')
    df3 = df3.set_index('交易日期')
    print(df)
    print(df3)
    df = pd.merge(df,df3,left_index = True, right_index = True)
    print(df)
    set_trace()
    df.to_excel('沪深300+稳稳的幸福.xlsx')

 

if __name__ == '__main__':
    test()
