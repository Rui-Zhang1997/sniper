#!/usr/bin/env python
""" This file implements a facade for the Rutgers Schedule of Classes API."""

# Requests is so awesome
import requests
from utils import get_current_tylc

class Soc:
    """ Communicates with Rutgers SOC """
    def __init__(self, term, year, campus):
        """ We always use certain parameters"""
        self.base_url = 'http://sis.rutgers.edu/soc/api/'
        self.params = (
            ('year', str(year)),
            ('term', str(term)),
            ('campus', str(campus)),
        )

        # Spoof the user agent for good measure
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.60 Safari/537.1',
        }


    def query(self, resource, params={}):
        """Queries the given resource (a string) with the given parameters.
        For example self.query('/api/subjects.json', { 'keyword': 'Computer Science' })"""
        params.update(self.params)

        r = requests.get(self.base_url + resource, params=params, headers=self.headers)

        if r.status_code == requests.codes.ok:
            return r.json()

        raise Exception('You made an invalid request %s: %s' % (r.status_code, r.text))

    def get_courses(self):
        """ Gives you a list of courses in a department """
        return self.query('/courses.gzip')
      
    def get_sections(self):
        return self.query('/openSections.gzip')
if __name__ == '__main__':
    soc = Soc(**get_current_tylc())
    #print(soc.get_courses(subject=198))
    import pdb; pdb.set_trace()
