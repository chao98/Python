import pprint
import os
import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

pp = pprint.PrettyPrinter(indent=2)


def create_pd(n):
    if n == 1:
        d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
             'two': pd.Series([4., 5., 6., 7.], index=['a', 'b', 'c', 'd'])}
        df = pd.DataFrame(d)
        df.index.name = 'index'
        # pp.pprint(d)
        print('Index: ', end='')
        pp.pprint(df.index)
        print('Column: ', end='')
        pp.pprint(df.columns)
        pp.pprint(df)
        print(pd.Series.idxmin(df.one))
        print(pd.Series.idxmax(df.one))
        # pp.pprint(df.tail(2))
        # pp.pprint(df.to_dict(outtype='list'))
        # pp.pprint(df.one)
        # pp.pprint(df['two'])
        # pp.pprint(list(df.one))
        # pp.pprint(df['a':'b'])
        # pp.pprint(df[0:1])
        # pp.pprint(df.loc[:,'one'])
        # pp.pprint(df.loc['a'])
        # pp.pprint(list(df.loc['a']))
        # pp.pprint(df.iloc[0])
        # pp.pprint(list(df.iloc[0]))
        # pp.pprint(df.iloc[1, 1])
        # pp.pprint(df.iloc[[0, 1, 2], :])
        # pp.pprint(df.ix[0:3])
        # pp.pprint(df.ix[:, 1])
        # pp.pprint(df[(df.one >= 2) & (df.two >= 6)])

    if n == 2:
        d = [{'one': 1, 'two': 1},
             {'one': 2, 'two': 2},
             {'one': 3, 'two': 3},
             {'two': 4}]
        df = pd.DataFrame(d, index=['a', 'b', 'c', 'd'], columns=['one', 'two'])
        df.index.name = 'index'
        pp.pprint(d)
        pp.pprint(df)

    if n == 3:
        pdfile = 'today_all.txt'
        if os.path.exists(pdfile):
            ctime = os.path.getmtime(pdfile)
            print(datetime.fromtimestamp(ctime))
            if datetime.now() - datetime.fromtimestamp(ctime) <= timedelta(days=1) :
                df = pd.read_csv(pdfile, dtype={'code': str}, encoding='gbk')
                print(df.columns)
                print(df.iloc[:, [1, 2, 4]])


def main():
    create_pd(3)


if __name__ == '__main__':
    main()

