import requests
from bs4 import BeautifulSoup

default_header = {'cookie': 'over18=1'}
def get_context(url: str, headers: dict[str,str] = {}):
    if len(headers) == 0:
        resp = requests.get(url, headers = default_header)
    else:
        resp = requests.get(url, headers = headers)

    soup = BeautifulSoup(resp.text, "html.parser")

    header = soup.find_all('span', 'article-meta-value')

    author, board = header[0].text, header[1].text

    title, date = header[2].text, header[3].text

    main_container = soup.find(id='main-container')

    all_text = main_container.text

    pre_text = all_text.split('--')[0]

    texts = pre_text.split('\n')

    contents = texts[2:]

    content = '\n'.join(contents)

    result = {
        'author':   author,
        'board':    board,
        'title':    title,
        'date':     date,
        'link':     url,
        'content': content
    }
    return result
