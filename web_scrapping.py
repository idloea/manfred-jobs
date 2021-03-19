from bs4 import BeautifulSoup
import requests


def get_href_to_list(url):
    """
    Get all the href elements of a URL to a list
    :param url: URL of the website to extract the href elements
    :return: list of href elements
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    text_list = []
    href_list = []
    for element in soup.findAll('a'):
        text_list.append(element.contents[0])
        href_list.append(element['href'])
    return text_list, href_list


