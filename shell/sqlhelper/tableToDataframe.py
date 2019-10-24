
# created by zhaoliyuan
# this function will help you to read data from database and turn it into dataframe

import pandas as pd
from sqlalchemy import *
from sqlalchemy.orm import sessinmaker
from sqlalchemy.ext.declarative import declarative_base
import sys
sys.path.append('../shell')
from config import uris

def main(key = 'base', cols, filters, dates = ''):
    
    # connect to database
    if key in uris.keys():
        uri = uris[key]
        engine = create_engine(uri)
    else:
        print('engine cannot be created! please check config.py')
        return -1

    # make sqls
    Session = sessionmaker(bind = engine)
    session = Session()
    sql = session.query(cols)
    
    # add filters

    sql = sql.statement

    if parse_dates:
        df = pd.read_sql(sql, session.bind, parse_dates = dates)
    else:
        df = pd,read_sql(sql, session.bind)


