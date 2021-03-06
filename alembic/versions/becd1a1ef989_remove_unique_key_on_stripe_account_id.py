"""Remove unique key on stripe account id

Revision ID: becd1a1ef989
Revises: 2d106555cb25
Create Date: 2017-11-08 09:08:25.648271

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'becd1a1ef989'
down_revision = '2d106555cb25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('stripe_account_id', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('stripe_account_id', 'user', ['stripe_account_id'], unique=True)
    # ### end Alembic commands ###
