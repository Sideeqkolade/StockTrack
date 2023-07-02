#!/usr/bin/python3
""" a script that accesses the datas in a database
"""

import sys
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from inventory import Inventory

if __name__ == '__main__':
    def __init__(self):
        """ initializes the database
        """
        STOCKTRACK_USER = getenv('STOCKTRACK_USER')
        STOCKTRACK_PWD = getenv('STOCKTRACK_PWD')
        STOCKTRACK_HOST = getenv('STOCKTRACK_HOST')
        STOCKTRACK_DB = getenv('STOCKTRACK_DB')
        engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(STOCKTRACK_USER, STOCKTRACK_PWD, STOCKTRACK_HOST, STOCKTRACK_DB))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

    def display_items():
        """ displays the items table
        """
        inventories = session.query(Inventory.item_code, Inventory.brand_name, Inventory.market_name).all()
        session.close()