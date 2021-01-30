"""create company table

Revision ID: 2d1b1471e9aa
Revises: 
Create Date: 2021-01-23 22:14:11.671340

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '2d1b1471e9aa'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('company',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('tax', sa.String(length=16), nullable=True),
    sa.Column('address', sa.String(length=16), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    )

    #insert data
    seed()

def downgrade():
    op.drop_table('company')

def seed():
    # get metadata from current connection
    meta = sa.MetaData(bind=op.get_bind())

    # pass in tuple with tables we want to reflect, otherwise whole database will get reflected
    meta.reflect(only=('company',))

    # define table representation
    company_tbl = sa.Table('company', meta)

    timestamp = datetime.now()

    # insert records
    op.bulk_insert(company_tbl,
        [
            {
                'id':1, 'name':'上耀', 'phone':'0912345678', 'tax':'12345678',
                'address':'新北市新莊區', 'created_at':timestamp, 'updated_at':timestamp
            },
        ]
    )
