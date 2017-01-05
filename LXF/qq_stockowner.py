import requests
from bs4 import BeautifulSoup
import json


def downhtml(url, params):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3

    try:
        r = requests.get(url, params=params, headers=headers, timeout=timeout)
    # if r.status_code == requests.codes.ok:
    #     #print('OK', url)
    #     return r.text
    # else:
    #     #print('NOK, exit')
    #     return
    except requests.exceptions.RequestException:
        print(params.values())
        return

    return r.text


def parserhtml(html):
    if html is None:
        return

    qq_soup = BeautifulSoup(html, 'html.parser')
    req_table = qq_soup.find('table', attrs={'class': 'list list_d'})
    tr_list = req_table.find_all('tr')
    stock_owner_info = []

    for tr in tr_list:
        k = 'class'
        # print(tr.attrs)
        if k in tr.attrs and tr.attrs[k] == ['fntB']:
            pass
        else:
            owner_info = []
            for td in tr.find_all('td'):
                owner_info.append(td.getText())
            stock_owner_info.append(owner_info)

    return stock_owner_info


def get_stklst(fn):
    """
    :param fn:
    :return:
    Open a file, extract all stock ID, put them into a list and return it
    """

    stk_lst = []
    with open(fn, 'r') as f:
        for line in f:
            if line == '\n' or line is None or line == '':
                continue
            sid, *left = line.split()
            if sid is not None and sid.isdigit():
                stk_lst.append(sid)

    return stk_lst


def save_all_owner(ofile, owners):
    # print(len(owners))
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(owners)

    with open(ofile, 'w') as f:
        json.dump(owners, f, sort_keys=True, indent=2)


def chk_owners(file):
    with open(file, 'r') as f:
        owners = json.load(f)
        print(len(owners))

        # for k in sorted(owners):
        #     print(k, ' --> ', owners[k])


def extract_stk_list(stk_list):
    url = r'http://stock.finance.qq.com/corp1/stk_holder_count.php'
    params = {'zqdm': ''}
    failed = []
    owners = {}
    counter = 0

    for stk in stk_list:
        params['zqdm'] = stk
        html = downhtml(url, params)
        if html is None:
            failed.append(stk)
            # print('Stock [%s] NOK' % stk)
        if counter % 70 == 0:
            print('\n[%4d]: ' % counter, end='')
        print('.', end='', flush=True)
        counter += 1
        owners[stk] = parserhtml(html)

    return owners, failed


def main():
    ifile = 'stk_list.txt'
    ofile = 'owners.txt'

    stk_list = get_stklst(ifile)
    owners = {}
    counter = 0
    while stk_list != []:
        owners_piece, stk_list = extract_stk_list(stk_list)
        owners.update(owners_piece)
        counter += 1
        print('\n>>> Will re-try with: ', stk_list)
        if counter >= 10:
            print('Tried too many time, exit!')
            break

    save_all_owner(ofile, owners)
    chk_owners(ofile)
    # print('Failed with: ', stk_list)

if __name__ == '__main__':
    main()
