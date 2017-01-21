import sys
import getopt
import tushare as ts
from datetime import datetime, timedelta

DATEFMT = '%Y-%m-%d'


def get_stock_list(price=10000):
    stock_list = []
    tmp = 'today_all.txt'
    df = ts.get_today_all()
    df.to_csv(tmp)
    with open(tmp) as f:
        for l in f:
            data = l.split(',')
            if len(data) >= 4 and str.isdigit(data[1]) and float(data[4]) < price:
                stock_list.append(data[1])
    return stock_list


def get_single_peak_data(code, start, end):
    pass


def get_peak_data(stock_list, start, end):
    if stock_list:
        print(get_single_peak_data(stock_list[0], start, end))


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'c:s:e:', ['code=', 'start=', 'end='])
    except getopt.GetoptError:
        print('python getpeakdata.py -s startdate -e enddate -c code')
        exit(2)

    code, start, end = None, None, None

    for opt, arg in opts:
        if opt in ['-c', '--code']:
            code = arg
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
            print('python getpeakdata.py -s startdate -e enddate -c code')
            exit(2)

    if not end:
        end = datetime.now().strftime(DATEFMT)
        start = (datetime.now() - timedelta(days=90)).strftime(DATEFMT)

    print(code, start, end)
    # price = 10
    stock_list = get_stock_list()
    print(len(stock_list))
    get_peak_data(stock_list, start, end)

if __name__ == '__main__':
    main(sys.argv[1:])