import requests
from bs4 import BeautifulSoup

url_list = ["planqc.eu", "kipu-quantum.com"]

def get_site_text_content(url: str) -> str:
    """Given a url, get only the text content of this site"
    @param url: str. The root url we want to parse for text.
    @return str. Text content of the url
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def get_sitemap_urls(url: str) -> list[str]:
    """Get all urls from the sitemap.
    If the sitemap doesn't exist, just return the original URL.
    @param url: The root url from which we want to get all subpages
    @return list of subpages
    TODO: make this recursive!
    """

    sitemap_url = url + '/sitemap.xml'
    response = requests.get(sitemap_url)

    if response:
        soup = BeautifulSoup(response.text, features='xml')
        urls = [loc.text for loc in soup.find_all('loc')]

        return urls
    return [url]

def get_filepath_from_root_url(root_url: str, data_directory='./data/text_data/') -> str:
    """

    :param root_url:
    :param data_directory:
    :return:
    """
    # get rid of https://
    root_url = root_url.split('://')[1]
    filename = data_directory + root_url.replace('/', '_') + '.txt'

    return filename

def get_text_from_all_subpages(root_url: str) -> None:
    """

    :param root_url:
    :return:
    """

    urls = get_sitemap_urls(root_url)

    filename = get_filepath_from_root_url(root_url)

    with open(filename, 'w') as file:
        for url in urls:
            text_content = get_site_text_content(url)
            file.write(text_content)


def main():
    pass


if __name__ == '__main__':
    main()