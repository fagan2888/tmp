#coding=utf8

import os

rf = 0.025 / 52
annual_rf = 0.03


hs300_code               = '000300.SH' #沪深300
zz500_code               = '000905.SH' #中证500
largecap_code            = '399314.SZ' #巨潮大盘
smallcap_code            = '399316.SZ' #巨潮小盘
largecapgrowth_code      = '399372.SZ' #巨潮大盘成长
largecapvalue_code       = '399373.SZ' #巨潮大盘价值
smallcapgrowth_code      = '399376.SZ' #巨潮小盘成长
smallcapvalue_code       = '399377.SZ' #巨潮小盘价值


csibondindex_code         = 'H11001.CSI'  #中证全债指数
ratebondindex_code        = 'H11001.CSI'  #中证国债指数
credictbondindex_code     = 'H11073.CSI'  #中证信用债指数
convertiblebondindex_code = '000832.SH'   #中证可转债指数


sp500_code                = 'SP500.SPI'   #标普500指数
gold_code                 = 'GLNC'#黄金指数
hs_code                   = 'HSCI.HI'     #恒生指数

fund_num = 5

# 定义全局变量
version = '1.0'
verbose = False
datadir = "./tmp"


def datapath(filepath) :
    return os.path.join(datadir, filepath)
