"""create_product_table

Revision ID: ab9042fa4165
Revises: 83a6bcede832
Create Date: 2021-01-28 20:28:27.632509

"""
from alembic import op
import sqlalchemy as sa
import sys
from server.models.enum.status import status

# revision identifiers, used by Alembic.
revision = 'ab9042fa4165'
down_revision = '83a6bcede832'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('product',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('vendor_id', sa.Integer, sa.ForeignKey('vendor.id')),
                    sa.Column('name', sa.String(length=128), nullable=False),
                    sa.Column('quantity', sa.Integer, nullable=False),
                    sa.Column('unit', sa.String(length=16), nullable=True),
                    sa.Column('status', sa.Enum(status), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False)
                    )


def downgrade():
    pass
