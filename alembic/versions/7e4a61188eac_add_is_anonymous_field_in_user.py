"""Add is_anonymous field in user

Revision ID: 7e4a61188eac
Revises: 86599aab5918
Create Date: 2017-06-16 13:20:37.347941

"""

# revision identifiers, used by Alembic.
revision = '7e4a61188eac'
down_revision = '86599aab5918'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_anonymous', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_anonymous')
    # ### end Alembic commands ###
