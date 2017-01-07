import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import logging


def downhtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3

    # try:
    #     r = requests.get(url, headers=headers, timeout=timeout)
    # except requests.exceptions.RequestException:
    #     return

    r = requests.get(url, headers=headers, timeout=timeout)
    return r.text


def parserhtml(html):
    if html is None:
        return

    date, owner, aver = [], [], []
    jqka_soup = BeautifulSoup(html, 'html.parser')
    req_div = jqka_soup.find('div', attrs={'class': 'data_tbody'})
    top_table = req_div.find('table', attrs={'class': 'top_thead'})
    for div in top_table.find_all('div', attrs={'class': 'td_w'}):
        date.append(div.getText())

    tbody_table = req_div.find('table', attrs={'class': 'tbody'})
    for i, tr in enumerate(tbody_table.find_all('tr')):
        for td in tr.find_all('td'):
            if i == 0:
                owner.append(td.getText())
            elif i == 2:
                aver.append(td.getText())

    return list(zip(date, owner, aver, '-'*len(date), '-'*len(date)))


def get_stklst(fn):
    stk_lst = []
    with open(fn, 'r') as f:
        for line in f:
            if line in ['\n', '', None]:
                continue
            sid, *left = line.split()
            if sid is not None and sid.isdigit():
                stk_lst.append(sid)

    return stk_lst


def save_all_owner(ofile, owners):
    with open(ofile, 'w') as f:
        json.dump(owners, f, sort_keys=True, indent=2)


def chk_owners(file):
    with open(file, 'r') as f:
        owners = json.load(f)
        print(len(owners))


def extract_stk_list(stk_list):
    base_url = r'http://stockpage.10jqka.com.cn/{}/holder/#holdernum'
    failed = []
    owners = {}
    counter = 0
    start = datetime.now()

    for stk in stk_list:
        url = base_url.format(stk)
        try:
            html = downhtml(url)
            if counter % 60 == 0:
                delta = (datetime.now() - start).seconds
                print('\n[%6.1f | %4d]: ' % (delta, counter), end='')
            print('.', end='', flush=True)
            owners[stk] = parserhtml(html)
            counter += 1
        except requests.exceptions.RequestException:
            print('d[{}]'.format(stk), end='')
            failed.append(stk)
        except Exception as e:
            print('p[{}]'.format(stk), end='')
            # logging.exception(e)

    return owners, failed


def main():
    ifile = 'stk_list.txt'
    ofile = 'jqowners.txt'

    stk_list = get_stklst(ifile)
    owners = {}
    counter = 0
    while stk_list:
        owners_piece, stk_list = extract_stk_list(stk_list)
        owners.update(owners_piece)
        counter += 1
        print('\n>>> Will re-try with: ', stk_list)
        if counter >= 10:
            print('Tried too many time, exit!')
            break

    save_all_owner(ofile, owners)
    chk_owners(ofile)

if __name__ == '__main__':
    main()