from bs4 import BeautifulSoup
from parse_html import parse_html

url = 'https://announcements.bybit.com/en-us/?category=new_crypto&page=1'
html = parse_html(url=url)


def get_current_listing():
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find(
        class_="ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line article-item-title").find('span').text
    return result


if __name__ == '__main__':
    get_current_listing()
