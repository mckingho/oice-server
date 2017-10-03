"""Add user_subscription_payout table

Revision ID: de9dc089bb7c
Revises: 810fbe6bd66e
Create Date: 2017-05-25 14:00:21.285048

"""

# revision identifiers, used by Alembic.
revision = 'de9dc089bb7c'
down_revision = '810fbe6bd66e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_subscription_payout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('subscription_user_id', sa.Integer(), nullable=False),
    sa.Column('oice_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('platform', sa.Unicode(length=16), nullable=False),
    sa.Column('original_transaction_id', sa.Unicode(length=128), nullable=True),
    sa.Column('payout_amount', sa.Float(), server_default='0', nullable=False),
    sa.Column('is_paid', sa.Boolean(), server_default=sa.text('false'), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['oice_id'], ['oice.id'], ),
    sa.ForeignKeyConstraint(['subscription_user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('original_transaction_id')
    )
    op.create_index('usersubscriptionpayout_author_idx', 'user_subscription_payout', ['author_id', 'is_paid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_subscription_payout')
    # ### end Alembic commands ###
