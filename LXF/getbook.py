import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime


def downhtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3
    r = requests.get(url, headers=headers, timeout=timeout)
    return r.text


def one_book(info):
    book = list()
    # name of the book
    book.append(info.find('a').string)
    # author, date, price
    book.append(info.find('div', attrs={'class', 'pub'}).getText())
    # rating
    book.append(info.find('span', attrs={'class', 'rating_nums'}).getText())
    # people
    people = info.find('span', attrs={'class', 'pl'}).getText().strip()
    # book.append(re.match(r'(\d+)', people).group(1))
    book.append(people)
    print(book)
    return book


def books(soup):
    detail = []
    # douban_soup = BeautifulSoup(html, 'html.parser')
    ul_div = soup.find('ul', attrs={'class', 'subject-list'})
    for info in ul_div.find_all('div', attrs={'class', 'info'}):
        try:
            detail.append(one_book(info))
        except AttributeError:
            print(info)
            break
    return detail


def extract_book(html, book_list):
    if html is None:
        return

    douban_soup = BeautifulSoup(html, 'html.parser')
    book_list.extend(books(douban_soup))
    print(book_list)
    # ul_div = douban_soup.find('ul', attrs={'class', 'subject-list'})
    # for info in ul_div.find_all('div', attrs={'class', 'info'}):
    #     print(info)
    #     print(info.find('a').string.strip())
    #     print(info.find('div', attrs={'class', 'pub'}).getText().strip())
    #     print(info.find('span', attrs={'class', 'rating_nums'}).getText())
    #     print(info.find('span', attrs={'class', 'pl'}).getText())
    #     break

    page_div = douban_soup.find('div', attrs={'class', 'paginator'})
    # print('\n>>> Page indicator: ')
    for url in page_div.find_all('a', href=True):
        # print('Found the URL: %s' % href['href'])
        try:
            html = downhtml(url)
        except requests.exceptions.RequestException:
            print('failed with %s' % url)
            exit(1)
        douban_soup = BeautifulSoup(html, 'html.parser')
        book_list.extend(books(douban_soup))
        print(book_list)
    return book_list


def main(keywords):
    html = r''
    base_url = r'https://book.douban.com/subject_search?search_text='
    url = base_url + keywords

    try:
        html = downhtml(url)
    except requests.exceptions.RequestException:
        print('failed with %s' % url)
        exit(1)

    book_list = []
    print(extract_book(html, book_list))


if __name__ == '__main__':
    keywords = r'python'
    main(keywords)