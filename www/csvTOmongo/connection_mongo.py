#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymongo
import config
"""
Module which connects to database
"""
# NOTE: passwords for script user are different on the two servers
def connection_db(host, port, database):
    """
    Connect to database
    """
    try:
        client = pymongo.MongoClient(host=host, port=port)
        db = client[database]
        return db, client
    except Exception as E:
        print(str(E))        

def connection_client(host, port):
    """
    Connect to database
    """
    try:
        client = pymongo.MongoClient(host=host, port=port)
        
        return client
    except Exception as E:
        print(str(E))        

def test():
    client1 = connection_client('localhost', 27017)
    client2 = connection_client('localhost', 27017)

test