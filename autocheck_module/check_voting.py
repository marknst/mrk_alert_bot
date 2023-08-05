from bs4 import BeautifulSoup
from user_agents import random_user_agent
from parse_html import parse_html

url = "https://www.bitmart.com/voting/en-US"

html = parse_html(url=url)

def get_current_voting():

    soup = BeautifulSoup(html, 'html.parser')
    
    result = soup.find(
        class_="title d-flex flex-wrap align-items-center").find('span').text
    return result

if __name__ == '__main__':
    get_current_voting()