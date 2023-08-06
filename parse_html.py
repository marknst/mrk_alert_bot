import requests
from user_agents import random_user_agent

def parse_html(url: str):
    response = requests.get(url, headers={'User-Agent': random_user_agent()})

    if response.status_code == 200:
        html_content = response.text
        return html_content
    else:
        print("Failed to fetch the webpage: ", response.status_code)
        html_content = None