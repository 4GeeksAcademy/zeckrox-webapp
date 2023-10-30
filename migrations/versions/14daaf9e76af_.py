"""empty message

Revision ID: 14daaf9e76af
Revises: 3a565482284f
Create Date: 2023-10-30 01:17:17.393355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14daaf9e76af'
down_revision = '3a565482284f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.alter_column('icon',
               existing_type=sa.VARCHAR(length=400),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payment', schema=None) as batch_op:
        batch_op.alter_column('icon',
               existing_type=sa.VARCHAR(length=400),
               nullable=False)

    # ### end Alembic commands ###
