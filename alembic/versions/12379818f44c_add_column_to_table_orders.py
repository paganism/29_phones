"""Add column to table orders

Revision ID: 12379818f44c
Revises: 6298086f7f79
Create Date: 2018-10-14 20:59:21.801211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12379818f44c'
down_revision = None
branch_labels = None
depends_on = None
normalized_phone_number_length = 100


def upgrade():
    op.add_column('orders', sa.Column('normalized_phone_number', sa.String(normalized_phone_number_length)))


def downgrade():
    op.drop_column('orders', 'normalized_phone_number')
