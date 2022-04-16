"""add content column to post table

Revision ID: 1c59c357eecc
Revises: c32cf4ca253a
Create Date: 2022-04-16 00:29:55.789169

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c59c357eecc'
down_revision = 'c32cf4ca253a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
