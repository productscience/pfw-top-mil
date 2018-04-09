# -*- coding: utf-8 -*-

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
