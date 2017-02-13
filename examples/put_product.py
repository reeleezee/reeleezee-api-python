#!/usr/bin/env python
"""
put_product.py

Example on how to create / update a product

Licensed under MIT license
(c) 2017 Reeleezee BV
"""
import sys
import uuid
import pprint
from apiclient import ApiClient
from products import Product
from settings import USERNAME, PASSWORD, URI, HEADERS

def put_product():
    RESOURCE = '/Products/'

    try:
        guid = str(uuid.uuid4())
        
        product = Product(None)
        product.Description = 'New product from API'
        product.SearchName = 'New API product'
        product.Comment = 'This product is created by the Python API client with id: ' + guid
        product.Price = 12.50

        client = ApiClient(URI, HEADERS, USERNAME, PASSWORD)
        response = client.PUT(RESOURCE + guid, product.json())
        if response.status_code == 200 and response.is_json:
            pprint.pprint(response.json)
            product = Product(response.json)
            print ("{0:38} {1:40} {2:20} {3}".format(
                product.id,
                product.Description[:40], 
                product.SearchName[:20], 
                product.Price))
        else:
            print ("response error: %d - %s" % (response.status_code, response.text))
    except ValueError:
        print ("Unexpected data: ", response.text)
    except:
        print ("Unexpected error:", sys.exc_info()[0])

def main():
    put_product()

if __name__ == '__main__':
    main()