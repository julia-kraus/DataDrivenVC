import requests
from bs4 import BeautifulSoup

url_list = ["planqc.eu", "kipu-quantum.com"]

for url in url_list:
    print(url)
    html_text = requests.get('http://' + url).text

    soup = BeautifulSoup(html_text, 'html.parser')

    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    visible_text = soup.getText()

    file_name = url + '.txt'

    with open(file_name, 'w') as f:
        f.write(visible_text)
