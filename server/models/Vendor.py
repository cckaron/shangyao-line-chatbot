from server.models import connection
from sqlalchemy import or_, desc
from datetime import datetime
from server.models.enum.status import status as e_status
from server.models.enum.source import source as e_source

db = connection.get_connection()


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=128), nullable=False)
    phone = db.Column(db.String(length=16), nullable=False)
    tax = db.Column(db.String(length=16), nullable=True)
    company_address = db.Column(db.String(length=16), nullable=True)
    shipping_address = db.Column(db.String(length=16), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, name, phone, tax, company_address, shipping_address, created_at, updated_at):
        self.id = id
        self.name = name
        self.phone = phone
        self.tax = tax
        self.company_address = company_address
        self.shipping_address = shipping_address
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
    def find(cls, vendor_id):
        try:
            rtn = cls.query.filter_by(id=vendor_id).first()
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
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
