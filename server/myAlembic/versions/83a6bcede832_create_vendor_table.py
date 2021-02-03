"""create_vendor_table

Revision ID: 83a6bcede832
Revises: 2d1b1471e9aa
Create Date: 2021-01-28 19:43:29.069333

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '83a6bcede832'
down_revision = '2d1b1471e9aa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('vendor',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.Column('phone', sa.String(length=16), nullable=False),
                    sa.Column('tax', sa.String(length=16), nullable=True),
                    sa.Column('company_address', sa.String(length=16), nullable=True),
                    sa.Column('shipping_address', sa.String(length=16), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    )


def downgrade():
    op.drop_table('vendor')
