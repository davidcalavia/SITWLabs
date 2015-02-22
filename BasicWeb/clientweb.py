#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 10/14/2014

@author: carlesm
'''

import urllib2


class Client(object):

    """Web Client, for www.udl.Created

    Downloads www.udl.cat main page to parse
    for agenda items"""

    def __init__(self):
        super(Client, self).__init__()

    def get_web_page(self, url):
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def run(self):
        # get web page
        # parse for data
        # print formatted data
        html = self.get_web_page("http://www.udl.cat/")
        print html


if __name__ == "__main__":
    client = Client()
    client.run()
