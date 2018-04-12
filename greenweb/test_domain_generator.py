import os
import pytest
from domain_generator import gen_urls, cut_down_list, fetch_top_mil, decompress_top_mil

def test_we_return_domains_with_no_trailing_chars():
    with open('top-50.csv') as csvfile:

        # create our generator
        urls = gen_urls(csvfile)

        # pull the first one off the generator
        google = next(urls)

        assert google == 'http://api.thegreenwebfoundation.org/greencheck/google.com'

def test_we_make_subections_of_file():

    with open('top-50.csv') as csvfile:
        assert len(csvfile.readlines()) == 10

    subsection_filepath = cut_down_list(5, 'top-50.csv')

    with open(subsection_filepath) as subsection_file:
        assert len(subsection_file.readlines()) == 5


@pytest.mark.slowtest
def test_we_can_fetch_top_mil():

    assert os.path.exists('top-1m.csv.zip') == False

    res = fetch_top_mil()

    assert res == 'top-1m.csv.zip'
    assert os.path.exists('top-1m.csv.zip') == True

@pytest.mark.slowtest
def test_decompress_top_mil():
        
    fetch_top_mil()
    assert os.path.exists('top-1m.csv.zip') == True

    decompress_top_mil('top-1m.csv.zip')

    assert os.path.exists('top-1m.csv') == True