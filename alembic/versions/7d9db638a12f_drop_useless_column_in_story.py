"""drop useless column in story

Revision ID: 7d9db638a12f
Revises: cb62bebedb4d
Create Date: 2017-06-16 12:52:24.656417

"""

# revision identifiers, used by Alembic.
revision = '7d9db638a12f'
down_revision = 'cb62bebedb4d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('story', 'on_going')
    op.drop_column('story', 'license')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('license', mysql.SMALLINT(display_width=6), server_default=sa.text("'0'"), autoincrement=False, nullable=False))
    op.add_column('story', sa.Column('on_going', mysql.TINYINT(display_width=1), server_default=sa.text("'1'"), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
