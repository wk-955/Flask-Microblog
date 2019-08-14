"""empty message

Revision ID: d3c07245452e
Revises: ec23bfba47c7
Create Date: 2019-07-18 09:55:11.646908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3c07245452e'
down_revision = 'ec23bfba47c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
