#!/usr/bin/env python
"""
get_products.py

Example on how to get a productlist

Licensed under MIT license
(c) 2017 Reeleezee BV
"""
import sys
from apiclient import ApiClient
from products import Products
from settings import USERNAME, PASSWORD, URI, HEADERS

def get_products():
    resource = '/Products'

    try:
        client = ApiClient(URI, HEADERS, USERNAME, PASSWORD)

        while True:
            response = client.GET(resource)
            if response.status_code == 200 and response.is_json:
                products = Products(response.json)
                for product in products:
                    print ("{0:38} {1:40} {2:20} {3}".format(
                        product.id,
                        product.Description[:40] if product.Description != None else '', 
                        product.SearchName[:20] if product.SearchName != None else '', 
                        product.Price))
            else:
                print ("response error: %d - %s" % (response.status_code, response.text))

            # paging
            resource = response.next_link
            if (resource == None or response.status_code != 200):
                break

    except ValueError:
        print ("Unexpected data: ", response.text)
    except:
        print ("Unexpected error:", sys.exc_info()[0])

def main():
    get_products()

if __name__ == '__main__':
    main()