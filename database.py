#!/usr/bin/python3
""" a script that accesses the datas in a database
"""
import io
import csv
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from inventory import Base, Inventory


STOCKTRACK_USER = getenv('STOCKTRACK_USER')
STOCKTRACK_PWD = getenv('STOCKTRACK_PWD')
STOCKTRACK_HOST = getenv('STOCKTRACK_HOST')
STOCKTRACK_DB = getenv('STOCKTRACK_DB')
engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(STOCKTRACK_USER, STOCKTRACK_PWD, STOCKTRACK_HOST, STOCKTRACK_DB),
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_data_db(data):
    """Adds the content of inventory form to the database"""

    try:
        item_code = data['item_code']
        item_name = data['item_name'] 
        brand_name = data['brand_name']
        market_name = data['market_name']
        supplier = data['supplier']
        quantity = data['quantity']
        unit = data['unit']
        purchase_price = data['purchase_price']
        percentage_profit = data['percentage_profit']
        date = data['date']

        new_inventory = Inventory(
            item_code=item_code,
            item_name=item_name,
            brand_name=brand_name,
            market_name=market_name,
            supplier=supplier,
            quantity=quantity,
            unit=unit,
            purchase_price=purchase_price,
            percentage_profit=percentage_profit,
            date=date
        )
        
        session.add(new_inventory)
        session.commit()

    except Exception as e:
        session.rollback()
        raise e


def show_items():
    """Returns items to be displayed on items page from the database"""
    
    try:
        result = session.query(
            Inventory.item_code,
            Inventory.item_name,
            Inventory.brand_name,
            Inventory.market_name
            ).distinct().all()

        session.close()
        return result

    except Exception as e:
        session.rollback()
        raise e
    
def show_purchase_report():
    """displays purchase reports from the datatbase"""

    try:
        purchase_report = session.query(
            Inventory.date,
            Inventory.supplier,
            Inventory.item_code,
            Inventory.item_name,
            Inventory.brand_name,
            Inventory.market_name,
            Inventory.quantity,
            Inventory.unit,
            Inventory.purchase_price,
        ).all()

        session.close()
        return purchase_report
    
    except Exception as e:
        session.rollback()
        raise e


def create_csv_string(report_data):
    """create a downloadable file in csv format"""

    try:
        csv_buffer = io.StringIO()
        csv_writer = csv.writer(csv_buffer)
        csv_writer.writerow(['Purchase Date', 'Supplier', 'Item Code', 'Item Name', 'Brand Name', 'Market Name', 'Quantity', 'Unit Price', 'Total Price'])

        for row in report_data:
            csv_writer.writerow(row)
        
        csv_data = csv_buffer.getvalue()
        csv_buffer.close()

        return csv_data

    except Exception as e:
        raise e
