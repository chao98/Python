import requests
from bs4 import BeautifulSoup
from collections import deque


def downhtml(url, params):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3
    r = requests.get(url, params=params, headers=headers, timeout=timeout)
    if r.status_code == requests.codes.ok:
        #print('OK', url)
        return r.text
    else:
        #print('NOK, exit')
        return


def parsehtml(html):
    '''
    :param html:
    :return: stock list on this html page, and also if next page exist
    '''

    stock_list = []

    return stock_list, True


def get_stock_list(url):
    '''
    1) Compose first complete url
    2) Download html, and find nex url
    3) Loop to get html and next url, until next url is None
    4) Return stock_list
    '''

    page, max_show, sort, order = '1', '80', '2', '1'
    params = {'mod': ['all', 'list'], 'id': 'ssa', 'module': 'SS',
              'type': 'ranka', 'sort': sort, 'page': page,
              'max': max_show, 'order': order}
    stock_list = []
    failed_page = []
    next_page_exist = False

    if url is not None:
        stk_lst, next_page_exist = parsehtml(downhtml(url, params))
        if len(stk_lst) != 0:
            print('Page [%s] OK' % page)
        pass


def main():
    url1 = r'http://stockapp.finance.qq.com/mstats/'
    stock_list = get_stock_list(url1)
    return


if __name__ == '__main__':
    main()
