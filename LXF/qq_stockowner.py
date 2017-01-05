import requests
from bs4 import BeautifulSoup
import json


def downhtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3
    r = requests.get(url, headers=headers, timeout=timeout)
    if r.status_code == requests.codes.ok:
        #print('OK', url)
        return r.text
    else:
        #print('NOK, exit')
        return


def parserhtml(url):
    html = downhtml(url)
    if html is None:
        return

    qq_soup = BeautifulSoup(html, 'html.parser')
    req_table = qq_soup.find('table', attrs={'class': 'list list_d'})
    tr_list = req_table.find_all('tr')
    stock_owner_info = []

    for tr in tr_list:
        k = 'class'
        #print(tr.attrs)
        if k in tr.attrs and tr.attrs[k] == ['fntB']:
            pass
        else:
            owner_info =[]
            for td in tr.find_all('td'):
                owner_info.append(td.getText())
            stock_owner_info.append(owner_info)

    return stock_owner_info


def main():
    url1 = r'http://stock.finance.qq.com/corp1/stk_holder_count.php?zqdm=600518'
    data = parserhtml(url1)
    #print(len(data), data)
    print(json.dumps(data))

    url2 = r'http://stockapp.finance.qq.com/mstats/?mod=all#mod=list&id=ssa&module=SS&type=ranka&sort=2&page=1&max=40&order=1'


if __name__ == '__main__':
    main()
