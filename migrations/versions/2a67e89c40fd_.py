"""empty message

Revision ID: 2a67e89c40fd
Revises: 46b1333eab49
Create Date: 2018-02-14 14:33:11.005086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a67e89c40fd'
down_revision = '46b1333eab49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('receiver', sa.String(), nullable=False))
    op.add_column('message', sa.Column('receiver_type', sa.String(), nullable=False))
    op.drop_column('message', 'to_type')
    op.drop_column('message', 'to')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('to', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('message', sa.Column('to_type', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('message', 'receiver_type')
    op.drop_column('message', 'receiver')
    # ### end Alembic commands ###
