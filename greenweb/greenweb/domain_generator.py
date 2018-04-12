# -*- coding: utf-8 -*-
import zipfile
import requests

# Read a csv file, and return a generator for a spider to iterate through.
def gen_urls(file_object):

    while True:

        # Read a line from the file
        line = file_object.readline()

        # Drop out if there are no lines left to iterate through
        if not line:
            break

        # turn '1,google.com\n' to just 'google.com'
        domain = line.split(',')[1]
        trimmed_domain = domain.rstrip()

        yield "http://api.thegreenwebfoundation.org/greencheck/{}".format(
            trimmed_domain)

def cut_down_list(no_of_urls, file_path):
    """
    Fetch the top N urls from the list of urls, and write it to a new file, for iterating through
    """
    with open(file_path) as file:

        subection_filepath = "top-{}-subsection.csv".format(no_of_urls)
        with open(subection_filepath, 'w+') as subsection_file:

            for idx, line in enumerate(file):
                if idx < no_of_urls:
                    subsection_file.write(line)


    return subection_filepath

def fetch_top_mil():
    """
    Fetch the compressed top million urls file from AWS bucket, and decompresses it
    
    Returns a filepath that can be opened
    """

    file_path = 'top-1m.csv.zip'

    req = requests.get(
        'http://s3.amazonaws.com/alexa-static/{}'.format(file_path), stream=True)

    if req.status_code == 200:

        with open(file_path, 'wb') as fd:
            for chunk in req.iter_content(chunk_size=128):
                fd.write(chunk)

        return file_path

    # otherwise assume it failed
    return False


def decompress_top_mil(file_path):
    """
    Decompress the compressed file passed in. Assumes it's a zip file.
    """

    zip_ref = zipfile.ZipFile(file_path, 'r')
    zip_ref.extractall('.')
    zip_ref.close()
