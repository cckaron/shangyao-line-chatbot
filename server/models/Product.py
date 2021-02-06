from venv import logger

from sqlalchemy.exc import SQLAlchemyError

from server.models import connection
from sqlalchemy import or_, desc
from datetime import datetime
from server.models.enum.status import status as e_status

db = connection.get_connection()


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    name = db.Column(db.String(length=128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(length=16), nullable=True)
    status = db.Column(db.Enum(e_status), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, vendor_id, name, quantity, unit, status, created_at, updated_at):
        self.id = id
        self.vendor_id = vendor_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.status = status
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add(self):
        s = db.session()
        s.expire_on_commit = False
        db.session.add(self)

        try:
            db.session.commit()
            return self
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @classmethod
    def find(cls, product_id):
        try:
            rtn = cls.query.filter_by(id=product_id).first()
            return rtn
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()

    @classmethod
    def findall(cls):
        try:
            rtn = cls.query.all()
            return rtn
        except SQLAlchemyError as e:
            logger.error(e.args)
            db.session.rollback()
            raise
        finally:
            db.session.close()
