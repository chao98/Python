import requests
from bs4 import BeautifulSoup
import json


def downhtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3

    try:
        r = requests.get(url, headers=headers, timeout=timeout)
    # if r.status_code == requests.codes.ok:
    #     #print('OK', url)
    #     return r.text
    # else:
    #     #print('NOK, exit')
    #     return
    except requests.exceptions.RequestException:
        return

    return r.text


def parserhtml(html):
    if html is None:
        return

    qq_soup = BeautifulSoup(html, 'html.parser')
    pass


def get_stklst(fn):
    """
    :param fn:
    :return:
    Open a file, extract all stock ID, put them into a list and return it
    """

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
    base_url = r'http://stockpage.10jqka.com.cn/{}/holder/#holdernum'
    failed = []
    owners = {}
    counter = 0

    for stk in stk_list:
        url = base_url.format(stk)
        html = downhtml(url)
        if html is None:
            failed.append(stk)
            # print('Stock [%s] NOK' % stk)
        if counter % 70 == 0:
            print('\n[%4d]: ' % counter, end='')
        print('.', end='', flush=True)
        counter += 1
        # owners[stk] = parserhtml(html)
        print(html)

    # return owners, failed


def main():
    ifile = 'stk_list.txt'
    ofile = 'owners.txt'

    stk_list = get_stklst(ifile)
    extract_stk_list(stk_list)


if __name__ == '__main__':
    main()