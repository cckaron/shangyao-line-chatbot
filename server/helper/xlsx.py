import os
from venv import logger

import pandas as pd
import json

from sqlalchemy.exc import SQLAlchemyError

from server.config import Config
from server.models import connection
from server.models.Product import Product
from server.models.Vendor import Vendor

import sqlalchemy as sa

# get seeder path from config
seeder_path = os.path.join(Config.ASSETS_DIR, "seeder")

# get metadata from current connection
meta = sa.MetaData(bind=connection.get_connection())


def read_and_seed(db):
    with pd.ExcelFile(os.path.join(seeder_path, 'product.xlsx')) as xlsx:
        # for sheet_name in xlsx.sheet_names:
        rows = pd.read_excel(xlsx, "Vendor") \
            .to_json(orient='records', lines=True) \
            .splitlines()

        seed(db, "Vendor", rows)

        rows = pd.read_excel(xlsx, "Product") \
            .to_json(orient='records', lines=True) \
            .splitlines()

        seed(db, "Product", rows)


def seed(db, table, rows):
    for row in rows:
        row = json.loads(row)
        print(row)
        # db.session.add(Product(**row))
        exec("db.session.add(%s(**row))" % table)

    try:
        db.session.commit()
    except SQLAlchemyError as e:
        logger.error(e.args)
        db.session.rollback()
        return False
