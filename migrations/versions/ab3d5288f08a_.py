"""empty message

Revision ID: ab3d5288f08a
Revises: 498e4428fc14
Create Date: 2023-11-21 19:35:48.180435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3d5288f08a'
down_revision = '498e4428fc14'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salt', sa.String(length=40), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=80),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
        batch_op.drop_column('salt')

    # ### end Alembic commands ###
