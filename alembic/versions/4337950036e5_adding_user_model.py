"""Adding User Model

Revision ID: 4337950036e5
Revises: 6952b3ab684
Create Date: 2013-11-16 12:07:01.387863

"""

# revision identifiers, used by Alembic.
revision = '4337950036e5'
down_revision = '6952b3ab684'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.Unicode(), nullable=True),
    sa.Column('email', sa.Unicode(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
