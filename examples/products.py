"""
products.py

Product classes

Licensed under MIT license
(c) 2017 Reeleezee BV
"""
import json

class Products:
    def __init__(self, json):
        self.__dict__ = json

    def __getitem__(self, index):
        return Product(self.value[index])

class Product:
    def __init__(self, json):
        if json != None:
            self.__dict__ = json
        
    def json(self):
        return json.dumps(self.__dict__)