import sys
import os
import getopt
import json
import tushare as ts
import pandas as pd
from datetime import datetime, timedelta

DATEFMT = '%Y-%m-%d'


def get_stock_list(params):
    pdfile = 'today_all.txt'
    if os.path.exists(pdfile):
        ctime = os.path.getmtime(pdfile)
        if datetime.now() - datetime.fromtimestamp(ctime) <= timedelta(days=1):
            df = pd.read_csv(pdfile, dtype={'code':str}, encoding='gbk')
    else:
        df = ts.get_today_all()
        df.to_csv(pdfile)
    # print('\nColumns: ', df.columns)
    lprice, hprice = params['lprice'], params['hprice']
    lmktcap, hmktcap = params['lmktcap'], params['hmktcap']
    newdf = df.loc[(df.trade >= lprice) &
                   (df.trade <= hprice) &
                   (df.mktcap >= lmktcap) &
                   (df.mktcap <= hmktcap) &
                   (df.open != 0)]
    return list(newdf.code)


def get_single_peak_data(code, params):
    start, end, incr = params['start'], params['end'], params['incr']
    lratio, hratio = params['lratio'], params['hratio']
    df = ts.get_h_data(code, start, end)
    # print(list(zip(df.index, df.close)))
    lidx, hidx = pd.Series.idxmin(df.close), pd.Series.idxmax(df.close)
    low, high = df.loc[lidx, 'close'], df.loc[hidx, 'close']
    # print(type(lidx), lidx < hidx)
    # print(hidx < datetime.now())
    lidxd = lidx.strftime(DATEFMT)
    hidxd = hidx.strftime(DATEFMT)
    # print('\t{}: {} -> {}, {} -> {}'.format(code, lidxd, low, hidxd, high))
    if incr and lidx < hidx and (high - low) / low >= lratio:
        print('\t{}: {} -> {}, {} -> {}'.format(code, lidxd, low, hidxd, high))
        return code, (lidxd, low), (hidxd, high)
    elif not incr and hidx < lidx and (high - low) / low >= lratio:
        return code, (hidxd, high), (lidxd, low)


def get_peak_data(stock_list, params):
    result = []
    for code in stock_list:
        try:
            single = get_single_peak_data(code, params)
            if single:
                result.append(single)
        except AttributeError:
            print('AttributeError {}'.format(code))
        except json.decoder.JSONDecodeError:
            print('JSONDecodeError {}'.format(code))
    return result


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'r:s:e:', ['ratio=', 'start=', 'end='])
    except getopt.GetoptError:
        print('python getpeakdata.py -s startdate -e enddate -r ratio')
        exit(2)

    ratio, start, end = 0.5, None, None

    for opt, arg in opts:
        if opt in ['-r', '--ratio']:
            ratio = arg
        elif opt in ['-s', '--start']:
            start = arg
            if not end:
                end = datetime.now().strftime(DATEFMT)
        elif opt in ['-e', '--end']:
            end = arg
            if not start:
                delta = timedelta(days=90)
                start = (datetime.strptime(end, DATEFMT) - delta).strftime(DATEFMT)
        else:
            print('python getpeakdata.py -s startdate -e enddate -r ratio')
            exit(2)

    if not end:
        end = datetime.now().strftime(DATEFMT)
        start = (datetime.now() - timedelta(days=90)).strftime(DATEFMT)

    # print(code, start, end)
    params = {'lprice': 0, 'hprice': 10,
              'start': start, 'end': end,
              'lratio': ratio, 'hratio': float('inf'),
              'lmktcap': 0, 'hmktcap': 10**15,
              'incr': True}

    stock_list = get_stock_list(params)
    print('\ntotal stock (%d<price<%d): %4d' % (params['lprice'], params['hprice'], len(stock_list)))
    print(get_peak_data(stock_list, params))

if __name__ == '__main__':
    main(sys.argv[1:])