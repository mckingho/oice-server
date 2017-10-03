"""Add is_trial in user

Revision ID: 448a0f79018
Revises: 125109a41d8
Create Date: 2016-12-20 13:23:37.681752

"""

# revision identifiers, used by Alembic.
revision = '448a0f79018'
down_revision = '9b4fe51811'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_trial', sa.Boolean(), server_default=sa.text('0'), nullable=False))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_trial')
    ### end Alembic commands ###
