from server.models import connection
from sqlalchemy import or_, desc

db = connection.getConnection()


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=64), nullable=False)
    phone = db.Column(db.String(length=16), nullable=False)
    tax = db.Column(db.String(length=16), nullable=False)
    address = db.Column(db.String(length=128), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    def __init__(self, id, name, phone, tax, address, created_at, updated_at):
        self.id = id
        self.name = name
        self.phone = phone
        self.tax = tax
        self.address = address
        self.created_at = created_at
        self.updated_at = updated_at

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
    def find(cls, company_id):
        try:
            rtn = cls.query.filter_by(id=company_id).first()
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
