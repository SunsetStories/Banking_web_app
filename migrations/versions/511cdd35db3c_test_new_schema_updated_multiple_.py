"""test new schema, updated multiple foreign keys

Revision ID: 511cdd35db3c
Revises: 77302b50b38e
Create Date: 2023-06-08 17:30:31.485769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '511cdd35db3c'
down_revision = '77302b50b38e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.drop_constraint('fk_transactions_table_receiver_accounts_table', type_='foreignkey')
        batch_op.drop_constraint('fk_transactions_table_sender_accounts_table', type_='foreignkey')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_transactions_table_sender_accounts_table', 'accounts_table', ['sender'], ['account_num'])
        batch_op.create_foreign_key('fk_transactions_table_receiver_accounts_table', 'accounts_table', ['receiver'], ['account_num'])

    # ### end Alembic commands ###