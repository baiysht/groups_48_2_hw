# queries.py

CREATE_TABLE_shop = """
    CREATE TABLE IF NOT EXISTS shop (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    product_size TEXT,
    price TEXT,
    photo TEXT,
    productid TEXT
    )
"""

INSERT_shop_QUERY = """
    INSERT INTO shop (name_product, product_size, price, photo, productid)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_product_details = """
    CREATE TABLE IF NOT EXISTS product_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT, 
    category TEXT,
    infoproduct TEXT
    )
"""

INSERT_product_details_QUERY = """
    INSERT INTO product_details (productid, category, infoproduct)
    VALUES (?, ?, ?)
"""