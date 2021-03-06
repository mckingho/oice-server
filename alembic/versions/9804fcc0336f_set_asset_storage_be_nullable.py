"""Allow asset storage be null

Revision ID: 9804fcc0336f
Revises: 5a75f1d14bfe
Create Date: 2017-10-23 02:10:32.141508

"""

# revision identifiers, used by Alembic.
revision = '9804fcc0336f'
down_revision = '5a75f1d14bfe'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asset', 'content_type',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1024),
               nullable=True)
    op.alter_column('asset', 'storage',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1024),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('asset', 'storage',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1024),
               nullable=False)
    op.alter_column('asset', 'content_type',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=1024),
               nullable=False)
    # ### end Alembic commands ###
