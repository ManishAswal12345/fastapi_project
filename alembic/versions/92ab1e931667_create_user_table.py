"""create user table

Revision ID: 92ab1e931667
Revises: 1c59c357eecc
Create Date: 2022-04-16 09:42:47.837635

"""
from time import time
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92ab1e931667'
down_revision = '1c59c357eecc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
