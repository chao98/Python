import requests
import pprint
from bs4 import BeautifulSoup


def simple_get(n):
    pp = pprint.PrettyPrinter(indent=2)

    if n == 1:
        url1 = r'http://xlzd.me'
        url2 = r'http://stock.finance.qq.com/corp1/stk_holder_count.php?zqdm=600518'
        url3 = r'http://movie.douban.com/top250'
        headers = {'User-Agent': 'my custom user agent', 'Cookie': 'haha'}
        timeout = 3
        r = requests.get(url2, headers=headers, timeout=timeout)
        print('Status: ', r.status_code)
        #print('encoding: ', r.encoding)
        pp.pprint(r.headers)
        #pp.pprint(r.text)

    if n == 2:
        url3 = r'http://movie.douban.com/top250'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
        r = requests.get(url3, headers=headers)
        print('Status: ', r.status_code)
        pp.pprint(r.headers)
        print(r.text)

    if n == 3:
        url2 = r'http://stock.finance.qq.com/corp1/stk_holder_count.php'
        params = {'zqdm': '600518'}
        headers = {'User-Agent': 'my custom user agent', 'Cookie': 'haha'}
        timeout = 3
        r = requests.get(url2, headers=headers, timeout=timeout, params=params)
        print('Status: ', r.status_code)
        print(r.headers)
        print(r.text)

    if n == 4:
        url3 = r'http://movie.douban.com/top250'
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
        r = requests.get(url3, headers=headers)

        soup = BeautifulSoup(r.text, 'html.parser')
        movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

        for movie_li in movie_list_soup.find_all('li'):
            detail = movie_li.find('div', attrs={'class': 'hd'})
            movie_name = detail.find('span', attrs={'class': 'title'}).getText()
            print(movie_name)


def main():
    simple_get(4)


if __name__ == '__main__':
    main()