#coding=utf8

db_asset = {
    "host": "rdsf4ji381o0nt6n2954.mysql.rds.aliyuncs.com",
    "port": 3306,
    "user": "jiaoyang",
    "passwd": "wgOdGq9SWruwATrVWGwi",
    "db":"asset_allocation",
    "charset": "utf8"
}

db_base = {
    "host": "rdsijnrreijnrre.mysql.rds.aliyuncs.com",
    "port": 3306,
    "user": "modelx",
    "passwd": "ca0bA3oG5JxCJIG23OUz3",
    "db":"mofang_api",
    "charset": "utf8"
}

db_wind = {
    "host": "rdsf4ji381o0nt6n2954.mysql.rds.aliyuncs.com",
    "port": 3306,
    "user": "jiaoyang",
    "passwd": "wgOdGq9SWruwATrVWGwi",
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

db_asset_uri = 'mysql://jiaoyang:wgOdGq9SWruwATrVWGwi@rdsf4ji381o0nt6n2954.mysql.rds.aliyuncs.com/asset_allocation?charset=utf8&use_unicode=1'
#db_base_uri =  'mysql://root:Mofang123@192.168.88.254/mofang?charset=utf8&use_unicode=1'
db_base_uri =  'mysql://jiaoyang:wgOdGq9SWruwATrVWGwi@rdsijnrreijnrre.mysql.rds.aliyuncs.com/mofang_api?charset=utf8&use_unicode=1'
#db_mapi_uri =  'mysql://root:Mofang123@localhost/mapi?charset=utf8&use_unicode=1'
db_caihui_uri =  'mysql://caihui:F4HfYeFXAyZM2Asa@192.168.88.254/caihui?charset=utf8&use_unicode=1'
#db_portfolio_sta_uri = 'mysql://root:Mofang123@localhost/portfolio_statistics?charset=utf8&use_unicode=1'
#db_wind_uri =  'mysql://finance:lk8sge9jcdhw@db_asset.licaimofang.com/lcmf_wind?charset=utf8&use_unicode=1'
db_wind_uri = 'mysql://jiaoyang:wgOdGq9SWruwATrVWGwi@rdsf4ji381o0nt6n2954.mysql.rds.aliyuncs.com/lcmf_wind?charset=utf8&use_unicode=1'
db_trade_uri = 'mysql://jiaoyang:wgOdGq9SWruwATrVWGwi@rm-bp15sb1c9t277l882rw.mysql.rds.aliyuncs.com/trade?charset=utf8&use_unicode=1'
db_mofang_wind_uri = 'mysql://root:Mofang123@192.168.88.254/mofang_wind?charset=utf8&use_unicode=1'
db_mofang_api_uri = 'mysql://wind:56pJn38L3Z4WQ8d8@rdsijnrreijnrre.mysql.rds.aliyuncs.com/mofang_api?charset=utf8&use_unicode=1'
db_wind_db_uri = 'mysql://public:h76zyeTfVqAehr5J@192.168.88.254/wind?charset=utf8&use_unicode=1'
db_wind_sync_uri = 'mysql://zhaoliyuan:zhaoliyuan20d@1101075@192.168.88.254/wind_sync_data?charset=utf8&use_unicode=1'
#db_prophet_uri = 'mysql://zhaoliyun:y+LjN98VPGSKayiiyFJ9WQ@rm-bp15sb1c9t277l882rw.mysql.rds.aliyuncs.com/prophet?charset=utf8&use_unicode=1'
db_prophet_uri = 'mysql://mapi:m0nmthUQfXBBOySdkRy3@kdb-master.mysql.rds.aliyuncs.com/prophet?charset=utf8&use_unicode=1'

uris = {
    'asset': db_asset_uri,
    'base': db_base_uri,
    'caihui': db_caihui_uri,
    'trade':db_trade_uri,
    #'portfolio_sta': db_portfolio_sta_uri,
    #'portfolio_sta': config.db_portfolio_sta_uri,
    #'mapi': db_mapi_uri,
    'wind': db_wind_uri,
    'mofang_wind': db_mofang_wind_uri,
    'mofang_api' : db_mofang_api_uri,
    'wind_db' : db_wind_db_uri,
    'wind_sync': db_wind_sync_uri,
    'prophet':db_prophet_uri,
}

