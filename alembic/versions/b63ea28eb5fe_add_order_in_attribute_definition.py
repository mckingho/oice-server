"""Add order in attribute definition

Revision ID: b63ea28eb5fe
Revises: becd1a1ef989
Create Date: 2017-11-09 03:50:04.539127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b63ea28eb5fe'
down_revision = 'becd1a1ef989'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attribute_definition', sa.Column('order', sa.Integer(), server_default='0', nullable=False))
    op.create_index('macro_order_idx', 'attribute_definition', ['macro_id', 'order'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('macro_order_idx', table_name='attribute_definition')
    op.drop_column('attribute_definition', 'order')
    # ### end Alembic commands ###
