"""changed balance to decimal type

Revision ID: d514d7fb65e7
Revises: 617d91ff53bc
Create Date: 2023-06-05 18:17:54.651055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd514d7fb65e7'
down_revision = '617d91ff53bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.DOUBLE(),
               type_=sa.DECIMAL(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts_table', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.DECIMAL(),
               type_=sa.DOUBLE(),
               existing_nullable=True)

    # ### end Alembic commands ###
