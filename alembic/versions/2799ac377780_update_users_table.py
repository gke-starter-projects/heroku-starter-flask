"""Update users table

Revision ID: 2799ac377780
Revises: 3cce56b906f2
Create Date: 2022-04-17 11:49:07.654756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2799ac377780'
down_revision = '3cce56b906f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'name',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('user', 'password',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'password',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('user', 'name',
                    existing_type=sa.TEXT(),
                    nullable=True)
    # ### end Alembic commands ###
