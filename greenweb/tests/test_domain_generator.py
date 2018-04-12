import sys
import pytest
from pathlib import Path

cur_path = Path.cwd()
sys.path.append(str(cur_path))

from greenweb.domain_generator import (
    gen_urls, fetch_top_mil, cut_down_list, decompress_top_mil
)

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
    zip_string = 'top-1m.csv.zip'

    # setup
    if Path(zip_string).exists():
        # unlink is functionally the same as delete
        Path(zip_string).unlink()

    res = fetch_top_mil()

    assert res == zip_string
    assert Path(zip_string).exists()


@pytest.mark.slowtest
def test_decompress_top_mil():
    zip_string = 'top-1m.csv.zip'

    fetch_top_mil()

    assert Path(zip_string).exists()

    decompress_top_mil('top-1m.csv.zip')

    assert Path('top-1m.csv').exists()