"""empty message

Revision ID: a0e2bb5e60c3
Revises: 021c265adcfd
Create Date: 2023-06-05 17:14:19.803582

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0e2bb5e60c3'
down_revision = '021c265adcfd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.alter_column('balance',
               existing_type=sa.NUMERIC(precision=10, scale=2),
               type_=sa.Integer(),
               existing_nullable=True)
        batch_op.drop_constraint('uq_account_account_no', type_='unique')
        batch_op.drop_column('account_no')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_account_id', type_='foreignkey')
        batch_op.drop_column('account_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_user_account_id', 'account', ['account_id'], ['id'])

    with op.batch_alter_table('account', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_no', sa.VARCHAR(length=10), nullable=False))
        batch_op.create_unique_constraint('uq_account_account_no', ['account_no'])
        batch_op.alter_column('balance',
               existing_type=sa.Integer(),
               type_=sa.NUMERIC(precision=10, scale=2),
               existing_nullable=True)

    # ### end Alembic commands ###
