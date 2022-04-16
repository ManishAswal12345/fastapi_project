"""add last few columns to post table

Revision ID: 9079f71d4eb6
Revises: 6f4448487d4a
Create Date: 2022-04-16 10:09:49.779236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9079f71d4eb6'
down_revision = '6f4448487d4a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                                    nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                    nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
