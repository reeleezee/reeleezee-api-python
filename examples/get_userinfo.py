#!/usr/bin/env python
"""
get_userinfo.py

Example on how to get the user info

Licensed under MIT license
(c) 2017 Reeleezee BV
"""
import sys
from apiclient import ApiClient
import pprint
from settings import USERNAME, PASSWORD, URI, HEADERS

def get_request(resource):
    return requests.get(URI + resource, headers=HEADERS, auth=(USERNAME, PASSWORD))

def get_userinfo():
    RESOURCE = '/UserInfo?$expand=*'

    try:
        client = ApiClient(URI, HEADERS, USERNAME, PASSWORD)
        response = client.GET(RESOURCE)
        if response.status_code == 200 and response.is_json:
            pprint.pprint(response.json)
        else:
            print ("response error: %d - %s" % (response.status_code, response.text))
    except ValueError:
        print ("Unexpected data: ", response.text)
    except:
        print ("Unexpected error:", sys.exc_info()[0])

def main():
    get_userinfo()

if __name__ == '__main__':
    main()