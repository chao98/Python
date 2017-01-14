import sys
import getopt
import os
import tushare as ts
from datetime import datetime, timedelta


def get_dates(start, end):
    datefmt = '%Y-%m-%d'

    if end:
        startdate = datetime.strptime(start, datefmt)
        enddate = datetime.strptime(end, datefmt)
        date = []
        while enddate - startdate >= timedelta(days=0):
            weekday = startdate.strftime('%a')
            if weekday not in ['Sat', 'Sun']:
                date.append(startdate.strftime(datefmt))
            startdate += timedelta(days=1)
    else:
        return [start]

    print(date)
    return date


def get_tick(code, start, end=None, file=None):
    date = get_dates(start, end)
    for d in date:
        df = ts.get_tick_data(code, date=d)
        df.to_csv(file, mode='a')


def main(argv):
    try:
        opts, args = getopt.getopt(argv, 'hc:s:e:o:', ['code=', 'start=', 'end=', 'Ofile='])
    except getopt.GetoptError:
        print('python gettickdata -c code -s startdate -e enddate -o outfile')
        sys.exit(2)

    code, startdate, enddate, ofile = None, None, None, None

    for opt, arg in opts:
        if opt == '-h':
            print('python gettickdata -c code -s startdate -e enddate -o outfile')
            sys.exit()
        elif opt in ['-c', '--code']:
            code = arg
        elif opt in ['-s', '--start']:
            startdate = arg
        elif opt in ['-e', '--end']:
            enddate = arg
        elif opt in ['-o', '--Ofile']:
            ofile = arg
        else:
            print('python gettickdata -c code -s startdate -e enddate -o outfile')
            sys.exit()

    # print(code, startdate, enddate, ofile)
    get_tick(code, startdate, enddate, file=ofile)


if __name__ == '__main__':
    main(sys.argv[1:])