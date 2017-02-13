"""
restclient.py

Helper classes

Licensed under MIT license
(c) 2017 Reeleezee BV
"""
import requests
import re

class ApiClient(object):

    def __init__(self, uri, headers, username, password):
        self.__uri= uri
        self.__headers = headers
        self.__auth = (username, password)

    def GET(self, resource):
        return Response(requests.get(self.__uri + resource, headers=self.__headers, 
                                        auth=self.__auth))

    def PUT(self, resource, data):
        return Response(requests.put(self.__uri + resource, headers=self.__headers, 
                                        auth=self.__auth, data=data))

class Response:

    def __init__(self, response):
        self.__response = response
        # check for paging
        self.__next_link = self.content.get('@odata.nextLink', None)
        if self.__next_link != None:
            match = re.search(r'/api/[^/]+(.*)', self.__next_link)
            if match != None:
                self.__next_link = match.group(1)         

    @property
    def status_code(self):
        return self.__response.status_code

    @property
    def text(self):
        return self.__response.text        

    @property
    def content(self):
        return self.__response.json() if self.is_json else self.__response.text                
    
    @property
    def json(self):
        return self.__response.json()

    @property
    def next_link(self):
        return self.__next_link

    @property
    def is_json(self):
        return self.__response.headers['content-type'].startswith('application/json;')
