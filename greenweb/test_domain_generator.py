import pytest
from domain_generator import gen_urls

def test_we_return_domains_with_no_trailing_chars():
    with open('top-50.csv') as csvfile:

        # create our generator
        urls = gen_urls(csvfile)
        
        # pull the first one off the generator
        google = next(urls)

        assert google == 'http://api.thegreenwebfoundation.org/greencheck/google.com'