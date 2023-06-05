"""empty message

Revision ID: 4c322d2b56f5
Revises: a0e2bb5e60c3
Create Date: 2023-06-05 17:37:03.860663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c322d2b56f5'
down_revision = 'a0e2bb5e60c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('account')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('balance', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_account')
    )
    # ### end Alembic commands ###
