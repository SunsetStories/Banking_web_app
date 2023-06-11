"""added transaction types

Revision ID: 3d020c48583a
Revises: 7432e9a42f27
Create Date: 2023-06-06 14:02:57.469868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d020c48583a'
down_revision = '7432e9a42f27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('transaction_type_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'transaction_type_table', ['transaction_type_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions_table', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('transaction_type_id')

    # ### end Alembic commands ###