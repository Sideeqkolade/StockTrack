#!/usr/bin/python3
""" a script holds the content of inventory page in a table
"""
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship 

Base = declarative_base()
""" creates a base class for ORM
"""

class Inventory(Base):
    """ Inventory class
    """

    __tablename__ = 'inventories'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    item_code = Column(String(128), nullable=False)
    item_name = Column(String(128), nullable=False)
    brand_name = Column(String(128), nullable=False)
    market_name = Column(String(128), nullable=False)
    supplier = Column(String(128), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit = Column(Integer, nullable=False)
    purchase_price = Column(Integer, nullable=False)
    percentage_profit = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)