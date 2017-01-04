import requests
from bs4 import BeautifulSoup


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
    if url is None:
        return
    else:
        html = downhtml(url)
        if html is None:
            return
        else:
            mv_info_list = []
            mv_info_list.extend(findmv(html))
            next_url_piece = find_next(html)
            if next_url_piece is not None:
                next_url = url[0:30] + next_url_piece
                mv_info_list.extend(parserhtml(next_url))

    return mv_info_list


def findmv(html):
    douban_soup = BeautifulSoup(html, 'html.parser')
    mv_list = douban_soup.find('ol', attrs={'class': 'grid_view'})
    mv_info = []

    for mv in mv_list.find_all('li'):
        mv_detail = mv.find('div', attrs={'class': 'hd'})
        mv_name = mv_detail.find('span', attrs={'class': 'title'}).getText()
        mv_info.append(mv_name)

    return mv_info


def find_next(html):
    douban_soup = BeautifulSoup(html, 'html.parser')
    np = douban_soup.find('span', attrs={'class': 'next'}).find('a')
    if np:
        return np['href']

    return


def main():
    url = r'http://movie.douban.com/top250'
    mv_info = parserhtml(url)
    print(len(mv_info), mv_info)

if __name__ == '__main__':
    main()
