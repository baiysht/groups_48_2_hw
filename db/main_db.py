# main_db.py
import sqlite3
from db import queries


db_shop = sqlite3.connect('db/shop')
db_product_details = sqlite3.connect('db/product_details')
cursor_shop = db_shop.cursor()
cursor_product_details = db_product_details.cursor()



async def DataBase_create():
    if db_shop and db_product_details:
        print('База данных подключена!')
    cursor_shop.execute(queries.CREATE_TABLE_shop)
    cursor_product_details.execute(queries.CREATE_TABLE_product_details)


async def sql_insert_shop(name_product, product_size, price, photo, productid):
    cursor_shop.execute(queries.INSERT_shop_QUERY, (
        name_product, product_size, price, photo, productid
    ))
    db_shop.commit()

async def sql_insert_product_details(productid, category, infoproduct):
    cursor_product_details.execute(queries.INSERT_product_details_QUERY, (
        productid, category, infoproduct
    ))
    db_product_details.commit()