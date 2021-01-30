"""create company table

Revision ID: 2d1b1471e9aa
Revises: 
Create Date: 2021-01-23 22:14:11.671340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d1b1471e9aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('companies',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('tax', sa.String(length=16), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table('companies')
