import os
import json
import pandas as pd
from datetime import datetime, timedelta

DATEFMT = '%Y-%m-%d'


def check_single(f, params):
    df = pd.read_csv(f, dtype={'code': str}, encoding='gbk')
    start, end = params['start'], params['end']
    incr, ratio = params['incr'], params['lratio']
    code = df.loc[0, 'code']
    if df.loc[0, 'date'] >= start:
        return

    newdf = df[(df.date >= start) & (df.date <= end)]
    lidx, hidx = pd.Series.idxmin(newdf.close), pd.Series.idxmax(newdf.close)
    low, high = newdf.loc[lidx, 'close'], newdf.loc[hidx, 'close']
    ldate, hdate = newdf.loc[lidx, 'date'], newdf.loc[hidx, 'date']
    if incr and lidx < hidx and (high - low) / low >= ratio:
        return code, (ldate, low), (hdate, high)
    elif not incr and hidx < lidx and (high - low) / high >= ratio:
        return code, (hdate, high), (ldate, low)


def filter_stock(params):
    path = 'hist'
    r = []
    files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print('Total files = {}'.format(len(files)))

    begin = datetime.now()
    width = 60
    for i, f in enumerate(files):
        if i % width == 0:
            delta = (datetime.now() - begin).seconds
            print('\n[%4.1f|%4d] .' % (delta, i), end='', flush=True)
        else:
            print('.', end='', flush=True)

        single = check_single(f, params)
        if single:
            r.append(single)
    return r


def main():
    today = datetime.now()
    delta = timedelta(days=30*2)
    start = (today - delta).strftime(DATEFMT)
    end = today.strftime(DATEFMT)
    params = {'lprice': 0, 'hprice': 10000,
              'start': start, 'end': end,
              'lratio': 0.4, 'hratio': float('inf'),
              'lmktcap': 0, 'hmktcap': 10**10,
              'incr': True}

    result = filter_stock(params)
    ofile = '{}-{}.txt'.format(start, 'result')
    with open(ofile, 'w') as f:
        print('\nFound {} stocks fit for condition.'.format(len(result)))
        json.dump(result, f)

if __name__ == '__main__':
    main()