from src.main_julia import get_sitemap_urls, get_site_text_content, \
    get_text_from_all_subpages, get_filepath_from_root_url
import os
import pytest
url_list = ["planqc.eu", "kipu-quantum.com"]

@pytest.fixture
def plancq():
    return "https://planqc.eu"
def test_get_filepath_from_root_url(plancq):
    filename = get_filepath_from_root_url(plancq)
    assert filename == "./data/text_data/planqc.eu.txt"

def test_get_sitemap_urls_planqc(plancq):
    """There should be three sites in the sitemap"""
    urls = get_sitemap_urls(plancq)
    assert len(urls) == 3

    assert urls[0] == 'https://planqc.eu/'
    assert urls[1] == 'https://planqc.eu/imprint/'
    assert urls[2] == 'https://planqc.eu/privacy/'

def test_get_sitemap_urls_kipu_quantum():
    """There should be three sites in the sitemap. Problem here: sitemap is
    recursively another xml."""
    #TODO: Possible strategies to deal with recursive sitemaps
    # Just parse root page: add root page always to urls and then dedupe
    urls = get_sitemap_urls("https://kipu-quantum.com")
    assert len(urls) > 0
    assert len(urls) == 4


def test_get_site_text_content(plancq):
    """The function should output the text content of the given url"""
    text_content = get_site_text_content(plancq)
    assert text_content is not None
    assert type(text_content) == str
    assert len(text_content) > 0

def test_get_text_from_all_subpages_planqc(plancq):
    get_text_from_all_subpages("https://planqc.eu")
    assert os.path.exists(plancq) == True

def get_text_from_all_subpages(plancq):
    get_text_from_all_subpages(plancq)
    assert os.path.exists("./data/text_data/planqc.eu.txt")

