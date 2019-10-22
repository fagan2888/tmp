#coding=utf8

db_asset = {
    "host": "db_asset.licaimofang.com",
    "port": 3306,
    "user": "finance",
    "passwd": "lk8sge9jcdhw",
    "db":"asset_allocation",
    "charset": "utf8"
}

db_base = {
    "host": "192.168.88.254",
    "port": 3306,
    "user": "root",
    "passwd": "Mofang123",
    "db":"mofang",
    "charset": "utf8"
}

#db_caihui = {
#    "host": "rdsijnrreijnrre.mysql.rds.aliyuncs.com",
#    "port": 3306,
#    "user": "koudai",
#    "passwd": "Mofang123",
#    "db": "caihui",
#    "charset": "utf8"
#}
db_caihui = {
    "host": "db_caihui.licaimofang.com",
    "port": 3306,
    "user": "finance",
    "passwd": "lk8sge9jcdhw",
    "db": "caihui",
    "charset": "utf8"
}

db_wind = {
    "host": "db_asset.licaimofang.com",
    "port": 3306,
    "user": "finance",
    "passwd": "lk8sge9jcdhw",
    "db":"lcmf_wind",
    "charset": "utf8"
}


#db_portfolio_sta = {
#    "host": "127.0.0.1",
#    "port": 3306,
#    "user": "root",
#    "passwd": "Mofang123",
#    "db":"portfolio_statistics",
#    "charset": "utf8"
#}

db_asset_uri = 'mysql://finance:lk8sge9jcdhw@db_asset.licaimofang.com/asset_allocation?charset=utf8&use_unicode=1'
db_base_uri =  'mysql://zhaoliyuan:zhaoliyuan20d@1101075@192.168.88.254/mofang?charset=utf8&use_unicode=1'
#db_base_uri =  'mysql://root:Mofang123@192.168.88.254/mofang?charset=utf8&use_unicode=1'
#db_mapi_uri =  'mysql://root:Mofang123@localhost/mapi?charset=utf8&use_unicode=1'
db_caihui_uri =  'mysql://finance:lk8sge9jcdhw@db_caihui.licaimofang.com/caihui?charset=utf8&use_unicode=1'
#db_portfolio_sta_uri = 'mysql://root:Mofang123@localhost/portfolio_statistics?charset=utf8&use_unicode=1'
db_wind_uri =  'mysql://finance:lk8sge9jcdhw@db_asset.licaimofang.com/lcmf_wind?charset=utf8&use_unicode=1'
db_wind_db_uri = 'mysql://public:h76zyeTfVqAehr5J@192.168.88.11/wind?charset=utf8&use_unicode=1'
db_macro_factor_uri = 'mysql://finance:lk8sge9jcdhw@192.168.88.17/lcmf_wind?charset=utf8&use_unicode=1'
db_finance_uri = 'mysql://yangning:yangning20d@11024950@192.168.88.254/finance?charset=utf8&use_unicode=1'
#db_mofang_uri = 'mysql://zhaoliyuan:zhaoliyuan20d@1101075@192.168.88.254/mofang?charset=utf8&use_unicode=1'
#db_asset_allocation_uri = 'mysql://zhaoliyuan:zhaoliyuan20d@1101075@192.168.88.254/asset_allocation?charset=utf8&use_unicode=1'

uris = {
    'asset': db_asset_uri,
    'base': db_base_uri,
    'caihui': db_caihui_uri,
    #'portfolio_sta': db_portfolio_sta_uri,
    #'portfolio_sta': config.db_portfolio_sta_uri,
    #'mapi': db_mapi_uri,
    'wind': db_wind_uri,
    'wind_db': db_wind_db_uri,
    'macro_factor':db_macro_factor_uri,
    'finance':db_finance_uri,
    #'asset_allocation':db_asset_allocation_uri,
}

