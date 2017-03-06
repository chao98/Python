import requests
import pprint
import re
from pandas import DataFrame
from bs4 import BeautifulSoup

pp = pprint.PrettyPrinter(indent=2)


def downhtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    timeout = 3
    r = requests.get(url, headers=headers, timeout=timeout)
    return r.text


def get_next_link(html):
    douban_soup = BeautifulSoup(html, 'html.parser')
    page_div = douban_soup.find('div', attrs={'class', 'paginator'})
    # urls=  [url['href'] for url in page_div.find_all('a', href=True)]
    # return urls[-1]
    next_div = page_div.find('span', attrs={'class', 'next'})
    url = next_div.find('a', href=True)
    return url['href'] if url else None


def get_html(url):
    try:
        return downhtml(url)
    except requests.exceptions.RequestException:
        print('failed with %s' % url)
        exit(1)


def get_one_book(info):
    title = info.find('a')['title']

    authors, date, price = '', '', ''
    book_misc = info.find('div', attrs={'class', 'pub'}).getText()
    if book_misc is not None:
        book_misc = book_misc.strip().split('/')
        if len(book_misc) >= 2:
            price = book_misc[-1].strip()
            date = book_misc[-2].strip()
            authors = '; '.join(map(str.strip, book_misc[:-2]))

    rate = info.find('span', attrs={'class', 'rating_nums'})
    rating = 0
    if rate is not None:
        rating = float(rate.getText())

    people_num = 0
    people = info.find('span', attrs={'class', 'pl'})
    if people is not None:
        people = people.getText().strip()
        if r'无人评价' in people or r'少于' in people:
            people_num = 0
        else:
            m = re.match(r'^\((\d+)\w+\)$', people)
            if m is not None:
                people_num = int(m.group(1))

    return [title, authors, date, price, rating, people_num]


def get_books_on_one_page(html):
    douban_soup = BeautifulSoup(html, 'html.parser')
    ul_div = douban_soup.find('ul', attrs={'class', 'subject-list'})
    books_on_one_page = list()
    for info in ul_div.find_all('div', attrs={'class', 'info'}):
        books_on_one_page.append(get_one_book(info))
    return books_on_one_page


def format_output(data, file='douban.txt', columns=None):
    if columns is None:
        columns = ['Title', 'authors', 'Date', 'Price', 'Rating', 'People']

    fmt = ':: '
    with open(file, 'w') as f:
        f.write(fmt.join(columns))
        f.write('\n')
        for d in data:
            f.write(fmt.join(map(str, d)))
            f.write('\n')


def main(keywords):
    base_url = r'https://book.douban.com'
    search_part = r'/subject_search?search_text='
    url = base_url + search_part + keywords
    # url = r'https://book.douban.com/subject_search?start=1200&search_text=python&cat=1001'

    whole_book_list = list()
    html = get_html(url)
    whole_book_list.extend(get_books_on_one_page(html))

    # nlink = get_next_link(html)
    # while nlink is not None:
    #     nlink = base_url + nlink
    #     # pp.pprint(nlink)
    #     html = get_html(nlink)
    #     whole_book_list.extend(get_books_on_one_page(html))
    #     nlink = get_next_link(html)

    pp.pprint(whole_book_list)
    # columns = ['Title', 'authors', 'Date', 'Price', 'Rating', 'People']
    # df = DataFrame(whole_book_list, columns=columns)
    # df.to_csv('douban1.txt')
    format_output(whole_book_list)

if __name__ == '__main__':
    keywords = r'python'
    main(keywords)