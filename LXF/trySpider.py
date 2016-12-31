from __future__ import print_function
import urllib2
import sys
import os
import time
import random
from socket import error as socket_err

def spider(stockid):
    savedir = './examdir/'
    baseurl = 'http://stock.finance.qq.com/corp1/stk_holder_count.php?zqdm='
    #baseurl = 'http://www.yidiancangwei.com/shareholders.php?ID='
    queryurl = baseurl + stockid

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }

    req = urllib2.Request(url=queryurl, headers=headers)

    if stockid[0] in '03':
        stockid = 'sz' + stockid
    elif stockid[0] in '6':
        stockid = 'sh' + stockid

    outfilename = savedir + stockid + '.htm'
    with open(outfilename, 'w') as f:
        s = urllib2.urlopen(req).read()
        f.write(s)

def chkdir(outdir):
    filenames = os.listdir(outdir)
    savedfiles = []

    for filename in filenames:
        if 'sz' in filename or 'sh' in filename:
            savedfiles.append(filename[2:8])

    return savedfiles

def rand(m):
    while 1:
        r = random.random()
        r = r * 10
        if r <= m:
            break

    return r

def main():
    if len(sys.argv) != 3:
        print('Err: lack of filenames!')
        print('Usage: python trySpider.py infile outfile')
        exit(1)

    infile = sys.argv[1]
    outdir = sys.argv[2]

    savedfilelist = chkdir(outdir)
    count = 0

    with open(infile) as f:
        for l in f:
            params = l.split()
            if len(params) > 0:
                idstr = params[0]
            if idstr.isdigit() is True and idstr not in savedfilelist:
                count = count + 1
                time.sleep(rand(2))
                try:
                    spider(idstr)
                    print('.', end='')
                    if count == 70:
                        count = 0
                        print()
                    sys.stdout.flush()
                except socket_err:
                    print('\nCatch socket err')
                    print('sleep 5s, then continue.')
                    continue

if __name__ == '__main__':
    main()
