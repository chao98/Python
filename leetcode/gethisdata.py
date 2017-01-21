import os
import json
import tushare as ts
import pandas as pd
from datetime import datetime, timedelta

DATEFMT = '%Y-%m-%d'


def get_stock_list():
    pdfile = 'today_all.txt'
    if os.path.exists(pdfile):
        ctime = os.path.getmtime(pdfile)
        if datetime.now() - datetime.fromtimestamp(ctime) <= timedelta(days=1):
            df = pd.read_csv(pdfile, dtype={'code':str}, encoding='gbk')
    else:
        df = ts.get_today_all()
        df.to_csv(pdfile)
    return list(df.loc[df.open != 0].code)
    # return list(df.code)


def down_single(code, params):
    dir = 'hist'
    if not os.path.isdir(dir):
        os.mkdir(dir)
    ofile = '{}/{}.txt'.format(dir, code)
    if os.path.isfile(ofile):
        ctime = os.path.getmtime(ofile)
        if datetime.now() - datetime.fromtimestamp(ctime) <= timedelta(days=1):
            return
    start, end = params['start'], params['end']
    df = ts.get_k_data(code, start=start, end=end)
    df.to_csv(ofile)


def down_stock_his_data(stock_list, params):
    begin = datetime.now()
    width = 50
    for i, code in enumerate(stock_list):
        if i % width == 0:
            delta = (datetime.now() - begin).seconds
            print('\n[%7.1f|%4d] .' % (delta, i), end='', flush=True)
        else:
            print('.', end='', flush=True)

        try:
            down_single(code, params)
        except Exception as err:
            print('{}@{}'.format(err.args, code))
        # break


def main():
    today = datetime.now()
    delta = timedelta(days=365*3)
    start = (today - delta).strftime(DATEFMT)
    end = today.strftime(DATEFMT)
    params = {'start': start, 'end': end}
    stock_list = get_stock_list()
    print('Total down: {}'.format(len(stock_list)))
    down_stock_his_data(stock_list, params)

if __name__ == '__main__':
    main()