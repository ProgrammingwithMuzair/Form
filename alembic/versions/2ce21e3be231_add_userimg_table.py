"""add userimg table

Revision ID: 2ce21e3be231
Revises: 1614316b8e85
Create Date: 2022-03-28 23:22:54.414559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce21e3be231'
down_revision = '1614316b8e85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userimage',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userid'], ['userdata.Id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userimage')
    # ### end Alembic commands ###
