"""added id and modified account_num

Revision ID: 6f1c4ba81c56
Revises: 22e63872c9f0
Create Date: 2023-06-04 21:30:44.738419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f1c4ba81c56'
down_revision = '22e63872c9f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id', sa.Integer(), nullable=False))
        batch_op.alter_column('account_num',
               existing_type=sa.BIGINT(),
               nullable=True,
               autoincrement=True)
        batch_op.create_unique_constraint(None, ['account_num'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('account_num',
               existing_type=sa.BIGINT(),
               nullable=False,
               autoincrement=True)
        batch_op.drop_column('id')

    # ### end Alembic commands ###
